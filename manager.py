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
        self._collection = []

        self._options = self.makeOptions()
        self._menu = self.makeMenu()

        #Greet the user
        clearTerminal()
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
        """Makes a menu displaying the options the user can choose from.

        Additionally, the method alter self._options to remove the part that is only relevant for the menu.

        Returns the menu.
        """
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

    def browsePages(modifying = False):
        """Uses PAGESIZE to display the objects in self._collection on several pages.

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
        endStr = "'n' to see the next page of " + self._plural + " or 'q' to get back to the main menu.\n"

        #Populate options and promptStr
        if modifying:
            #Add all indices to the options and specify to the user that modification is possible
            options = list(range(len(self._collection)))
            options = [str(i) for i in options]
            promptStr = '\nEnter the index of the ' + self._singular + ' to modify. Alternatively, enter ' + endStr
        else:
            promptStr = '\nEnter ' + endStr
        options.append('q')
        options.append('n')

        #Loop through the list until the user chooses an index or to quit
        while choice == 'n':
            for i in range(1 + (len(self._collection) - 1) // PAGESIZE):
                clearTerminal()
                print('\nList of ' + self._plural +', page ' + str(i + 1) + ':\n')
                for j in range(PAGESIZE):
                    current = PAGESIZE * i + j
                    if current < len(self._collection):
                        print(str(current) + ': ', end='')  #Do not print a newline yet
                        #self._collection[current].printCounter()
                        print(self._collection[current])
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

    def run(self):
        """Manage objects until the user decides to exit."""
        while self._running:
            self.showMenu()
            choice = getPosInt('your choice', len(self._options))

            self.chooseAction(choice)

    def exit(self):
        clearTerminal()
        quitting = True
        if self._modified:
            print('You have made unsaved changes to the ' + self._plural + '. Are you sure you want to exit without saving?\n')
            quitting = getConfirmation()

        if quitting:
            self._running = False
            print('Have a nice day.\n')

    def load(self):
        reading = True
        clearTerminal()
        if self._modified and len(self._collection) > 0:
            print('Loading from file will overwrite all current ' + self._plural + '. Are you sure you want to do this?\n')
            reading = getConfirmation() #Do not proceed if the user doesn't confirm

        if reading:
            #Try to read from file. Inform the user if the file was not found.
            try:
                print('File read function has to be defined.')
                # file = open(FILENAME, 'r')
                # self._collection = readCounters(file)
                # file.close()
                # print('Data was read from file.\n')
                # self._modified = False
            except FileNotFoundError:
                print('There is no file that can be loaded. No changes were made.\n')
        else:
            print('No data was read.\n')

    def show(self):
        if len(self._collection) == 0:
            clearTerminal()
            print('No ' + self._plural + ' have been added yet.\n')
        else:
            browsePages(self._collection)

    def add(self):
        obj = self.addObject()

        #Display the counter and ask if it should be added
        clearTerminal()
        print('Here is your ' + self._singular + ':\n')
        #counter.printCounter()
        print(obj)
        print('\nDo you want to add it to your list of ' + self._plural + '?\n')

        if getConfirmation():
            self._collection.append(obj)
            self._modified = True
            print('The ' + self._singular + ' has been added.\n')
        else:
            print('No ' + self._singular + ' was added.\n')

    def modify(self):
        print('Modifying')

    def save(self):
        clearTerminal()
        if len(self._collection) == 0:
            print('There are no ' + self._plural + ' to save.\n')
        else:
            print("'Saving will overwrite all content in '" + FILENAME + "'. Are you sure?\n")
            if getConfirmation():
                file = open(FILENAME, 'w')
                for obj in self._collection:
                    obj.writeToFile(file)
                file.close()
                self._modified = False
                print('Data saved.\n')
            else:
                print('Save aborted.\n')

    def reprompt(self):
        """Prepare to display the menu and prompt the user again.

        The method should never get called if using a correctly implemented getPosInt() call with valid parameters to prompt the user.
        """
        clearTerminal()
        print('You entered an invalid option. Try again.\n')

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

man = Manager('testClass', 'testClasses')
man.run()
