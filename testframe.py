####################
# File description #
####################

#Creator: Jon Simonsen
#Version 0.03
#Last official change: 08.02.20
#Utility function for tests

def printTests(results):
    """Prints a summary of the test results.
    results should be a list containing one True for each successful test and one False for each failed test.
    Returns nothing.
    """
    successes = fails = 0

    for test in results:
        if test == True:
            successes += 1
        else:
            fails += 1

    print('\n' + str(successes) + ' tests gave the expected result.')
    print(str(fails) + ' tests did not give the expected result.')
    print(str(len(results)) + ' cases were tested.\n')
    
