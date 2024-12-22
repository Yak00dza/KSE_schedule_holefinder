CLASSES_PER_DAY = 8

class Day:
    def __init__(self, classes):
        self.classes = classes

    def get_schedule_of(self, group_combination):
        schedule = ['FREE'] * CLASSES_PER_DAY
        n = len(self.classes)
        taken = []

        for i in range(n):
            current_class = self.classes[i] 
            if current_class.intersects(group_combination):
                taken.append(i+1)
                intersection = current_class.get_intersection(group_combination)
                schedule[i] = ' | '.join(intersection.groups)

        if len(taken) == 0:
            return schedule

        for i in range(taken[0], taken[-1]):
            if i not in taken:
                schedule[i-1] = 'HOLE'

        return schedule
