####################
# File description #
####################

#Creator: Jon Simonsen
#Version 0.03
#Last official change: 08.02.20

from testframe import printTests
from scores import Dart

def test_dart(mult, points, is_valid):
    """Test if initializing a new dart with mult and points gives the expected result (is_valid).
    Returns True if the expected result is reached and False otherwise."""
    try:
        dart = Dart(mult, points)
    except NameError:
        print('No dart class imported.')
        return False
    except TypeError:
        print(str(mult) + ' or ' + str(points) + ' is not the correct argument type.')
        return False
    else:
        print('<' + str(dart) + '> was created.')

    if dart.getMultiplier() == mult and dart.getPoints() == points:
        return is_valid
    elif dart.getMultiplier() == None and dart.getPoints() == None:
        return not is_valid
    else:
        print('Unexpected dart initialization. Needs closer code examination.')
        return False

#Variable inititalization
results = []

##Tests that should succeed
results.append(test_dart(0, 0, True))
results.append(test_dart(1, 0, True))
results.append(test_dart(1, 1, True))
results.append(test_dart(1, 20, True))
results.append(test_dart(1, 25, True))
results.append(test_dart(1, 50, True))
#could test some random cases in [2,19]
results.append(test_dart(2, 1, True))
results.append(test_dart(2, 20, True))
#could test some random cases in [2,19]
results.append(test_dart(3, 1, True))
results.append(test_dart(3, 20, True))

##Tests that should fail
#Invalid multiplier
results.append(test_dart(-1, 0, False))
results.append(test_dart(-1, 20, False))
results.append(test_dart(-1, 50, False))
results.append(test_dart(4, 0, False))
results.append(test_dart(4, 20, False))
results.append(test_dart(4, 50, False))
results.append(test_dart(1.5, 0, False))
results.append(test_dart(1.5, 20, False))
results.append(test_dart(1.5, 50, False))
results.append(test_dart('1', 0, False))
results.append(test_dart('1', 20, False))
results.append(test_dart('1', 50, False))

#Invalid points
results.append(test_dart(1, -1, False))
results.append(test_dart(1, 21, False))
results.append(test_dart(1, 24, False))
results.append(test_dart(1, 26, False))
results.append(test_dart(1, 49, False))
results.append(test_dart(1, 51, False))

#Invalid combo
results.append(test_dart(0, 1, False))
results.append(test_dart(2, 0, False))
results.append(test_dart(2, 25, False))
results.append(test_dart(2, 50, False))

#Test summary
printTests(results)
