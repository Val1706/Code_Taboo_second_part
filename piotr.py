def mentor_choice():
    while True:
        try:
            mentor = int(provide_mentor())
            if 0 < mentor < 6:
                return mentor
        except (ValueError, TypeError):
            pass


def get_mentor():
    print_mentor_list()
    mentor = mentor_choice()

    if mentor == 1:
        mentor == mentors[1]
    elif mentor == 2:
        mentor == mentors[2]
    elif mentor == 3:
        mentor == mentors[3]
    elif mentor == 4:
        mentor == mentors[3]
    elif mentor == 5:
        mentor == mentors[3]
    elif mentor == 0:
        mentor == "0"

    return mentor