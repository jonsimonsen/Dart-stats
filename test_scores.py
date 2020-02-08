####################
# File description #
####################

#Creator: Jon Simonsen
#Version 0.04
#Last official change: 08.02.20

from scores import Dart, Score
from testframe import printTests

def test_score(dart1, dart2, dart3, order):
    """Function for testing a score. Makes a new score for the given darts.
    Tests if they are sorted in the given order.
    order should be a list containing the three integer 1,2 and 3 and nothing else (1 meaning the dart that should be first in the sorted list).
    returns True if the order is correct, and False otherwise.
    """
    score = Score(dart1, dart2, dart3)
    if score.getDart(order[0]) == dart1 and score.getDart(order[1]) == dart2 and score.getDart(order[2]) == dart3:
        return True
    else:
        print('test failed.')
        return False

#Variable initialization
results = []

#Make some darts for testing
gutter = Dart(0, 0)
board = Dart(1, 0)
minHit = Dart(1, 1)
median = Dart(1, 11)
standard = Dart(1, 20)
almost = Dart(1, 25)
unbiased = Dart(1, 50)
barely = Dart(2, 1)
unusual = Dart(2, 11)
finish = Dart(2, 20)
no_cigar = Dart(3, 1)
eyes = Dart(3, 11)
maxHit = Dart(3, 20)

#Presorted
print('Testing sorted darts')
results.append(test_score(gutter, gutter, gutter, [0, 1, 2]))
results.append(test_score(minHit, board, gutter, [0, 1, 2]))
results.append(test_score(unbiased, almost, minHit, [0, 1, 2]))
results.append(test_score(maxHit, eyes, no_cigar, [0, 1, 2]))
results.append(test_score(maxHit, unusual, minHit, [0, 1, 2]))
results.append(test_score(maxHit, finish, standard, [0, 1, 2]))
results.append(test_score(no_cigar, unusual, standard, [0, 1, 2]))

#Reversed
print('Testing reversely sorted darts')
results.append(test_score(gutter, board, minHit, [2, 1, 0]))
results.append(test_score(minHit, almost, unbiased, [2, 1, 0]))
results.append(test_score(no_cigar, eyes, maxHit, [2, 1, 0]))
results.append(test_score(minHit, unusual, maxHit, [2, 1, 0]))
results.append(test_score(standard, finish, maxHit, [2, 1, 0]))
results.append(test_score(standard, unusual, no_cigar, [2, 1, 0]))

#Random order
print('Testing randomly ordered darts')
results.append(test_score(board, gutter, minHit, [1, 2, 0]))
results.append(test_score(minHit, unbiased, almost, [2, 0, 1]))
results.append(test_score(maxHit, no_cigar, eyes, [0, 2, 1]))
results.append(test_score(maxHit, minHit, unusual, [0, 2, 1]))
results.append(test_score(standard, maxHit, finish, [2, 0, 1]))
results.append(test_score(unusual, no_cigar, standard, [1, 0, 2]))

#Print summary
printTests(results)
