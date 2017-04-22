# --------------------------------------------------------------------------- #
# Write a program that prints out the numbers 1 to 100 (inclusive). If the
# number is divisible by 3, print Crackle instead of the number. If it's
# divisible by 5, print Pop. If it's divisible by both 3 and 5, print CracklePop.
# NOTE: You can use any language.
# --------------------------------------------------------------------------- #

import sys

# I am using an object-oriented approach in Python 3. TODO....Notes...

class CracklePop:

    # This list holds the terms of our sequence
    mySequence = []

    # This dictionary holds the words we should replace numbers with,
    # if they are divisible by the key value.
    myDictionary = {
        3 : 'Crackle',
        5 : 'Pop'
    }

    # This method will replace an integer with the terms from the dictionary
    # that it is divisible by *if* there are any terms that evenly divide it.
    # INPUT: myInteger is the int value that we would like to consider.
    # OUTPUT: The correct term for our cracklePop sequence.
    @classmethod
    def findTerm(self, myInteger):

        # This string holds the correct replacement, if there is one.
        myReplacementString = ''
        for myKey in self.myDictionary.keys():
            if myInteger % myKey == 0:
                myReplacementString += self.myDictionary[myKey]

        # Check if the integer should be replaced, otherwise return myInteger.
        if len(myReplacementString) == 0:
            return myInteger
        else:
            return myReplacementString

    # This method fills the mySequence list, using the *inclusive* bounds given
    # by the start and end. Check that they are integers before proceeding.
    @classmethod
    def initializeSequence(self, start, end):
        try:
            startingInt = int(start)
            endingInt = int(end)
        except Exception:
            sys.stderr.write(sys.exc_info()[0])
            sys.exit(1)
        else:
            for myInt in range(startingInt,endingInt+1):
                self.mySequence.append(self.findTerm(myInt))

    # This function will print the contents of self.mySequence
    @classmethod
    def printSequence(self):
        for myTerm in self.mySequence:
            #print(self.findTerm(myTerm))
            print(myTerm)

    # This function runs the cracklePop exercise.
    # NOTE: This function calls the init method itself, you do not have to
    # call init() externally before using this method.
    @classmethod
    def run(self, start, end):
        self.initializeSequence(start,end)
        self.printSequence()
