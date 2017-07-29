from datetime import date
import view
import events


def start():

    events.PrivateMentoring.read_events()
    events.Checkpoint.read_events()



    convert_existing_date(events.Event.get_events())




    """
    Contain main logic of controller,
    call functions to perform task chosen by user
    """

    choice = None

    head = "Chose option:"
    options_list = ["Book private mentoring",
                    "Book checkpoint",
                    "Show all my events",
                    "Cancel event",
                    "Reschedule event"
                    ]
    exit_msg = "Exit program"

    while choice != "0":
        view.print_menu(head, options_list, exit_msg)
        choice = view.get_choice()
        if choice == "1":
            book_private_mentoring()
        elif choice == "2":
            book_checkpoint()
        elif choice == "3":
            display_all_evets()
        elif choice == "4":
            cancel_event()
        elif choice == "5":
            reschedule_event()
        elif choice == "0":
            say_goodbye()
        else:
            view.print_msg("Wrong option!")

        events.Checkpoint.save_events()
        events.PrivateMentoring.save_events()


def display_all_evets():
    """
    Call function to print all Events objects to user
    """

    view.print_all_events(events.Event.get_events())


def book_checkpoint():
    """
    Call functions that allow user create Checkpoint object
    """

    date = view.get_event_date()

    date = validate_date_format(date)

    if date is not None:
        events.Checkpoint(date)


def book_private_mentoring():
    """
    Call functions that allow user create PrivateMentoring object
    """

    date = view.get_event_date()

    date = validate_date_format(date)
    preffered_mentor = choice_preffered_mentor()

    if date is not None and preffered_mentor is not None:
        goal = view.get_goal()

        events.PrivateMentoring(date, goal, preffered_mentor)


def say_goodbye():
    """
    Call function that print goodbye massage to user
    """

    view.print_goodbye()


def convert_date(date_str):
    """
    Convert data from string to date object

    Args:
        date_str: date of event choose by user

    Returns:
        :obj: `date`: date of event choose by user
    """

    date_list = date_str.split('-')
    return date(int(date_list[2]), int(date_list[1]), int(date_list[0]))


def convert_existing_date(array):
    for object in array:
        date_list = object.date.split('-')
        object.date = date(int(date_list[0]), int(date_list[1]), int(date_list[2]))
        return object.date


def cancel_event():
    """
    Call functions to cancel event
    """

    date = view.get_event_date()

    date = validate_date_format(date)

    if date is not None:
        event_name = view.get_event_name().lower()

        if event_name == "checkpoint":
            events.Checkpoint.del_event(date)

        elif event_name == "private mentoring":
            events.PrivateMentoring.del_event(date)

        else:
            view.print_msg("No such event!")


def reschedule_event():
    """
    Call functions to change event date
    """

    view.print_msg("Enter old event date")
    date = view.get_event_date()

    view.print_msg("Enter new event date")
    new_date = view.get_event_date()

    date = validate_date_format(date)
    new_date = validate_date_format(new_date)

    if date is not None and new_date is not None:
        event_name = view.get_event_name().lower()
        if event_name == "checkpoint":
            events.Checkpoint.change_date(date, new_date)

        elif event_name == "private mentoring":
            events.PrivateMentoring.change_date(date, new_date)

        else:
            view.print_msg("No such event!")


def validate_date_format(date_str):
    """
    Validate if givan date is correct

    Args:
        date_str: date of event choose by user

    Returns:
        :obj: `date`: date of event choose by user
    """

    try:
        date = convert_date(date_str)
    except (ValueError, IndexError):
        view.print_msg("Wrong data format!")
    else:
        return date


def validate_date_future(date):
    """
    Validate if givan date is in future

    Args:
        date_str: date of event choose by user

    Returns:
        :obj: `date`: date of event choose by user
    """

    # not call enywhere
    if date <= date.today():
        view.print_msg("Date have to be in future!")
    else:
        return date


def choice_preffered_mentor():
    """
    Call functions to diplay manu and choose preferred mentor
    """

    AVAIALBLE_OPTIONS_LIST = ["0", "1", "2", "3", "4", "5"]

    choice = None
    preffered_mentor = None

    head = "Chose option:"
    options_list = ["Mateusz Ostafi",
                    "Agnieszka Koszany",
                    "Dominik Starzyk",
                    "Mateusz Steliga",
                    "Marcin Izworski"
                    ]
    exit_msg = "Exit booking provate mentoring"

    while choice not in AVAIALBLE_OPTIONS_LIST:
        view.print_menu(head, options_list, exit_msg)
        choice = view.get_choice()
        if choice == "1":
            preffered_mentor = "Mateusz Ostafi"
        elif choice == "2":
            preffered_mentor = "Agnieszka Koszany"
        elif choice == "3":
            preffered_mentor = "Dominik Starzyk"
        elif choice == "4":
            preffered_mentor = "Mateusz Steliga"
        elif choice == "5":
            preffered_mentor = "Marcin Izworski"
        elif choice == "0":
            view.print_msg("End of booking")
        else:
            view.print_msg("Wrong option!")

    return preffered_mentor
