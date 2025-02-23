import { Component, OnInit } from '@angular/core';
import { Event } from '../../models/event';
import { DynamicDialogConfig, DynamicDialogRef } from 'primeng/dynamicdialog';
import { Calendar } from 'primeng/calendar';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-event-dialog',
  imports: [FormsModule, Calendar],
  templateUrl: './event-dialog.component.html',
  styleUrl: './event-dialog.component.scss'
})
export class EventDialogComponent implements OnInit {
  event: Event = { uid: '0', name: '', startDate: new Date(), endDate: new Date() };
  isNew: boolean = false;
  
  constructor(public ref: DynamicDialogRef, public config: DynamicDialogConfig) {}

  ngOnInit() {
    if (this.config.data) {
      this.isNew = this.config.data.isNew || false;
      if (!this.isNew) {
        this.event = { ...this.config.data.event };
      }
    }
  }

  save() {
    this.ref.close(this.event);
  }

  cancel() {
    this.ref.close();
  }
}
