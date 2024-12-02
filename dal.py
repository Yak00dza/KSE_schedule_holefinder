from group_combination import GroupCombination
from week import Week
from config import get_cfg_option()
import json
import openpyxl

class DAL: #Data Abstraction Layer
    def __init__(self, filename):
        self.filename = filename

    def load_sheet(selfm sheet_name):
        workbook = openpyxl.load_workbook(self.filename)
        return workbook.get_sheet_by_name(sheet_name)     

    def fetch_schedule(self): 
        sheet = self.load_sheet(get_cfg_option('schedule_sheet'))
        #TODO: implement
        return None

    def fetch_groups(self): #returns {student_email -> their groups}
        sheet = self.load_sheet(get_cfg_option('groups_sheet'))
        #TODO: implement
        return None 

    def write_holes_to_json(self, holes):
        pass

    def get_groups_by_email(self) -> GroupCombination:
        pass

    def get_week_by_number(self) -> Week:
        pass
