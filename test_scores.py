####################
# File description #
####################

#Creator: Jon Simonsen
#Version None
#Last official change: 07.02.20

#from scores import Dart, Score

def test_score(dart1, dart2, dart3, order):
    """Function for testing a score. Makes a new score for the given darts.
    Tests if they are sorted in the given order.
    order should be a list containing the three integer 1,2 and 3 and nothing else (1 meaning the dart that should be first in the sorted list).
    returns True if the order is correct, and False otherwise.
    """
    score = Score(dart1, dart2, dart3)
    if score.getDart(0) == dart1 and score.getDart(1) == dart2 and score.getDart(2) == dart3:
        return True
    else:
        print('test failed.')
        return False

#Variable initialization
results = []
successes = 0
fails = 0

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
results.append(test_score(gutter, gutter, gutter, [1, 2, 3]))
results.append(test_score(minHit, board, gutter, [1, 2, 3]))
results.append(test_score(unbiased, almost, minHit, [1, 2, 3]))
results.append(test_score(maxHit, eyes, no_cigar, [1, 2, 3]))
results.append(test_score(maxHit, unusual, minHit, [1, 2, 3]))
results.append(test_score(maxHit, finish, standard, [1, 2, 3]))
results.append(test_score(no_cigar, unusual, standard, [1, 2, 3]))

#Reversed
print('Testing reversely sorted darts')
results.append(test_score(gutter, board, minHit, [3, 2, 1]))
results.append(test_score(minHit, almost, unbiased, [3, 2, 1]))
results.append(test_score(no_cigar, eyes, maxHit, [3, 2, 1]))
results.append(test_score(minHit, unusual, maxHit, [3, 2, 1]))
results.append(test_score(standard, finish, maxHit, [3, 2, 1]))
results.append(test_score(standard, unusual, no_cigar, [3, 2, 1]))

#Random order
print('Testing randomly ordered darts')
results.append(test_score(board, gutter, minHit, [2, 3, 1]))
results.append(test_score(minHit, unbiased, almost, [3, 1, 2]))
results.append(test_score(maxHit, no_cigar, eyes, [1, 3, 2]))
results.append(test_score(maxHit, minHit, unusual, [1, 3, 2]))
results.append(test_score(standard, maxHit, finish, [3, 1, 2]))
results.append(test_score(unusual, no_cigar, standard, [2, 1, 3]))

#Should refactor this into a utility function, since it is used in several tests.
for test in results:
    if test == True:
        successes += 1
    else:
        fails += 1

print('\n' + str(successes) + ' tests gave the expected result.')
print(str(fails) + ' tests did not give the expected result.')
print(str(len(results)) + ' cases were tested.\n')
