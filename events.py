import csv
from datetime import date



class Event:
    """
    Abstract class representing events

    Attributes:
        events (list of :obj: `Events`): list of all Events objects
    """

    events = []

    def __init__(self, date):
        '''
        Construct Event object

        Args:
            date (:obj: `date`): date of event
        '''

        self.date = date

    def get_date(self):
        """
        Return date of event
        """

        return self.date

    @classmethod
    def sort_events(cls):
        if len(cls.events) > 1:
            cls.events.sort(key=lambda event: event.date)

    @classmethod
    def add_event(cls, event):
        """
        Add event to events list and call function to rot that list

        Args:
            event (:obj: `Event`): some event
        """

        cls.events.append(event)
        cls.sort_events()

    @classmethod
    def get_events(cls):
        """
        Return list of events
        """

        return cls.events

    @classmethod
    def del_event(cls, date):
        """
        Remove Event object form events list
        """

        for event in cls.events:
            if event.date == date and event.__class__.__name__ == cls.__name__:
                Event.events.remove(event)

    @classmethod
    def change_date(cls, date, new_date):
        """
        Change event date
        """

        for event in cls.events:
            if event.date == date and event.__class__.__name__ == cls.__name__:
                event.date = new_date

    @staticmethod
    def save_events(file_name="events.csv"):

        with open(file_name, "w", newline="") as csvfile:
            saver = csv.writer(csvfile, delimiter="|")

            for event in __class__.events:

                if event.__class__.__name__ == PrivateMentoring.__name__:

                    saver.writerow([event.__class__.__name__,
                                    str(event.date),
                                    event.preffered_mentor,
                                    event.goal])

                elif event.__class__.__name__ == Checkpoint.__name__:

                    saver.writerow([event.__class__.__name__, str(event.date)])


class Checkpoint(Event):
    """
    Class representing checkpoint events

    Attributes:
        events (list of :obj: `Events`): list of all Events objects
    """

    def __init__(self, date):
        """
        Construct Checkpoint object

        Args:
            date (:obj: `date`): date of checkpoint
        """

        super().__init__(date)
        Event.add_event(self)

    def __str__(self):
        """
        Return information about checkpoint date as formatted string
        """

        return '{} Checkpoint'.format(self.date)

    @classmethod
    def read_events(cls,file_name="events.csv"):

        with open(file_name, 'r') as f:
            reader = csv.reader(f, delimiter='|')

            for line in reader:
                if line[0] == cls.__name__:
                    date = line[1]
                    cls(date)


class PrivateMentoring(Event):
    """
    Class representing private mentoring events

    Attributes:
        events (list of :obj: `Events`): list of all Events objects
    """

    def __init__(self, date, goal=None, preffered_mentor=None):
        """
        Construct PrivateMentoring object

        Args:
            date (:obj: `date`): date of checkpoint
            goal (string): gaol of private mentoring
            preffered_mentor (string): preffered mentor to private mentoring sesion
        """

        super().__init__(date)
        self.preffered_mentor = preffered_mentor
        self.goal = goal


        Event.add_event(self)

    def __str__(self):
        """
        Return information about private mentoring as formatted string
        """

        return '{} Private mentoring with {} about {}'.format(self.date,
                                                              self.preffered_mentor,
                                                              self.goal
                                                              )

    @classmethod
    def read_events(cls,file_name="events.csv"):

        with open(file_name, 'r') as f:
            reader = csv.reader(f, delimiter='|')
            try:
                for line in reader:
                    if line[0] == cls.__name__:
                        date = line[1]
                        goal = line[3]
                        mentor = line[2]
                        cls(date, goal, mentor)
            except:
                pass


