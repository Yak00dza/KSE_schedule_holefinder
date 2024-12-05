class GroupCombination:
    def __init__(self, groups):
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
