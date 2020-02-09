####################
# File description #
####################

#Creator: Jon Simonsen
#Version 1.0
#Last official change: 09.02.20

class Saveable(object):
    """An adt class for objects that can be saved to a file.
    All children should include an __init__ method that initializes self._info.
    All children should include a __repr__ method.
    """

    def __init__(self):
        """Default initialization of the ADT.
        Raises an error because all children should have their own init method.
        """

        raise NotImplementedError("Please don't try to initialize an object of the 'Saveable' ADT.")

    def __repr__(self):
        """Default representation of the ADT.
        Raises an error because all children should have their own repr method.
        """

        raise NotImplementedError("Please don't try to represent an object using the repr method of the 'Saveable' ADT.")

    def setInfo(self, val):
        """Setter for _info"""
        self._info = val

    def getInfo(self):
        """Getter for _info"""
        return self._info

    def writeToFile(self, handle):
        """Write the representation of this counter to the file connected to handle. Assumes that the file is in 'w' or 'a' mode."""
        handle.write(repr(self) + '\n')
