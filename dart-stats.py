####################
# File description #
####################

#Creator: Jon Simonsen
#Version 0.1
#Last official change: 12.02.20

#Imports
from manager import Manager

#Global constants
FILENAME = 'darts_out.txt'
GREETING = '\nWelcome to Darts-stats, an app to manage dart scores.\n\n'
INFO = "The app will use the file '" + FILENAME + "' in this directory for loading and saving data,\n"
PAGESIZE = 16   #Number of objects to display on a page (when modifying or showing objects)

class DartManager(Manager):
    """A class for managing dart scores."""

    def addObject(self):
        """Class specific helper for the add method that does the actual creation of a new score object."""

        #Ask for the name of the counter
        # prompt = 'Please enter the name of the counter (Max. ' + str(NAME_LEN) + ' characters): '
        # name = input(prompt)
        # while len(name) == 0 or len(name) > NAME_LEN:
        #     name = input('The name must be between 1 and ' + str(NAME_LEN) + ' characters long. Try again: ')
        #
        # #Ask for the count
        # clearTerminal()
        # count = getPosInt('The count', 10**COUNT_LEN - 1)
        #
        # #Create the counter
        # counter = UnitCounter(name, int(count))

        return None

    def changeObject(self):
        """Class specific helper for the modify method that creates a new object based on an existing object."""

        # counter = counterList[index].makeCopy()
        # print('Choose a new value for the count.\n')
        # count = getPosInt('The count', 10**COUNT_LEN - 1)
        # counter.setCount(count)
        # return (counter, index)
        return None
