class Day:
    def __init__(self, classes):
        self.classes = classes

    def find_holes_in(self, group_combination):
        n = len(self.classes)
        taken = []

        for i in range(n):
            if self.classes[i].intersects(group_combination):
                taken.append(i+1)

        if len(taken) == 0:
            return []

        holes = [i for i in range(taken[0], taken[-1]) if i not in taken]

        return holes
