from dal import DAL

def check_holes(args):
    filename = args.filename
    dal = DAL(filename)

    week_n = args.week
    email = args.student_email

    groups = dal.get_groups_by_email(email)
    week = dal.get_week_by_number(week_n)

    return week.get_holes(groups) 

