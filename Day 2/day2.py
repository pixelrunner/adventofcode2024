#!/usr/bin/env python3

def readInput(list_of_lines):
    # Open the file in read mode
    with open('input.txt', 'r') as file:
        # Read all lines in the file
        lines = file.readlines()

    # Initialize an empty list to store all lists of numbers
    list_of_lines = []

    # Process each line
    for line in lines:
        # Strip the newline character and split by spaces
        numbers = line.strip().split()
        # Convert each number from string to int
        numbers = [int(num) for num in numbers]
        # Append the list of numbers to list_of_lists
        list_of_lines.append(numbers)

    return list_of_lines
def part1(list_of_lines):
    safeCount = 0
    unsafeCount = 0

    for line in list_of_lines:
        # set up increase/decrease indicator
        # -1 = decreasing series
        # 1 = increasing series
        # 0 = initialised var (not calculated any yet)
        increaseDecrease = 0

        # set safe var
        safe = True

        increasingLine = sorted(line)
        decreasingLine = sorted(line, reverse=True)

        if line == increasingLine:
            increaseDecrease = 1
        elif line == decreasingLine:
            increaseDecrease = -1
        else:
            safe = False


        if safe == True:
            # let's work out the differences
            # if all the differences are eq to 1-3 then they are safe

            # x var is the location in the list
            x = 1
            while x < len(line):
                difference = line[x] - line[x-1]
                if (difference * increaseDecrease) < 1 or (difference * increaseDecrease) > 3:
                    safe = False
                    break
                x += 1

        if safe == True:
            safeCount += 1
        else:
            unsafeCount +=1

    return (safeCount, unsafeCount)


def has_duplicates(input_list):
    return len(input_list) != len(set(input_list))

def isIncreasingDecreasing(lineToTest):
    if has_duplicates(lineToTest):
        safe = False
    else:
        # set up increase/decrease indicator
        # -1 = decreasing series
        # 1 = increasing series
        # 0 = initialised var (not calculated any yet)
        increaseDecrease = 0

        # set safe var
        safe = True

        increasingLine = sorted(lineToTest)
        decreasingLine = sorted(lineToTest, reverse=True)


        if lineToTest == increasingLine:
            increaseDecrease = 1
        elif lineToTest == decreasingLine:
            increaseDecrease = -1
        else:
            safe = False

    if safe:
        return increaseDecrease
    return 0



def workOutDifferences(list, maxDifference, increaseDecrease):
    # let's work out the differences
    # if all the differences are eq to 1-3 then they are safe

    # x var is the location in the list
    x = 1
    while x < len(list):
        difference = list[x] - list[x - 1]
        if (difference * increaseDecrease) < 1 or (difference * increaseDecrease) > maxDifference:
            return False
        x += 1
    return True

def findSafeLines(singleLine):
    allIncreasingDecreasingLines = []
    increasingDecreasing = 0

    # first test original line then start popping one at a time
    increasingDecreasingTestResult = isIncreasingDecreasing(singleLine)
    if increasingDecreasingTestResult != 0:
        allIncreasingDecreasingLines.append(singleLine)
        increasingDecreasing = increasingDecreasingTestResult

    for i in range(len(singleLine)):
        # Create a new copy of subInputList for each iteration
        listToPop = singleLine[:]
        # Remove the element at index i
        listToPop.pop(i)
        # test new list
        increasingDecreasingTestResult = isIncreasingDecreasing(listToPop)
        if increasingDecreasingTestResult != 0:
            allIncreasingDecreasingLines.append(listToPop)
            increasingDecreasing = increasingDecreasingTestResult

    # now we have a list of all increasing and decreasing lines in a list
    # test each one until we find a safe item in the list and return safe (else return unsafe)
    for line in allIncreasingDecreasingLines:
        safeLine = workOutDifferences(line, 3, increasingDecreasing)

        if safeLine:
            return True

    return False

def part2(list_of_lines):
    unsafeCount = 0
    safeCount = 0

    for singleLine in list_of_lines:
        if findSafeLines(singleLine):
            safeCount += 1
        else:
            unsafeCount += 1

    return safeCount, unsafeCount

def day2():
    list_of_lines = []
    list_of_lines = readInput(list_of_lines)

    p1SafeCount, p1UnsafeCount = part1(list_of_lines)
    print (f"\r\nPart 1\r\n------\r\nSafe Count: {p1SafeCount} \r\nUnsafe Count: {p1UnsafeCount}\r\n")

    p2SafeCount, p2UnsafeCount = part2(list_of_lines)
    print(f"\r\nPart 2\r\n------\r\nSafe Count: {p2SafeCount} \r\nUnsafe Count: {p2UnsafeCount}\r\n")


if __name__ == '__main__':
    day2()