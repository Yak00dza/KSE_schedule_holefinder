class Day:
    def __init__(self, classes):
        self.classes = classes

    def discover_holes_in(self, group_combination):
        n = len(self.classes)
        taken = [False] * n

        for i in range(n):
            if self.classes[n].intersects(self, group_combination):
                taken[i] = True

        holes = []
        prev = 0
        for i in range(1, len(taken)):
            if taken[i] == True and taken[prev] == False:
                holes.append(i+1)
            prev = i

        return holes
