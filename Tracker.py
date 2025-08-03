import tkinter as tk
from Classes import Person

def showHelp(window):
    """
    This function simply opens a new window and displays the version number to the user
    """
    helpWindow = tk.Toplevel(window)
    helpLabel = tk.Label(helpWindow, text=f'Tracker version {version}')
    helpLabel.pack()


buildDate = "8/3/2025"
version = "0.02"

Main = tk.Tk()
Cal_Frame = tk.Frame()

#Build Menu
menubar = tk.Menu(Main)
Main.config(menu=menubar)
#Help Menu
help_menu = tk.Menu(menubar)
menubar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label='version', command=lambda: showHelp(Main))

User = Person("User","8/22/1996", "7/16/2025", Cal_Frame)
User.calendar.pack()

Main.title('Menstrual Tracker')
Cal_Frame.pack()
State = 0

if State == 0:
    ...
elif State == 1:
    ...


tk.mainloop()
"""
NOTES
To calculate your menstrual cycle, count the days from the first day of your period (day one) to the first day of your 
next period. This number represents your cycle length. Most women have cycles between 21 and 35 days, but the average 
is 28 days
"""

"""
the goal here is build a application that will track the menstrual cycle of a number of women. the primary purpose
is to predict when the next menstrual cycle will begin and when the current one will end
"""

"""
Stage 1
have a user selectiong and creation section. this first area is where you can either create a new user to go into
and existing user. no security is needed here
"""

"""
Stage 1b
if its seclected to create a new user, create a new account and add them to the user index
"""

"""
Stage 2
Open the users data and display a card link display to show when the last cycle ended and a prediction of when the 
next cycle will begin
"""

"""
Stage 3
at some point we need to evaluate the cycles and make the predictions of the next cycle
"""
