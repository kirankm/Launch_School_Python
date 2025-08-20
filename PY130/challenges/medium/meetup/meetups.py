from datetime import datetime, timedelta

class Meetup:
    DAY_OF_WEEK = {
        'sunday': 6,
        'monday': 0,
        'tuesday': 1,
        'wednesday': 2,
        'thursday': 3,
        'friday': 4,
        'saturday': 5,
    }

    SCHEDULE_START_DAY = {
        'first': 1,
        'second': 8,
        'third': 15,
        'fourth': 22,
        'fifth': 29,
        'teenth': 13,
        'last': None,
    }

    def __init__(self, year, month):
        self.year = year
        self.month = month
        self.first_day = datetime(year, month, 1)


    