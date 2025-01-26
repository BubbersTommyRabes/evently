from datetime import datetime
from typing import Annotated, List

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
  
  def save(self, event: EventIn) -> EventOut:
    try:
      event_db = self.to_entity(event)
      self.session.add(event_db)
      self.session.commit()
      return self.to_model(event_db)
    except Exception as e:
      self.session.rollback()
      raise e
  
  def to_entity(self, event: EventIn) -> EventDB:
    return EventDB(
      name=event.name,
      start_date=event.start_date,
      end_date=event.end_date,
      location=event.location,
      cancelled=event.cancelled,
      attendees=event.attendees,
    )
  
  def to_model(self, event: EventDB) -> EventOut:
    return EventOut(
      uid=str(event.uid),
      name=event.name,
      start_date=event.start_date,
      end_date=event.end_date,
      location=event.location,
      cancelled=event.cancelled,
      attendees=event.attendees,
    )