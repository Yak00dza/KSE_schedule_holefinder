from dal import DAL

def check_holes(args):
    filename = args.filename
    dal = DAL(filename)

    week_n = args.week
    email = args.student_email

    student_groups = dal.get_groups_by_email(email)
    week = dal.get_week_by_number(week_n)

    schedule = week.get_schedule_of(student_groups)
    for day in schedule:
        print(schedule[day])

    return schedule
