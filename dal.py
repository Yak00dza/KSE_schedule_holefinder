from openpyxl.reader.excel import load_workbook
from group_combination import GroupCombination
from week import Week
from config import get_cfg_option
import json
import openpyxl

class DAL: #Data Abstraction Layer
    def __init__(self, filename):
        self.filename = filename

    def load_sheet(self, sheet_name):
        workbook = openpyxl.load_workbook(self.filename,read_only=True, data_only=True)
        return workbook[sheet_name]

    def fetch_schedule(self):
        sheet = self.load_sheet(get_cfg_option('schedule_sheet'))
        #TODO: implement
        return None

    # returns {student_email -> their groups}
    def fetch_groups(self):
        worksheet = self.load_sheet(get_cfg_option('groups_sheet_name'))
        email_column_name = get_cfg_option('groups_sheet_column_info')['email_column_name']
        columns_for_student_info = get_cfg_option('groups_sheet_column_info')['columns_for_student_info']

        row = list(worksheet.iter_rows(max_row=1, values_only=True))[0]
        header = [column_name for column_name in row if column_name]

        email_ind = header.index(email_column_name)

        info = {}
        for row in worksheet.iter_rows(min_row=2, values_only=True):
            email = row[email_ind]
            if not email:
                break
            if email not in info:  # one student can have two majors so email might happen twice
                info[email] = []
            info[email] += [group for group in row[columns_for_student_info::] if group]

        return info

    def write_holes_to_json(self, holes):
        pass

    def get_groups_by_email(self) -> GroupCombination:
        pass

    def get_week_by_number(self) -> Week:
        pass


