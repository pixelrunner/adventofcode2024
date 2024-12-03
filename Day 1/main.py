#!/usr/bin/env python3

def readLists(list1, list2):
    # Define the input file path
    file_path = 'input.txt'

    # Read the file and process each line
    with open(file_path, 'r') as file:
        for line in file:
            # Split the line into two numbers
            num1, num2 = line.split()
            # Convert the numbers to integers and add them to the respective lists
            list1.append(int(num1))
            list2.append(int(num2))

    return list1, list2

def part1(list1, list2):
    # Initialize an empty list to store the modulus of the differences
    modulus_differences = []

    # Calculate the modulus of the difference between corresponding elements
    for num1, num2 in zip(list1, list2):
        modulus_differences.append(abs(num1 - num2))

    # Sum all the numbers in the differences list
    return sum(modulus_differences)

def part2(list1, list2):
    similarityScore = 0
    currentNumber = 0
    currentScore = 0

    # loop through list one work out the similarity score
    for item in list1:
        # added this if statement to do less list traversal for known numbers
        if item == currentNumber:
            similarityScore += currentScore
        else:
            currentNumber = item
            currentScore = item * list2.count(item)
            similarityScore += currentScore

    return similarityScore

def day1():
    # Initialize empty lists for the numbers
    list1 = []
    list2 = []

    list1, list2 = readLists(list1,list2)

    # Sort the lists in numerical order
    list1.sort()
    list2.sort()

    # calculate and print part 1
    print(f'Part 1 = {part1(list1, list2)}')
    print(f'Part 2 = {part2(list1, list2)}')


if __name__ == '__main__':
    day1()