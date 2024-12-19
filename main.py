from argparse import ArgumentParser
import logic
import dal

def init_arg_parser():
    parser = ArgumentParser(prog='holefinder', description='CLI program to find the holes in the schedule') 

    parser.add_argument('filename', help='.xlsx file with the schedule information')
    parser.add_argument('student_email', help='Student email to be checked')
    parser.add_argument('week', type=int, help='Week number to be checked')

    return parser

def get_args():
    parser = init_arg_parser()
    return parser.parse_args()

def main():
    args = get_args()
    holes = logic.check_holes(args)
    print(holes)

if __name__ == '__main__':
    main()
