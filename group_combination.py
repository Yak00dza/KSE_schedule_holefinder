class GroupCombination:
    def __init__(self, groups=[]):
        self.groups = groups

    def add_group(self, group):
        self.groups.append(group)

    def contains(self, group) -> bool:
        return group in self.groups

    def get_intersection(self, group_combination):
        intersection = GroupCombination()
        for group in self.groups:
            if group_combination.contains(group):
                intersection.add_group(group)
        return intersection

    def intersects(self, group_combination) -> bool:
        for group in self.groups:
            if group_combination.contains(group):
                return True
        return False

    def __add__(self, another):
        for group in self.groups:
            if not another.contains(group):
                another.add_group(group)
        return another

    def __str__(self):
        return str(self.groups)

