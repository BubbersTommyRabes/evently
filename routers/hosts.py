from datetime import datetime
from typing import Annotated, List
from fastapi import APIRouter, Depends, status

from models.Event import EventOut
from services.EventService import EventService

router = APIRouter(prefix="/hosts")

@router.get("/{host_id}/events", response_model=List[EventOut], status_code=status.HTTP_200_OK)
def get_host_events(host_id: str, service: Annotated[EventService, Depends(EventService)], start_date: datetime | None = None, end_date: datetime | None = None):
  return service.find_by_host(host_id, start_date, end_date)