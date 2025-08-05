import tkcalendar

class Person:
    def __init__(self, name, cstart, Frame):
        self.name = name
        # self.birthday = birthday
        self.Last_Cycle_start = cstart
        self.calendar = tkcalendar.Calendar(Frame)
