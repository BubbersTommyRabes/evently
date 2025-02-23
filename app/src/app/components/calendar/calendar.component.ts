import { Component, OnInit } from '@angular/core';
import { CalendarOptions, EventClickArg } from '@fullcalendar/core';
import { FullCalendarModule } from '@fullcalendar/angular';
import dayGridPlugin from '@fullcalendar/daygrid';
import interactionPlugin from '@fullcalendar/interaction';
import { DialogService } from 'primeng/dynamicdialog';
import { Event } from '../../models/event';
import { EventService } from '../../services/event.service';
import { EventDialogComponent } from '../event-dialog/event-dialog.component';

@Component({
  selector: 'app-calendar',
  imports: [FullCalendarModule],
  providers: [DialogService],
  templateUrl: './calendar.component.html',
  styleUrl: './calendar.component.scss',
  standalone: true
})
export class CalendarComponent implements OnInit {
  calendarOptions!: CalendarOptions;

  constructor(private eventService: EventService, private dialogService: DialogService) {}

  ngOnInit() {
    this.calendarOptions = {
      plugins: [dayGridPlugin, interactionPlugin],
      initialView: 'dayGridMonth',
      events: this.eventService.getEvents(),
      eventClick: this.handleEventClick.bind(this),
      headerToolbar: {
        left: 'prev,next today',
        center: 'title',
        right: 'addEvent'
      },
      customButtons: {
        addEvent: {
          text: 'Add Event',
          click: this.openAddEventDialog.bind(this)
        }
      },
      eventColor: '#3788d8', // Default event color
      height: 'auto'
    };
  }

  handleEventClick(arg: EventClickArg) {
    this.dialogService.open(EventDialogComponent, {
      header: 'Event Details',
      width: '30%',
      data: {
        event: {
          id: Number(arg.event.id),
          title: arg.event.title,
          start: arg.event.start,
          end: arg.event.end,
          description: arg.event.extendedProps['description']
        }
      }
    });
  }

  openAddEventDialog() {
    const ref = this.dialogService.open(EventDialogComponent, {
      header: 'Add New Event',
      width: '30%',
      data: { isNew: true }
    });

    ref.onClose.subscribe((newEvent: Event) => {
      if (newEvent) {
        this.eventService.addEvent(newEvent);
        this.calendarOptions = {
          ...this.calendarOptions,
          events: this.eventService.getEvents()
        };
      }
    });
  }
}
