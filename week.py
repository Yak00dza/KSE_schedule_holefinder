from day import Day

class Week:
    def __init__(self, days):
        self.days = days

    def get_schedule_of(self, group_combination):
        result = {}
        for day in self.days:
            result[day] = day.get_schedule_of(group_combination)

        return result
        
