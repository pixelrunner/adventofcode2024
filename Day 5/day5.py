#!/usr/bin/env python3

DEBUG = False

def setupLists():
    if DEBUG != True:
        filePath = "input.txt"
    else:
        filePath = "sampleinput.txt"

    with open(filePath, 'r') as file:
        # Read the entire file and split into lines
        lines = file.readlines()

    # Find the blank line that separates the two sections
    split_index = lines.index('\n')

    # Process the first section
    first_section = lines[:split_index]
    rulesList = []
    for line in first_section:
        nums = line.strip().split('|')
        rulesList.append([int(nums[0]), int(nums[1])])

    # Process the second section
    second_section = lines[split_index + 1:]
    fullPrintList = []
    for line in second_section:
        nums = line.strip().split(',')
        fullPrintList.append([int(num) for num in nums])

    return rulesList, fullPrintList


def buildPageRules(page, rulesList):
    pageRules = [item[1] for item in rulesList if item[0] == page]
    return pageRules

def bubbleSort(currentPrintList, pageRules, page):
    i = 0
    currentPageSorted = False
    itemMoved = False
    # loop through pages in current print run until the current page we are looking at
    # this ensures that the page we are looking at is not after any of the rules in the rule list
    while currentPageSorted == False:
        currentPageSorted = False
        for i in range(len(currentPrintList)):
            if currentPrintList[i] == page:
                currentPageSorted = True
                break  # Stop processing once we reach the stop value
            if currentPrintList[i] in pageRules:
                # Find the index of the stop value
                stop_index = currentPrintList.index(page)
                # If the stop value is not already at the start, move it one place to the left
                if stop_index > 0:
                    currentPrintList[stop_index], currentPrintList[stop_index - 1] = currentPrintList[stop_index - 1], currentPrintList[stop_index]
                    itemMoved = True
                    break
        # if currentPrintList[i] == page:
            # currentPageSorted = True

    return currentPrintList, itemMoved
def sortPrintLists(rulesList, fullPrintList):
    pageRules = []

    # go through each print run in the print list
    printRunPointer = 0
    for i in range(len(fullPrintList)):
        printRun = fullPrintList[i]
        pageListPointer = 0
        # create copy of current list to manipulate
        currentPrintList = printRun.copy()

        # go through each page in list
        while True:
            startAgain = False
            for page in currentPrintList:
                    pageRules = buildPageRules(page, rulesList)
                    currentPrintList, startAgain = bubbleSort(currentPrintList, pageRules, page)
                    if startAgain:
                        break
            if not startAgain:
                break

        # update printrun with currentPrint List
        fullPrintList[i] = currentPrintList

        # print(printRun)
        # print(currentPrintList)

        printRunPointer += 1
    return fullPrintList

def middleValue(sortedList, originalList, partNo):
    total_sum = 0
    for sublist1, sublist2 in zip(sortedList, originalList):
        for i in range(min(len(sublist1), len(sublist2))):
            if partNo == 1:
                if sublist1 == sublist2:
                    # Sum the middle values if the elements are identical
                    total_sum += middle_value(sublist1)
                    break  # Move to the next pair of sublists after summing
            elif partNo == 2:
                if sublist1 != sublist2:
                    # Sum the middle values if the elements are different
                    total_sum += middle_value(sublist1)
                    break  # Move to the next pair of sublists after summing
    return total_sum


def middle_value(lst):
    mid_index = len(lst) // 2
    return lst[mid_index]


def part1(rulesList, fullPrintList):
    originalList = fullPrintList.copy()
    sortedList = sortPrintLists(rulesList, fullPrintList)

    p1MiddleSum = middleValue(sortedList, originalList, 1)
    print(f"Part 1 answer: {p1MiddleSum}")
    return originalList, sortedList

def part2(originalList, sortedList):

    p1MiddleSum = middleValue(sortedList, originalList, 2)
    print(f"Part 2 answer: {p1MiddleSum}")

def day5():
    rulesList, fullPrintList = setupLists()

    originalList, sortedList = part1(rulesList, fullPrintList)

    part2(originalList, sortedList)

if __name__ == '__main__':
    day5()