####################
# File description #
####################

#Creator: Jon Simonsen
#Version 0.1
#Last official change: 09.02.20

#Contains a menu-driven environment for managing objects.
#This includes adding, modifying, displaying, saving and loading instances.

#Imports
import os

#Global constants
FILENAME = 'get_out.txt'
GREETING = '\nWelcome. This is a greeting for the base Manager class, and should be overridden for real classes.\n\n'
INFO = "This Manager will use the file '" + FILENAME + "' in this directory for loading and saving data,\nbut this info and the file name should be overridden for real Manager classes.\n"
PAGESIZE = 16   #Number of objects to display on a page (when modifying or showing objects)

###########
# Methods #
###########

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

def getPosInt(valName, maxVal):
    """Prompt the user for an integer until a non-negative integer that is not higher than maxVal is entered. Returns that integer."""
    #Initial prompt
    prompt = 'Enter ' + valName.lower() + ' (Max. ' + str(maxVal) + '): '
    num = -1

    #Loop until valid input is given
    while True:
        count = input(prompt)
        #Try to convert to an int. Change the prompt for the next iteration (if any)
        try:
            num = int(count)
            if num < 0:
                prompt = valName + ' must be a positive integer or zero. Try again: '
            elif num > maxVal:
                prompt = valName + ' must be ' + str(maxVal) + ' or less. Try again: '
            else:
                break
        except ValueError:
            prompt = valName + ' must be an integer. Try again: '

    return num

class Manager(object):
    """Manager for objects of the Saveable class"""

    def __init__(self, singular, plural):
        """Create a new manager"""
        self._running = True
        self._modified = False
        self._singular = singular
        self._plural = plural

        self._options = self.makeOptions()
        self._menu = self.makeMenu()
        self.greet()

    def makeOptions(self):
        """Creates a list of options for a menu and returns it."""

        options = [
            'Exit\n',
            'Load ' + self._plural + ' from file',
            'Show all ' + self._plural,
            'Add a new ' + self._singular,
            'Modify an existing ' + self._singular,
            'Save all ' + self._plural
        ]

        return options

    def makeMenu(self):
        """Makes a menu displaying the options the user can choose from."""
        menu = [
            'Please choose what to do next (enter the digit corresponding to your choice):',
            '------------------------------']
        for num, opt in enumerate(self._options[1:], 1):
            menu.append(str(num) + ': ' + opt)
        menu.append('0: ' + self._options[0])

        #Options does not need to keep track of more than the first word anymore
        for num, opt in enumerate(self._options):
            self._options[num] = opt.split()[0].lower()

        return menu

    def showMenu(self):
        """Displays the menu in the terminal."""
        [print(line) for line in self._menu]

    def greet(self):
        """Displays a greeting and additional info.

        GREETING must be defined as a global constant.
        INFO must be defined as a global constant.
        """
        #Should probably be defined as an ADT method to be defined in children
        print(GREETING + INFO)

    def chooseAction(self, choice):
        """Choose the action corresponding to choice.

        choice should be the index of an option in self._options.
        If this is the case, it calls the class method with the same name as that option.
        If not, it calls self.reprompt().
        """

        option = 'undefinedMethod'
        try:
            option = self._options[choice]
        except Exception:
            pass

        #https://www.pydanny.com/why-doesnt-python-have-switch-case.html
        method = getattr(self, option, 'invalid')
        if method == 'invalid':
            method = getattr(self, 'reprompt')
        return method()

    def run(self):
        while self._running:
            self.showMenu()
            choice = getPosInt('your choice', len(self._options) - 1)

            self.chooseAction(choice)

    def exit(self):
        clearTerminal()
        quitting = True
        if self._modified:
            print('You have made unsaved changes to the counters. Are you sure you want to exit without saving?\n')
            quitting = getConfirmation()

        if quitting:
            self._running = False
            print('Have a nice day.\n')

    def load(self):
        print('Loading')

    def show(self):
        print('Showing')

    def add(self):
        print('Adding')

    def modify(self):
        print('Modifying')

    def save(self):
        print('Saving')

    def reprompt(self):
        print('Reprompting')


def browsePages(counterList, modifying = False):
    """Uses PAGESIZE to display the counters in counterList on several pages.
    Lets the user navigate to the next page until an escape character or an item selection is made.
    If modifying is False, the user will not be able to select items.
    Clears terminal before returning.
    Returns the final input from the user.
    """

    #Variable initialization
    choice = 'n'
    current = 0
    options = []    #Holds all strings that are considered valid input
    promptStr = None
    endStr = "'n' to see the next page of counters or 'q' to get back to the main menu.\n"

    #Populate options and promptStr
    if modifying:
        #Add all indices to the options and specify to the user that modification is possible
        options = list(range(len(counterList)))
        options = [str(i) for i in options]
        promptStr = "\nEnter the index of the counter to modify. Alternatively, enter " + endStr
    else:
        promptStr = "\nEnter " + endStr
    options.append('q')
    options.append('n')

    #Loop through the list until the user chooses an index or to quit
    while choice == 'n':
        for i in range(1 + (len(counterList) - 1) // PAGESIZE):
            clearTerminal()
            print('\nList of counters, page ' + str(i + 1) + ':\n')
            for j in range(PAGESIZE):
                current = PAGESIZE * i + j
                if current < len(counterList):
                    print(str(current) + ': ', end='')  #Do not print a newline yet
                    counterList[current].printCounter()
                else:
                    break

            #Give info and "force" the user to enter valid input
            print(promptStr)
            choice = ''
            while not choice in options:
                choice = input('Choice: ')

            if choice == 'n':
                continue    #Go to next page (loops around if currently on last page)
            else:
                break   #Since the while loop terminates when choice != 'n', this should break out of both loops.

    clearTerminal()
    return choice

def addCounter():
    """Prompts the user for input to create a new counter and asks if it should be added.
    Clears the terminal before returning.
    Returns the counter if the user says yes and None otherwise.
    """
    #Ask for the name of the counter
    clearTerminal()
    prompt = 'Please enter the name of the counter (Max. ' + str(NAME_LEN) + ' characters): '
    name = input(prompt)
    while len(name) == 0 or len(name) > NAME_LEN:
        name = input('The name must be between 1 and ' + str(NAME_LEN) + ' characters long. Try again: ')

    #Ask for the count
    clearTerminal()
    count = getPosInt('The count', 10**COUNT_LEN - 1)

    #Create the counter
    counter = UnitCounter(name, int(count))

    #Add info if the user wishes
    clearTerminal()
    info = input('Type any additional info and press enter (press enter directly if there is no additional info): ')
    if len(info):
        counter.setInfo(info)

    #Display the counter and ask if it should be added
    clearTerminal()
    print('Here is your counter:\n')
    counter.printCounter()
    print('\nDo you want to add it to your list of counters?\n')

    if getConfirmation():
        return counter
    else:
        return None

def changeCounter(counterList):
    """Function for creating a new counter based on an existing one and returning the new one along with a reference to the old one.
    counterList is a list of UnitCounters.
    The function prompts the user for what counter is to be replaced and then how to change it.
    Clears the terminal before returning.
    Returns a tuple consisting of the new counter and the index of the one to be replaced.
    The new counter will be returned as None if the user chose to delete a counter.
    Returns None if the user decided to not change anything after all. Also prints some status info after clearing the terminal when returning None.
    """
    clearTerminal()
    #If no counters were provided, there's nothing to change
    if len(counterList) == 0:
        print('There are no counters to modify.\n')
        return None

    #Print information to the user
    print('You will now be presented with a list of the counters you can modify.\n'
    'Each will be preceded by its index.\n')
    input('Press enter to continue: ')

    choice = browsePages(counterList, True)

    if choice == 'q':
        print('Nothing was changed.\n')
        return None
    else:
        index = int(choice)
        print('You can now modify the following counter:\n')
        counterList[index].printCounter()
        print('\nDo you want to delete it?\n')

        if getConfirmation():
            return (None, index)
        else:
            counter = counterList[index].makeCopy()
            print('Choose a new value for the count.\n')
            count = getPosInt('The count', 10**COUNT_LEN - 1)
            counter.setCount(count)
            info = input('Choose new value for info: ')
            counter.setInfo(info)
            clearTerminal()
            return (counter, index)

##########################
# Main (executable code) #
##########################

#Variable initialization
# running = True
# counters = []
# file = None
# prompt = ''
# print(GREETING + INFO)
# modified = False    #True if counters have been added since last load, false otherwise.
#
# clearTerminal()

#Main loop
# while running:
#     makeMenu()
#     res = input('Enter the digit corresponding to your choice: ')
#     if res == '1':
#         reading = True
#         clearTerminal()
#         if modified and len(counters) > 0:
#             print('Loading from file will overwrite all current counters. Are you sure you want to do this?\n')
#             reading = getConfirmation() #Do not proceed if the user doesn't confirm
#
#         if reading:
#             #Try to read from file. Inform the user if the file was not found.
#             try:
#                 file = open(FILENAME, 'r')
#                 counters = readCounters(file)
#                 file.close()
#                 print('Data was read from file.\n')
#                 modified = False
#             except FileNotFoundError:
#                 print('There is no file that can be loaded. No changes were made.\n')
#         else:
#             print('No data was read.\n')
#     elif res == '2':
#         if len(counters) == 0:
#             clearTerminal()
#             print('No counters have been added yet.\n')
#         else:
#             browsePages(counters)
#     elif res == '3':
#         counter = addCounter()
#         if counter is None:
#             print('No counter was added.\n')
#         else:
#             counters.append(counter)
#             modified = True
#             print('The counter has been added.\n')
#     elif res == '4':
#         counterTup = changeCounter(counters)
#
#         if counterTup is None:
#             continue
#
#         counter = counterTup[0]
#
#         #Display the old and new counter and ask if the changes are ok
#         print('The original counter was:\n')
#         counters[counterTup[1]].printCounter()
#
#         if counter is None:
#             print('\nAre you sure you want to delete it?\n')
#             if getConfirmation():
#                 counters.pop(counterTup[1])
#                 print('The counter has been deleted.\n')
#                 modified = True
#             else:
#                 print('No changes were made.\n')
#         else:
#             print('\nHere is your new counter:\n')
#             counter.printCounter()
#             print('\nDo you want to keep these changes?\n')
#
#             if getConfirmation():
#                 counters[counterTup[1]] = counter
#                 print('The counter was updated.\n')
#                 modified = True
#             else:
#                 print('Modification aborted. No changes were made.\n')
#     elif res == '5':
#         clearTerminal()
#         if len(counters) == 0:
#             print("There are no counters to save.\n")
#         else:
#             print("Saving will overwrite all content in '" + FILENAME + "'. Are you sure?\n")
#             if getConfirmation():
#                 file = open(FILENAME, 'w')
#                 for counter in counters:
#                     counter.writeToFile(file)
#                 file.close()
#                 modified = False
#                 print('Data saved.\n')
#             else:
#                 print('Save aborted.\n')
#     elif res == '6':
#         clearTerminal()
#         quitting = True
#         if modified:
#             print('You have made unsaved changes to the counters. Are you sure you want to exit without saving?\n')
#             quitting = getConfirmation()
#
#         if quitting:
#             running = False
#             print('Have a nice day.\n')
#     else:
#         clearTerminal()
#         print('You entered an invalid option. Try again.\n')

man = Manager('testClass', 'testClasses')
man.run()
