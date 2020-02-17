####################
# File description #
####################

#Creator: Jon Simonsen
#Version 1.0
#Last official change: 14.02.20

#Imports
import os

def clearTerminal():
    """Clear the terminal or command window that python is running in.

    Found at https://stackoverflow.com/questions/517970/how-to-clear-the-interpreter-console
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def getConfirmation():
    """Prompts the user for input until 'y' or 'n' has been entered.

    An explanation of what the user can confirm should be given before calling the function.
    Clears the terminal before returning.

    Returns True if 'y' and False if 'n'
    """
    answer = ''

    while answer not in ['y', 'n']:
        answer = input("Press 'y' for yes or 'n' for no and hit enter: ")
    clearTerminal()

    if answer == 'y':
        return True
    else:
        return False

def getPosInt(valName, maxVal = 999999999, inclusive = True):
    """Prompt the user for an integer until a non-negative integer that is not higher than maxVal is entered.

    valName should be a short description of the integer (what it represents) for use in prompting.
    maxVal should be the highest allowed value. It uses a default value if nothing is provided.
    inclusive should be a boolean telling if zero is allowed.

    Returns the first valid integer entered by the user."""
    #Initial prompt
    prompt = 'Enter ' + valName.lower() + ' (Max. ' + str(maxVal) + '): '
    num = -1

    #Loop until valid input is given
    while True:
        count = input(prompt)
        #Try to convert to an int. Change the prompt for the next iteration (if any)
        try:
            num = int(count)
            if num == 0 and not inclusive:
                prompt = valName + ' can not equal zero. Try again: '
            elif num < 0:
                prompt = valName + ' must be a positive integer '
                if inclusive:
                    prompt += 'or zero'
                prompt += '. Try again: '
            elif num > maxVal:
                prompt = valName + ' must be ' + str(maxVal) + ' or less. Try again: '
            else:
                break
        except ValueError:
            prompt = valName + ' must be an integer. Try again: '

    return num
