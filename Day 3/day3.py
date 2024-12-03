#!/usr/bin/env python3

import re

def importInput():
    # Open the file in read mode
    with open('input.txt', 'r') as file:
        # Read all lines in the file
        inputString = file.read()
    return inputString

def multiplyAndSumNumbers(mulList):
    # Define the pattern to match the numbers
    pattern = r"mul\((\d+),(\d+)\)"

    # List to store the results
    results = []

    # Loop through the list, extract the numbers, and multiply them
    for item in mulList:
        match = re.match(pattern, item)
        if match:
            num1 = int(match.group(1))
            num2 = int(match.group(2))
            product = num1 * num2
            results.append(product)
    total = sum(results)

    return total

def part1(inputString):
    # define regex pattern
    pattern = r"mul\(\d+,\d+\)"

    # find all matches
    matches = re.findall(pattern, inputString)

    return multiplyAndSumNumbers(matches)


def part2(inputString):
    # Define the pattern to match "do()", "don't()", and "mul(number,number)"
    pattern = r"(do\(\)|don't\(\)|mul\(\d+,\d+\))"

    # Find all matches
    matches = re.findall(pattern, inputString)

    # List to store the results
    results = []

    # Track if we are in a "do()" section
    in_do_section = True

    # Iterate through the matches
    for match in matches:
        if match == "do()":
            in_do_section = True
        elif match == "don't()":
            in_do_section = False
        elif "mul" in match and in_do_section:
            results.append(match)

    return multiplyAndSumNumbers(results)


def day3():
    inputText = importInput()

    print(f"Part 1: {part1(inputText)}")
    print(f"Part 2: {part2(inputText)}")


if __name__ == '__main__':
    day3()