from typing import Any, Optional, Self
from datetime import datetime
from sqlalchemy import UUID
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
import uuid

class Base(DeclarativeBase):
  pass

class Event(Base):
  __tablename__ = "event"
  
  uid: Mapped[UUID] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
  name: Mapped[str]
  host_id: Mapped[Optional[str]]
  start_date: Mapped[datetime]
  end_date: Mapped[Optional[datetime]]
  location: Mapped[Optional[str]]
  cancelled: Mapped[bool] = mapped_column(default=False)
  attendees: Mapped[int]
  
  def apply(self, updates: dict[str, Any]) -> Self:
    keys = updates.keys()
    if "name" in keys:
      self.name = updates["name"]
    if "host_id" in keys:
      self.host_id = updates["host_id"]
    if "start_date" in keys:
      self.start_date = updates["start_date"]
    if "end_date" in keys:
      self.end_date = updates["end_date"]
    if "location" in keys:
      self.location = updates["location"]
    if "cancelled" in keys:
      self.cancelled = updates["cancelled"]
    if "attendees" in keys:
      self.attendees = updates["attendees"]
    return self
  
  def __repr__(self) -> str:
    return f"Event(uid={self.uid}, name={self.name}, host_id={self.host_id}, start_date={self.start_date}, end_date={self.end_date}, location={self.location}, cancelled={self.cancelled}, attendees={self.attendees})"
  