from datetime import datetime
from pydantic import BaseModel

class EventIn(BaseModel):
  name: str
  start_date: datetime
  end_date: datetime
  location: str
  cancelled: bool
  attendees: int

class EventOut(BaseModel):
  uid: str | None
  name: str
  start_date: datetime
  end_date: datetime
  location: str
  cancelled: bool
  attendees: int