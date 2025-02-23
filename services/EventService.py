from datetime import datetime
from typing import Annotated, Any, List

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.orm import Session
from models.Event import EventIn, EventOut
from session import get_session
from orm import Event as EventDB
from uuid import UUID

class EventService:
  
  def __init__(self, session: Annotated[Session, Depends(get_session)]):
    self.session = session
  
  def find_all(self) -> List[EventOut]:
    query = select(EventDB)
    results = self.session.execute(query)
    events = []
    for row in results:
      events.append(self.to_model(row[0]))
    return events
  
  def find_by_uid(self, uid: str) -> EventOut | None:
    event_db = self.session.get(EventDB, UUID(uid))
    return None if event_db is None else self.to_model(event_db)
  
  def find_by_host(self, host_id: str, start_date: datetime | None, end_date: datetime | None) -> List[EventOut]:
    query = select(EventDB).where(EventDB.host_id == host_id)
    if start_date is not None:
      query = query.where((EventDB.end_date or start_date) >= start_date)
    if end_date is not None:
      query = query.where(EventDB.start_date <= end_date)

    results = self.session.execute(query)
    events = []
    for row in results:
      events.append(self.to_model(row[0]))
    return events
  
  def save(self, event: EventIn) -> EventOut:
    try:
      event_db = self.to_entity(event)
      self.session.add(event_db)
      self.session.commit()
      return self.to_model(event_db)
    except Exception as e:
      self.session.rollback()
      raise e

  def update(self, uid: str, updates: dict[str, Any]) -> EventOut:
    event_db = self.session.get(EventDB, UUID(uid))
    event_db.apply(updates)
    self.session.commit()
  
  def to_entity(self, event: EventIn) -> EventDB:
    return EventDB(
      name=event.name,
      host_id=event.host_id,
      start_date=event.start_date,
      end_date=event.end_date,
      location=event.location,
      cancelled=False,
      attendees=event.attendees,
    )
  
  def to_model(self, event: EventDB) -> EventOut:
    return EventOut(
      uid=str(event.uid),
      name=event.name,
      host_id=str(event.host_id),
      start_date=event.start_date,
      end_date=event.end_date,
      location=event.location,
      cancelled=event.cancelled,
      attendees=event.attendees,
    )