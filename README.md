# Dart-stats
The goal is to make a class for Dart scores and an app to keep track of scores.

# Modelling
-One class for single darts, and one class for scores that consists of three darts.

-Darts has an attribute called multiplier or some such that tells if the score was a single, double or treble.  
-Inner and outer bulls are considered to be singles, but maybe there should be some kind of flag to signify that they are not ordinary singles.  
-Hitting the board but scoring 0 is considered a single.  
-Missing the board is signified in a special way, possibly with its own multiplier (0).  
-The user is free to overrule the previous two suggestions. If the user doesn't care about distinguishing between zero point darts, using the 0 multiplier is suggested but only because that makes those scores stand out more.   

-Extra info is an attribute for scores. Example of extra info are date, distance from the center for all darts or saying that all darts hit in the same sector. 
The user decides what info to keep, but it is suggested to omit info that is not of special interest. This is to reduce the management cost, and make it easier to present the scores reasonably well.  
-The scores should be sorted descending by multipier and then descending by 
