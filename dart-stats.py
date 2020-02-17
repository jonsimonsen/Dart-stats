####################
# File description #
####################

#Creator: Jon Simonsen
#Version 0.1
#Last official change: 12.02.20

#Imports
from manager import Manager
from scores import Dart, Score, readScores
from user_io import *

#Global constants
# FILENAME = 'darts_out.txt'
# GREETING = '\nWelcome to Darts-stats, an app to manage dart scores.\n\n'
# INFO = "The app will use the file '" + FILENAME + "' in this directory for loading and saving data,\n"
# PAGESIZE = 16   #Number of objects to display on a page (when modifying or showing objects)

class DartManager(Manager):
    """A class for managing dart scores."""
    _fileName = 'darts_out.txt'
    _greeting = '\nWelcome to Darts-stats, an app to manage dart scores.\n\n'
    _info = "The app will use the file '" + _fileName + "' in this directory for loading and saving data.\n"

    def addObject(self):
        """Class specific helper for the add method that does the actual creation of a new score object."""

        darts = []
        newDart = None

        for i in range(1,4):
            print('Creating dart ' + str(i))
            #Ask for multiplier
            mul = getPosInt('multiplier', 3)
            if mul == 0:
                newDart = Dart(0,0)
            elif mul == 2 or mul == 3:
                #Ask for points
                points = getPosInt('points', 20, False)
                newDart = Dart(mul, points)
            elif mul == 1:
                valid = False
                while not valid:
                    points = getPosInt('points', 50)
                    if points <= 20 or points == 25 or points == 50:
                        valid = True
                newDart = Dart(mul, points)

            darts.append(newDart)
            print('Dart created')

        return Score(darts[0], darts[1], darts[2])

    def changeObject(self, index):
        """Class specific helper for the modify method that creates a new score based on an existing score.

        Returns a tuple containing a copy of the score, since nothing except info can be modified.
        The second tuple item is the index.
        """

        return (self._collection[index].makeCopy(), index)

    def readObjects(self, file):
        """Use the class specific read function to create darts base on reading them from file.

        file should be a handle to the file where darts are stored.
        """

        self._collection = readScores(file)

##########################
# Main (executable code) #
##########################

app = DartManager('Score', 'Scores')
app.run()
