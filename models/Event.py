from datetime import datetime
from typing import Any, Optional, Self
from pydantic import BaseModel, ValidationError, model_validator

class EventIn(BaseModel):
  name: str
  host_id: Optional[str]
  start_date: datetime
  end_date: Optional[datetime]
  location: Optional[str]
  attendees: int

class EventOut(BaseModel):
  uid: str | None
  name: str
  host_id: Optional[str]
  start_date: datetime
  end_date: datetime
  location: str
  cancelled: bool
  attendees: int
  
class EventUpdate(BaseModel):
  name: str | None = None
  host_id: Optional[str] = None
  start_date: datetime | None = None
  end_date: Optional[datetime] = None
  location: Optional[str] = None
  cancelled: bool | None = None
  attendees: int | None = None
  
  @model_validator(mode="after")
  def validate(self) -> Self:
    json_payload = self.model_dump(exclude_unset=True)
    errors: list[str] = []
    for field_name in ["name", "start_date", "cancelled", "attendees"]:
      error = EventUpdate.validate_required_field(json_payload, field_name)
      if error is not None:
        errors.append(error)
    if len(errors) > 0:
      raise ValueError(f"Required fields cannot be unset: [{'; '.join(errors)}]")
    return self
  
  @staticmethod
  def validate_required_field(json_payload: dict[str, Any], field_name: str) -> str | None:
    if field_name in json_payload and json_payload[field_name] is None:
      return f"Field '{field_name}' cannot be null"
    return None