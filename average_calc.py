#!/usr/bin/env python3

# Created by: Marcus Wehbi
# Created on: Dec 14 2022
# This program uses a for loop to generate 10 random numbers and then
# Calculate their average

import constants
import random


# Function to calculate the average and display it
def main():
    # Initialize the sum and the counter
    sum = 0
    counter = 0

    # Set an empty string to hold marks
    list_of_ints = []

    # Explain what the program does
    print(
        "This program generates a list of random "
        "numbers between 0 and 100, then calculates the average."
    )
    print("")

    # For loop to get ten numbers from 0 to 100 (marks), and add them to a list
    for counter in range(constants.MAX_ARRAY_SIZE):
        # Generate random number
        list_of_ints.append(random.randint(constants.MIN_NUM, constants.MAX_NUM))
        # Add each number to the sum
        sum = sum + list_of_ints[counter]
        # Keep track of the marks you are adding
        print(
            "{} added to the list at "
            "position {}".format(list_of_ints[counter], counter)
        )

    # Calculate average of all marks
    average = sum / constants.MAX_ARRAY_SIZE
    print("")
    # Print the average
    print("The average is {}".format(str(average)))


if __name__ == "__main__":
    main()
