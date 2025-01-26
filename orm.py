from typing import Optional
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
  start_date: Mapped[datetime]
  end_date: Mapped[Optional[datetime]]
  location: Mapped[Optional[str]]
  cancelled: Mapped[bool] = mapped_column(default=False)
  attendees: Mapped[int]
  
  def __repr__(self) -> str:
    return f"Event(uid={self.uid}, name={self.name}, start_date={self.start_date}, end_date={self.end_date}, location={self.location}, cancelled={self.cancelled}, attendees={self.attendees})"
  