from typing import Annotated, List
from fastapi import APIRouter, Depends, HTTPException, Response, status

from models.Event import EventIn, EventOut, EventUpdate
from services.EventService import EventService

router = APIRouter(prefix="/events")

@router.get("/", response_model=List[EventOut], status_code=status.HTTP_200_OK)
def list_events(service: Annotated[EventService, Depends(EventService)]):
  events = service.find_all()
  return events

@router.get("/{event_uid}", response_model=EventOut, status_code=status.HTTP_200_OK)
def get_event(event_uid: str, service: Annotated[EventService, Depends(EventService)]):
  event = service.find_by_uid(event_uid)
  if event is None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Event not found")
  return event

@router.post("/", response_model=EventOut, status_code=status.HTTP_201_CREATED)
def save_event(event: EventIn, service: Annotated[EventService, Depends(EventService)], response: Response):
  saved_event = service.save(event)
  response.headers["Location"] = f"/events/{saved_event.uid}"
  return saved_event

@router.patch("/{event_uid}", status_code=status.HTTP_204_NO_CONTENT)
def patch_event(event_uid: str, event: EventUpdate, service: Annotated[EventService, Depends(EventService)]):
  service.update(event_uid, event.model_dump(exclude_unset=True))