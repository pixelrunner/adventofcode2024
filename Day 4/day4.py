#!/usr/bin/env python3

DEBUG = False

def searchForM(xLocation, wordSearch, allRound):
    # look around "X" in the following pattern
    #
    # 1 2 3
    # 4 X 5
    # 6 7 8
    #
    # if found then return true and location number (else return false and 0)

    # check if we can go up (is x on top row)
    #

    mLocations = []
    mFound = False

    firstLoc = [xLocation[0]-1,xLocation[1]-1]
    secondLoc = [xLocation[0]-1,xLocation[1]]
    thirdLoc = [xLocation[0]-1,xLocation[1]+1]
    fourthLoc = [xLocation[0],xLocation[1]-1]
    fifthLoc = [xLocation[0],xLocation[1]+1]
    sixthLoc = [xLocation[0]+1,xLocation[1]-1]
    seventhLoc = [xLocation[0]+1,xLocation[1]]
    eighthLoc = [xLocation[0]+1,xLocation[1]+1]

    # go through each of the 8 positions and check for an "M"
    # before checking, check if the position actually exists for each location

    #check 1st loc
    if xLocation[0] != 0:
        if xLocation[1] != 0:
            if wordSearch[firstLoc[0]][firstLoc[1]] == "M":
                mLocations.append([-1,-1])
                mFound = True

    # check 2nd loc (not p2)
    if allRound:
        if xLocation[0] != 0:
            if wordSearch[secondLoc[0]][secondLoc[1]] == "M":
                mLocations.append([-1,0])
                mFound = True

    # check 3rd loc
    if xLocation[0] != 0:
        if xLocation[1] != len(wordSearch[0])-1:
            if wordSearch[thirdLoc[0]][thirdLoc[1]] == "M":
                mLocations.append([-1,1])
                mFound = True

    # check 4th loc (not p2)
    if allRound:
        if xLocation[1] != 0:
            if wordSearch[fourthLoc[0]][fourthLoc[1]] == "M":
                mLocations.append([0,-1])
                mFound = True

    # check 5th loc (not p2)
    if allRound:
        if xLocation[1] != len(wordSearch[0])-1:
            if wordSearch[fifthLoc[0]][fifthLoc[1]] == "M":
                mLocations.append([0,1])
                mFound = True

    # check 6th loc
    if xLocation[0] != len(wordSearch)-1:
        if xLocation[1] != 0:
            if wordSearch[sixthLoc[0]][sixthLoc[1]] == "M":
                mLocations.append([1,-1])
                mFound = True

    # check 7th loc (not p2)
    if allRound:
        if xLocation[0] != len(wordSearch)-1:
            if wordSearch[seventhLoc[0]][seventhLoc[1]] == "M":
                mLocations.append([1,0])
                mFound = True

    # check 8th loc
    if xLocation[0] != len(wordSearch)-1:
        if xLocation[1] != len(wordSearch[0])-1:
            if wordSearch[eighthLoc[0]][eighthLoc[1]] == "M":
                mLocations.append([1,1])
                mFound = True

    # need to return all locations of m
    return mFound, mLocations

def searchForNextLetter(xLocation, mLocation, letter, locationInWord, wordsearch):
    searchPosition=[]
    linePosition = xLocation[0] + (mLocation[0]*locationInWord)
    letterPosition = xLocation[1] + (mLocation[1]*locationInWord)
    searchPosition = [linePosition, letterPosition]

    # check if searchPosition exists
    if 0 <= searchPosition[0] < len(wordsearch):
        if 0 <= searchPosition[1] < len(wordsearch[0]):
            # now look for letter at location
            if wordsearch[searchPosition[0]][searchPosition[1]] == letter:
                return True
def part1(wordsearch):
    foundCounter = 0

    # find all "X"s
    xLocations = []
    linelocation = 0
    for line in wordsearch:
        letterlocation = 0
        for letter in line:
            if letter == "X":
                xLocations.append([linelocation, letterlocation])
            letterlocation += 1
        linelocation += 1

    # go through list of "X"s and look for all "M"'s
    # if finding an "M" then store then look for "A" in the next position
    for xLocation in xLocations:
        mFound, mLocations = searchForM(xLocation, wordsearch, True)
        if mFound:
            for mLocation in mLocations:
                # go through each M and see if an A exists after it
                # location position is where the letter is located with base 0
                if searchForNextLetter(xLocation, mLocation, "A", 2, wordsearch):
                    # if an A exists then search for an S
                    if searchForNextLetter(xLocation, mLocation, "S", 3, wordsearch):
                        foundCounter += 1
    return foundCounter


def searchForOppositeLetter(aLocation, mLocation, letter, wordsearch):
    searchPosition=[]
    linePosition = aLocation[0] + (mLocation[0]*-1)
    letterPosition = aLocation[1] + (mLocation[1]*-1)
    searchPosition = [linePosition, letterPosition]


    # now look for letter at location
    if wordsearch[searchPosition[0]][searchPosition[1]] == letter:
        return True
    return False
def part2(wordsearch):
    foundCounter = 0

    # find all "A"s
    aLocations = []
    linelocation = 0
    for line in wordsearch:
        if linelocation != 0:
            if linelocation != len(wordsearch)-1:
                letterlocation = 0
                for letter in line:
                    if letterlocation != 0:
                        if letterlocation != len(line)-1:
                            if letter == "A":
                                aLocations.append([linelocation, letterlocation])
                    letterlocation += 1
        linelocation += 1

    # go through list of "X"s and look for all "M"'s
    # if finding an "M" then store then look for "A" in the next position
    mLocations = []
    for aLocation in aLocations:
        mFound, mLocations = searchForM(aLocation, wordsearch, False)
        if mFound:
            if len(mLocations) == 2:
                masFound = True
                for mLocation in mLocations:
                    # go through each M and see if an S exists on other side of A
                    # location position is where the letter is located with base 0
                    if searchForOppositeLetter(aLocation, mLocation, "S", wordsearch) == False:
                        masFound = False

                if masFound == True:
                    foundCounter += 1
    return foundCounter


def setup():
    # Open the text file in read mode
    if DEBUG:
        filename = "sampleinput.txt"
    else:
        filename = "input.txt"

    with open(filename, 'r') as file:
        # Read each line in the file and strip any extra whitespace
        lines = file.readlines()

    # Create a nested list, where each line is a list of its characters
    fullWordSearchLists = [[char for char in line.strip()] for line in lines]

    return fullWordSearchLists
def day4():
    wordsearch = setup()

    p1NumberFound = part1(wordsearch)
    print(p1NumberFound)

    p2NumberFound = part2(wordsearch)
    print (p2NumberFound)

if __name__ == '__main__':
    day4()