from group_combination import GroupCombination
from week import Week
import json
import openpyxl

class DAL: #Data Abstraction Layer
    def __init__(self, filename):
        self.filename = filename

    def fetch_schedule(self):
        pass

    def fetch_groups(self):
        pass

    def write_holes_to_json(pass):
        pass

    def get_groups_by_email(pass) -> GroupCombination:
        pass

    def get_week_by_number(pass) -> Week:
        pass
