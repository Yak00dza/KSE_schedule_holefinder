from day import Day
from group_combination import GroupCombination
from week import Week
from config import get_cfg_option
import openpyxl

class DAL: #Data Abstraction Layer
    def __init__(self, filename):
        self.filename = filename

    def load_sheet(self, sheet_name):
        workbook = openpyxl.load_workbook(self.filename,read_only=True, data_only=True)
        return workbook[sheet_name]

    def fetch_schedule(self):
        worksheet = self.load_sheet(get_cfg_option('schedule_sheet'))
        config = get_cfg_option("schedule_sheet_info")
        rows = config["rows_per_week_including_gap_rows_and_weeks_name_rows"]
        lesson_rows = config["lessons_per_day"]
        columns = config["columns_per_work_day"]
        saturday_columns = config["columns_for_saturday"]
        days = config["scheduled_days"]
        total_weeks = config["total_weeks_this_term"]
        #first column is time slots
        #first row is a gap row
        #second row is a number of the week
        #no sunday
        all_weeks = []

        row_index = 0
        for row in worksheet.iter_rows(min_col = 2, max_row= total_weeks * rows, values_only=True):
            row_index += 1

            if row_index % rows == 2:
                new_week = Week([Day([]) for i in range(days)])

            if (row_index - 1) % rows in range(rows - lesson_rows, rows):
                day_chunks = []
                for i in range(1,days + 1):
                    if i < 6:
                        day_chunks.append([i for i in row[(i - 1) * columns : i * columns] if i])
                    else:
                        day_chunks.append([i for i in row[(i - 1) * columns : (i - 1) * columns + saturday_columns] if i])

                # even if chunk is empty list mustn't delete because messes up days order
                day_chunks = [GroupCombination(chunk) for chunk in day_chunks]
                for i in range(days):
                    new_week.days[i].classes.append(day_chunks[i])

            if row_index % rows == 0:
                all_weeks.append(new_week)

        return all_weeks


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
                continue
            if email not in info:  # one student can have two majors so email might happen twice
                info[email] = GroupCombination()
            info[email] += GroupCombination([group for group in row[columns_for_student_info::] if group])

        return info

    def write_holes_to_json(self, holes):
        pass

    def get_groups_by_email(self) -> GroupCombination:
        pass

    def get_week_by_number(self) -> Week:
        pass




