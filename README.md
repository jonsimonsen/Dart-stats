# Dart-stats
The goal is to make a class for Dart scores and an app to keep track of scores.

# Modelling classes
-One class for single darts, and one class for scores that consists of three darts.

-Darts has an attribute called multiplier that tells if the score was a miss, single, double or treble.  
-Inner and outer bulls are considered to be singles.  
-Hitting the board but scoring zero is considered a single.  
-Missing the board is signified by having a zero multiplier (as well as zero points).  
-The user is free to overrule the previous two suggestions. If the user doesn't care about distinguishing between zero point darts, using the zero multiplier is suggested but only because that makes those scores stand out more.  
-An attribute should keep track of the base score before considering the multiplier. It will be called points.  

-Extra info is an attribute for scores. Examples of extra info are date, distance from the center for all darts or saying that all darts hit in the same sector.
The user decides what info to keep, but it is suggested to omit info that is not of special interest. This is to reduce the management cost, and make it easier to present the scores reasonably well.  
-The scores should contain a list of its darts. The darts should be sorted descending by multipier and then descending by points.  
-The scores should have a representation that is suitable for printing to terminal and writing to/reading from files.  
-Methods and functions for file write and read operations should be included.

# Dart management application
-An application to manage scores. It is suggested to use the countem repo for inspiration and to reuse code.  

# Testing
-test_darts.py contains test cases for darts attributes.  
-test_scores contains test cases with list of darts for a score (to verify that the list is sorted correctly). It also tests file write and read for scores and that the string conversion looks as expected.

# History

# Version 0.1
-The Dart and Scores class are more or less finished. All the suggestions for modelling classes have been implemented.  
-Scores now inherits from the newly created class Saveable. The class defines methods for setting and getting and info attribute and for writing a representation of itself to file. This utility class will probably be used in other projects.  
-Writing to file and reading from file has been implemented.  
-Could consider refactoring file read to use less magic numbers and put some of it into the Saveable class.  
-Some basic testing of file writing and reading has been added to the test file for scores.

# Version 0.05
-The Score init function is finished for now. It sorts its darts in descending order.  
-Implemented a lt function for Darts.

# Version 0.04
-All tests of darts gives the expected result.  
-Made tests to confirm that scores sort their darts correctly.  
-Refactored code into a score summary function named printTests.  
-Made an equality function for darts, and started making a less than function.  
-Made a Score class with an init function without type checking or sorting.  
-Made a getter for darts in the Score class. It takes the index of the dart as a parameter.

# Version 0.02
-The tests were altered to confirm that wrong input gives None as attributes.  
-A str method for darts was implemented and used in the tests.  

# Version 0.01
-Made tests to verify that valid input produces darts with correct attributes.  
-Made tests to verify that incorrect input produces darts with incorrect attributes.  
-Made a class for darts with an init method and getters for its attributes.  
-The class has a helper for the init method that verifies that its arguments are valid. Otherwise, init will print an error message and set all attributes to None.  
-So far, it seems like the class will be made immutable (no setters).  

# TODO

-Consider doing cleanup of code and documentation for version 0.1.  
-Consider adding a print method to the scores class.  
-Making copies of the darts before adding them to a score should be considered. This is especially true if the darts class is changed to be mutable.  
-Plan how to approach the design of the management app.
