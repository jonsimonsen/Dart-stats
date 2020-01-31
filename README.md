# Dart-stats
The goal is to make a class for Dart scores and an app to keep track of scores.

# Modelling classes
-One class for single darts, and one class for scores that consists of three darts.

-Darts has an attribute called multiplier or some such that tells if the score was a single, double or treble.  
-Inner and outer bulls are considered to be singles, but maybe there should be some kind of flag to signify that they are not ordinary singles.  
-Hitting the board but scoring 0 is considered a single.  
-Missing the board is signified in a special way, possibly with its own multiplier (0).  
-The user is free to overrule the previous two suggestions. If the user doesn't care about distinguishing between zero point darts, using the 0 multiplier is suggested but only because that makes those scores stand out more.  
-An attribute should keep track of the base score before considering the multiplier. It is suggested that it is called points unless a more descriptive name is found.  

-Extra info is an attribute for scores. Example of extra info are date, distance from the center for all darts or saying that all darts hit in the same sector.
The user decides what info to keep, but it is suggested to omit info that is not of special interest. This is to reduce the management cost, and make it easier to present the scores reasonably well.  
-The scores should contain a list of its darts. The darts should be sorted descending by multipier and then descending by points.  
-The scores should have a representation that is suitable for printing to terminal and writing to/reading from files.  
-Methods and functions for file write and read operations should be included.

# Dart management application
-An application to manage scores. It is suggested to use the countem repo for inspiration and to reuse code.  

# Testing
-Write test cases for darts attributes outside the possible ranges.  
-Write test cases for the list of darts for a score to verify that the list is sorted correctly.  

# History

# Current version
-The tests were altered to confirm that wrong input gives None as attributes.  

# Version 0.01
-Made tests to verify that valid input produces darts with correct attributes.  
-Made tests to verify that incorrect input produces darts with incorrect attributes.  
-Made a class for darts with an init method and getters for its attributes.  
-The class has a helper for the init method that verifies that its arguments are valid. Otherwise, init will print an error message and set all attributes to None.  
-So far, it seems like the class will be made immutable (no setters).  

# TODO
-A repr method and/or str method for darts should be implemented and used in the tests.  
-Write scores test cases.  
-Construct the score class using test-driven development.  
-Plan how to approach the design of the management app.
