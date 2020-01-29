####################
# File description #
####################

#Creator: Jon Simonsen
#Version None
#Last official change: 29.01.19

#from darts import Dart

#Variable inititalization
results = []

##Tests that should succeed
results.append(test_dart(0, 0, True))
results.append(test_dart(0, 1, True))
results.append(test_dart(1, 0, True))
results.append(test_dart(1, 1, True))
results.append(test_dart(1, 20, True))
results.append(test_dart(1, 25, True))
results.append(test_dart(1, 50, True))
#could test some random cases in [2,19]
results.append(test_dart(2, 1, True))
results.append(test_dart(2, 20, True))
#could test some random cases in [2,19]
results.append(test_dart(2, 1, True))
results.append(test_dart(2, 20, True))

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
