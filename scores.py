####################
# File description #
####################

#Creator: Jon Simonsen
#Version None
#Last official change: 31.01.19

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

    def __str__(self):
        """Returns a string representing the dart"""
        if self._multiplier == None:
            return 'Invalid dart'

        prefix = ''
        mults = ['Miss - ', 'Single ', 'Double ', 'Treble ']
        return mults[self._multiplier] + str(self._points)

    def getMultiplier(self):
        """Getter for multiplier"""
        return self._multiplier

    def getPoints(self):
        """Getter for points"""
        return self._points

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
