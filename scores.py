####################
# File description #
####################

#Creator: Jon Simonsen
#Version None
#Last official change: 30.01.19

SECTORS = range(1, 21)

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

        if not (isinstance(multiplier, int) and isinstance(points, int)):
            print('When making new Darts, all arguments must be integers.')
            raise TypeError()

        if multiplier < 0 or multiplier > 3:
            print('Multiplier must be between 0 and 3.')
        if multiplier == 0:
            if points != 0:
                print('Zero multiplier can not be combined with non-zero points.\n')
                raise ValueError()

        self._multiplier = multiplier
        self._points = points

    def getMultiplier(self):
        """Getter for multiplier"""
        return self._multiplier

    def getPoints(self):
        """Getter for points"""
        return self._points
