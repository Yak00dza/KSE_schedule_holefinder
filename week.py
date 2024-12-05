from day import Day

class Week:
    def __init__(self, days):
        self.days = days

    def get_days(self):
        return self.days

    def get_day_n(self, n) -> Day:
        return self.days[n-1]
