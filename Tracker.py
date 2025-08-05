import tkinter as tk
import os
from Classes import Person

def showHelp(window):
    """
    This function simply opens a new window and displays the version number to the user
    """
    helpWindow = tk.Toplevel(window)
    helpLabel = tk.Label(helpWindow, text=f'Tracker version {version}')
    helpLabel.pack()


def createUser(name, cstart):
    """
    this function is to create a new user
    """
    with open(f'{path}\\Documents\\MenstrualTracker\\Users.txt', 'w') as f:
        f.write(name + ":" + cstart + "\n")


buildDate = "8/5/2025"
version = "0.04"

Main = tk.Tk()
Cal_Frame = tk.Frame()
Username_Frame = tk.Frame()

#Build Menu
menubar = tk.Menu(Main)
Main.config(menu=menubar)

#Help Menu
help_menu = tk.Menu(menubar)
menubar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label='version', command=lambda: showHelp(Main))

path = os.path.expanduser('~')
if os.path.exists(f'{path}\\Documents\\MenstrualTracker\\Users.txt'):
    State = 1
else:
    os.mkdir(f'{path}\\Documents\\MenstrualTracker')
    with open(f'{path}\\Documents\\MenstrualTracker\\Users.txt', "w"):
        ...
    State = 0

Main.title('Menstrual Tracker')

if State == 0:
    descriptionLabel = tk.Label(Main, text='Create a new User to track')
    descriptionLabel.grid(row=0, columnspan=2)

    NameLabel = tk.Label(Main, text='Username')
    NameLabel.grid(row=1, column=0)

    name_var = tk.StringVar()
    NameEntry = tk.Entry(Main, textvariable=name_var)
    NameEntry.grid(row=1, column=1)

    cStartLabel = tk.Label(Main, text='Last Cycle Start date')
    cStartLabel.grid(row=2, column=0)

    cstart_var = tk.StringVar()
    cstartEntry = tk.Entry(Main, textvariable=cstart_var)
    cstartEntry.grid(row=2, column=1)

    EntryButton = tk.Button(Main, text='Create', command=lambda: createUser(name_var.get(), cstart_var.get()))
    EntryButton.grid(row=3, columnspan=2)

elif State == 1:
    with open(f'{path}\\Documents\\MenstrualTracker\\Users.txt', 'r') as f:
        temp = f.readlines()
    userTemp = temp[0].split(':')
    Username_Frame.pack()
    Cal_Frame.pack()
    User = Person(userTemp[0], userTemp[1], Cal_Frame)
    userNameLabel = tk.Label(Username_Frame, text=User.name, bg='pink', fg='black', pady=5)
    userNameLabel.pack()
    User.calendar.pack()


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
