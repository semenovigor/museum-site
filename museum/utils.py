from datetime import datetime, timedelta, date
from calendar import HTMLCalendar
from django.conf import settings
from .models import Event
from django.utils import dateformat


class Calendar(HTMLCalendar):
    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        super(Calendar, self).__init__()

    def formatday(self, day, events):
        events_per_day = events.filter(start_time__day=day)
        d = ''
        for event in events_per_day:
            d += f'<li> {event}</li>' \
                 f'<li class="none-marker">{event.start_time.hour}{":"}{event.start_time.minute}{"-"}{event.end_time.hour}' \
                 f'{":"}{event.end_time.minute}</li>'

        if day != 0:
            if day == datetime.now().day:
                return f'<div class="col jsEvent py-3">' \
                       f'<button class="btn calendarDayNumber ' \
                       f'buttonHoverCal w-100 currentDay' \
                       f' "data-toggle="collapse" data-target="#collapse_{day}" aria-expanded="true"' \
                       f' aria-controls="collapse_{day}">' \
                       f'{day}</button>' \
                       f'' \
                       f' <div id="collapse_{day}" aria-labelledby="{day}" class="collapse"' \
                       f'data-parent="#accordion"><ul class="event-calendar-text pt-4"> {d}' \
                       f'</ul></div></div> '

            return f'<div class="col jsEvent py-3">' \
                   f'<button class="btn calendarDayNumber ' \
                   f'buttonHoverCal w-100' \
                   f' "data-toggle="collapse" data-target="#collapse_{day}" aria-expanded="true"' \
                   f' aria-controls="collapse_{day}">' \
                   f'{day}</button>' \
                   f'' \
                   f' <div id="collapse_{day}" aria-labelledby="{day}" class="collapse"' \
                   f'data-parent="#accordion"><ul class="event-calendar-text pt-4"> {d}</ul>' \
                   f'</div></div>'
        return '<div class="col"></div>'

    # formats a week as a tr
    def formatweek(self, theweek, events):
        week = ''
        for d, weekday in theweek:
            week += self.formatday(d, events)
        return f'<div class="row pt-4"> {week} </div>'

    # formats a month as a table
    # filter events by year and month
    def formatmonth(self, withyear=True):
        events = Event.objects.filter(start_time__year=self.year, start_time__month=self.month)
        cal = f'\n'
        if self.month == 1:
            cal += f'<div class="row calendar-month-name pb-4 d-flex justify-content-center text-uppercase">' \
                   f'{"Январь-"}{self.year}</div>\n '
        if self.month == 2:
            cal += f'<div class="row calendar-month-name pb-4 d-flex justify-content-center text-uppercase">' \
                   f'{"Февраль-"}{self.year}</div>\n '
        if self.month == 3:
            cal += f'<div class="row calendar-month-name pb-4 d-flex justify-content-center text-uppercase">' \
                   f'{"Март-"}{self.year}</div>\n'
        if self.month == 4:
            cal += f'<div class="row calendar-month-name pb-4 d-flex justify-content-center text-uppercase">' \
                   f'{"Апрель-"}{self.year}</div>\n '
        if self.month == 5:
            cal += f'<div class="row calendar-month-name pb-4 d-flex justify-content-center text-uppercase">' \
                   f'{"Май-"}{self.year}</div>\n'
        if self.month == 6:
            cal += f'<div class="row calendar-month-name pb-4 d-flex justify-content-center text-uppercase">' \
                   f'{"Июнь-"}{self.year}</div>\n'
        if self.month == 7:
            cal += f'<div class="row calendar-month-name pb-4 d-flex justify-content-center text-uppercase">' \
                   f'{"Июль-"}{self.year}</div>\n'
        if self.month == 8:
            cal += f'<div class="row calendar-month-name pb-4 d-flex justify-content-center text-uppercase">' \
                   f'{"Август-"}{self.year}</div>\n'
        if self.month == 9:
            cal += f'<div class="row calendar-month-name pb-4 d-flex justify-content-center text-uppercase">' \
                   f'{"Сентябрь-"}{self.year}</div>\n'
        if self.month == 10:
            cal += f'<div class="row calendar-month-name pb-4 d-flex justify-content-center text-uppercase">' \
                   f'{"Октябрь-"}{self.year}</div>\n'
        if self.month == 11:
            cal += f'<div class="row calendar-month-name pb-4 d-flex justify-content-center text-uppercase">' \
                   f'{"Ноябрь-"}{self.year}</div>\n'
        if self.month == 12:
            cal += f'<div class="row calendar-month-name pb-4 d-flex justify-content-center text-uppercase">' \
                   f'{"Декабрь-"}{self.year}</div>\n'
        cal += f'<div class="pl-2 row">' \
               f'<div class="col">' \
               f'<div class="col text-name-day text-center pb-3 ">{"Пн"}</div>' \
               f'<div class="d-flex justify-content-center">' \
               f'<div class="w-50 line-under-name-day"></div></div></div>' \
               f'<div class="col">' \
               f'<div class="col text-name-day text-center pb-3 ">{"Вт"}</div>' \
               f'<div class="d-flex justify-content-center">' \
               f'<div class="w-50 line-under-name-day"></div></div></div>' \
               f'<div class="col">' \
               f'<div class="col text-name-day text-center pb-3 ">{"Ср"}</div>' \
               f'<div class="d-flex justify-content-center">' \
               f'<div class="w-50 line-under-name-day"></div></div></div>' \
               f'<div class="col">' \
               f'<div class="col text-name-day text-center pb-3 ">{"Чт"}</div>' \
               f'<div class="d-flex justify-content-center">' \
               f'<div class="w-50 line-under-name-day"></div></div></div>' \
               f'<div class="col">' \
               f'<div class="col text-name-day text-center pb-3 ">{"Пт"}</div>' \
               f'<div class="d-flex justify-content-center">' \
               f'<div class="w-50 line-under-name-day"></div></div></div>' \
               f'<div class="col">' \
               f'<div class="col text-name-day text-center text-name-day-red pb-3 ">{"Сб"}</div>' \
               f'<div class="d-flex justify-content-center">' \
               f'<div class="w-50 line-under-name-day-red"></div></div></div>' \
               f'<div class="col">' \
               f'<div class="col text-name-day text-center text-name-day-red pb-3 ">{"Вс"}</div>' \
               f'<div class="d-flex justify-content-center">' \
               f'<div class="w-50 line-under-name-day-red"></div></div></div>' \
               f'</div>\n'
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f'<div><div class="accordion" id="accordion">' \
                   f'<div class="col text-center">{self.formatweek(week, events)}</div>' \
                   f'</div></div>\n'
        return cal
