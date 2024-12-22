from argparse import ArgumentParser
import logic
from dal import DAL
from openpyxl import Workbook
from openpyxl.styles import PatternFill
from openpyxl.formatting.rule import CellIsRule, FormulaRule

def init_arg_parser():
    parser = ArgumentParser(prog='holefinder', description='CLI program to find the holes in the schedule') 

    parser.add_argument('filename', help='.xlsx file with the schedule information')

    return parser

def get_args():
    parser = init_arg_parser()
    return parser.parse_args()

def save_result_to_xlsx(result):
    workbook = Workbook()
    key_order = sorted(result.keys(), key = lambda x: result[x]['total_holes'] + result[x]['total_overlaps'], reverse=True)
    for groups_hash in key_order:
        info = result[groups_hash]
        workbook.create_sheet(str(groups_hash))
        sheet = workbook[str(groups_hash)]

        sheet.append(['Total holes:', info['total_holes']])
        sheet.append(['Total overlaps:', info['total_overlaps']])
        sheet.append([])

        sheet.append(['Groups:'])
        sheet.append(info['groups'].groups)
        sheet.append([])

        sheet.append(['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб'])
        for week in info['schedule']:
            for i in range(8): #8 classes per day
                sheet.append([day[i] for day in week.values()])
            sheet.append([])

        start_row = 8  # Data starts after the header
        end_row = sheet.max_row
        start_col = 1
        end_col = sheet.max_column
        range_address = f"{sheet.cell(row=start_row, column=start_col).coordinate}:{sheet.cell(row=end_row, column=end_col).coordinate}"


        red_fill = PatternFill(start_color="FF0000", end_color="FF0000", fill_type="solid")
        green_fill = PatternFill(start_color="00FF00", end_color="00FF00", fill_type="solid") 
        orange_fill = PatternFill(start_color="FFA500", end_color="FFA500", fill_type="solid") 
        yellow_fill = PatternFill(start_color="FFFF00", end_color="FFFF00", fill_type="solid") 

        # Conditional formatting rules
        # Rule 1: Red for 'HOLE'
        rule_red = CellIsRule(operator="equal", formula=['"HOLE"'], fill=red_fill)
        sheet.conditional_formatting.add(range_address, rule_red)

        # Rule 2: Green for 'FREE'
        rule_green = CellIsRule(operator="equal", formula=['"FREE"'], fill=green_fill)
        sheet.conditional_formatting.add(range_address, rule_green)

        # Rule 3: Orange for cells containing '|'
        rule_orange = FormulaRule(formula=[f'ISNUMBER(SEARCH("|", {sheet.cell(row=start_row, column=start_col).coordinate}))'], fill=orange_fill)
        sheet.conditional_formatting.add(range_address, rule_orange)

        rule_yellow_default = FormulaRule(formula=[f'NOT(ISBLANK({sheet.cell(row=start_row, column=start_col).coordinate}))'], fill=yellow_fill)
        sheet.conditional_formatting.add(range_address, rule_yellow_default)

    if 'Sheet' in workbook.sheetnames:
        del workbook['Sheet']

    workbook.save('result.xlsx')

def main():
    args = get_args()
    filename = args.filename

    dal = DAL(filename)
    
    term = dal.get_all_weeks()

    result = {}
    students = dal.get_all_students()
    for student in students:
        groups = dal.get_groups_by_student(student)
        groups_hash = groups.get_hash()
        if groups_hash in result:
            continue
        result[groups_hash] = {}
        result[groups_hash]['groups'] = groups
        result[groups_hash]['schedule'] = []
        result[groups_hash]['total_holes'] = 0
        result[groups_hash]['total_overlaps'] = 0
        for week in term:
            schedule = week.get_schedule_of(groups) 
            result[groups_hash]['schedule'].append(schedule)
            for day in schedule.values():
                result[groups_hash]['total_holes'] += day.count('HOLE')
                result[groups_hash]['total_overlaps'] += len(list(filter(lambda x: '|' in x, day)))
    save_result_to_xlsx(result)

if __name__ == '__main__':
    main()
