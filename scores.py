####################
# File description #
####################

#Creator: Jon Simonsen
#Version 0.1
#Last official change: 09.02.20

#Imports
from saveable import Saveable

#Global consts
MULTS = ['Miss - ', 'Single ', 'Double ', 'Treble ']    #Must have equal length for parsing to work

class Dart(object):
    """A class for darts that have been thrown at a dart board."""

    def __init__(self, multiplier, points):
        """Create a dart with the given multiplier and points.
        multiplier should be an integer telling if the score was a single, double or treble.
        points should be the points that gets multiplied to reach the score of the dart.
        Inner and outer bulls are considered singles.
        Zero point darts can be single zeros or a zero with a zero multiplier.
        Zero point darts that hit the board are suggested as single zeros.
        """

        try:
            self.validateArgs(multiplier, points)
        except (TypeError, ValueError) as error:    #Execute on TypeError or ValueError
            print(error)
            self._multiplier = None
            self._points = None
        else:
            self._multiplier = multiplier
            self._points = points

    def __eq__(self, other):
        """Compares the dart to another dart.
        Returns True if _multiplier and _points are the same for both darts.
        Returns False otherwise.
        """
        if not isinstance(other, Dart):
            return False

        if (self._multiplier == other._multiplier) and (self._points == other._points):
            return True
        else:
            return False

    def __lt__(self, other):
        """Compares the dart to another dart.
        Returns True if _multiplier is less for self or if the multipliers are equal and _points is less for self.
        Returns False otherwise.
        """
        if not isinstance(other, Dart):
            return False

        if self._multiplier < other._multiplier or (self._multiplier == other._multiplier and self._points < other._points):
            return True
        else:
            return False

    def __str__(self):
        """Returns a string representing the dart"""
        if self._multiplier == None:
            return 'Invalid dart'

        prefix = ''
        return MULTS[self._multiplier] + '{:>2}'.format(self._points)

    def getMultiplier(self):
        """Getter for multiplier"""
        return self._multiplier

    def getPoints(self):
        """Getter for points"""
        return self._points

    def getScore(self):
        """Getter for the total score"""
        return self._multiplier * self._points

    def validateArgs(self, multiplier, points):
        """Helper for the init method to validate the input or throw an exception"""

        #Const inititalization
        SECTORS = range(1, 21)
        UNSECTORED = [0, 25, 50]

        if not (isinstance(multiplier, int) and isinstance(points, int)):
            raise TypeError('When making new Darts, all arguments must be integers.')
            return

        if multiplier < 0 or multiplier > 3:
            raise ValueError('Multiplier must be between 0 and 3.')
        elif multiplier > 1 and (points not in SECTORS):
            raise ValueError('Doubles or triples must be an integer between 1 and 20.')
        elif multiplier == 1 and not (points in SECTORS or points in UNSECTORED):
            raise ValueError('Singles must be an integer between 0 and 20 or a bull (25 or 50)')
        elif multiplier == 0 and points != 0:
            raise ValueError('Zero multiplier can not be combined with non-zero points.')

        return

class Score(Saveable):
    """A class for scores consisting of three Dart objects."""

    def __init__(self, dart1, dart2, dart3):
        """Create a new Score consisting of three darts."""
        #v0.05 - no copying
        self._info = ''
        self._total = 0
        if not (isinstance(dart1, Dart) and isinstance(dart2, Dart) and isinstance(dart3, Dart)):
            print('Invalid argument to Score initializer. All darts will be initialized as None.')
            self._darts = [None, None, None]
        else:
            darts = [dart1, dart2, dart3]
            self._darts = self.sortDarts(darts)
            for dart in self._darts:
                self._total += dart.getScore()

    def __str__(self):
        """Return a string representation of the score."""
        if self.getDart(0) is None:
            return "Undefined score."

        darts = []
        for dart in self._darts:
            darts.append(str(dart))

        return '[ ' + ', '.join(darts) + ' ] Score: {:>3}'.format(self._total)

    def __repr__(self):
        """Return a string representation of the score including info."""

        return str(self) + " - " + self._info

    def getDart(self, index):
        """Getter for the dart at the given index in _darts.
        Prints a message and returns None if an incorrect index is given.
        """
        if not index in [0, 1, 2]:
            print('Incorrect index given for a dart. None is returned.')
            return None
        else:
            return self._darts[index]

    def getTotal(self):
        """Getter for _total"""
        return self._total

    def sortDarts(self, darts):
        """Helper for init that sorts darts descending.
        darts should be a list containing the three darts for the score.
        returns the sorted list.
        """

        return sorted(darts, reverse=True)

#Function that creates scores instances from a file
def readScores(handle):
    """Read all Scores from the file that handle references and return a list of these scores."""

    #Initialize variables
    result = []
    darts = None
    newScore = None
    scores = handle.readlines()
    mul = 0
    mulLen = len(MULTS[0])
    points = 0

    #Parse the read file and make new scores
    for s in scores:
        start = 2
        darts = []

        for num in range(3):
            mul = MULTS.index(s[start:start + mulLen])
            start = start + mulLen
            points = int(s[start:start + 2])
            darts.append(Dart(mul, points))
            start += 4

        start += 14
        newScore = Score(darts[0], darts[1], darts[2])
        if len(s) > start:
            newScore.setInfo(s[start:len(s)])
        result.append(newScore)

    return result
