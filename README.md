! For internal use in KSE !

# What does this app do?
This app takes an .xlsx file with schedule infornation provided by SSO.
The programm processes the file and outputs a .xlsx file with the vizualization of the schedule of every existing group combination as well some statistics on some of them.
The vizualization highlites the holes and overlaps in the schedule.

# What technologies are used?
Everything is written in python with openpyxl handling interaction with .xlsx


# How to use this program?
Make sure to adjust configs beforehand.
To run the program simply execute the main file and provide the schedule .xlsx as an argument
`python3 main.py schedule.xlsx`

# How to adjust the configs?
To adjust the configs one edits `config.json`. The options there include:

## "schedule_sheet"
This field is for the name of the worksheet with the schedue intself

## "columns_for_monday" and "columns_per_work_day_except_monday"
This two options specify how many collumns one of the week takes in the schedule worksheet.
This has a separate option for Monday for historical reasons and this was kept unchanged because this is kind of funny.

## "groups_sheet_name"
This field is for the name of the worksheet where each student is assigned their groups.

## "columns_for_student_info"
This feild detemines how many first left rows the program will not scan for group names. THe first few columns have student info like names and emails, so it is important to set this correctly to avoid having wrong groups.

## "email_column_name"
This field is for the name of the column with student emails. Emails are used as unique student identifiers, because student names and/or last names can happen to be identical.


# Authors
- Yakiv Baiduk - logic and abstractions on top of .xlsx; Core design
- Anna Prokopchenko - implementation of interactions with the input spreadsheet.
