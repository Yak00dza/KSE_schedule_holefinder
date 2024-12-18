from day import Day

class Week:
    def __init__(self, days):
        self.days = days

    def find_holes_in(self, group_combination):
        result = {}
        for day in self.days:
            holes = day.find_holes_in(group_combination)
            result[day] = holes

        return result
        
