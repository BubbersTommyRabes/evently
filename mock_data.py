from orm import Event
from datetime import datetime
import uuid

mock_events = [
  Event(name="Christmas dinner recipes", host_id=str(uuid.uuid4()), start_date=datetime(2024, 12, 10, 10, 0, 0),
    end_date=datetime(2024, 12, 10, 16, 0, 0), location="Sagewood Cooking Academy", cancelled=False, attendees=20),
  Event(name="Best dishes for 2025", host_id=str(uuid.uuid4()), start_date=datetime(2024, 12, 27, 8, 0, 0),
    end_date=datetime(2024, 12, 28, 15, 0, 0), location="Briarstone Culinary Institute", cancelled=False, attendees=50),
  Event(name="Sage Chicken recipe", host_id=str(uuid.uuid4()), start_date=datetime(2024, 11, 23, 12, 30, 0),
    end_date=datetime(2024, 11, 23, 15, 30, 0), location="Maple Hollow Kitchen Studios", cancelled=False, attendees=7),
  Event(name="Truffle Risotto class", host_id=str(uuid.uuid4()), start_date=datetime(2025, 1, 16, 9, 0, 0),
    end_date=datetime(2025, 1, 16, 16, 30, 0), location="Cedarvale Gastronomy School", cancelled=True, attendees=30),
  Event(name="Make Pear Tart in 30 min", host_id=str(uuid.uuid4()), start_date=datetime(2025, 9, 4, 10, 0, 0),
    end_date=datetime(2025, 9, 4, 13, 0, 0), location="Thyme Ridge Culinary Center", cancelled=False, attendees=15),
  Event(name="Citrus Bass", host_id=str(uuid.uuid4()), start_date=datetime(2025, 4, 11, 9, 30, 0),
    end_date=datetime(2024, 4, 11, 11, 30, 0), location="Willowbrook Chef’s Atelier", cancelled=False, attendees=4),
]