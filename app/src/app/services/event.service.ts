import { Injectable } from '@angular/core';
import { Event } from '../models/event';

@Injectable({
  providedIn: 'root'
})
export class EventService {
  private events: Event[] = [];

  constructor() {
    this.events.push(
      { uid: '1', name: 'Team Meeting', startDate: new Date(2025, 1, 23, 10, 0), endDate: new Date(2025, 1, 23, 11, 0) },
      { uid: '2', name: 'Dentist', startDate: new Date(2025, 1, 25, 14, 0), endDate: new Date(2025, 1, 25, 15, 0) }
    );
  }

  getEvents(): Event[] {
    return [...this.events]
  }

  addEvent(event: Event) {
    event.uid = `${this.events.length + 1}`;
    this.events.push(event);
  }
}
