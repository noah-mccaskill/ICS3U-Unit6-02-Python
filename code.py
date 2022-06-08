#!/usr/bin/env python3

# Created by Noah McCaskill
# Created June 2022
# This program generates random numbers using arrays and finds the max.

import random


def find_max(num_array):
    # this function finds the highest number in the num_array

    max_num = num_array[0]

    for num_check in num_array:
        if num_check > max_num:
            max_num = num_check

    return max_num


def main():
    # this function generates 10 random numbers, calls a function, and outputs the highest one

    num_array = []

    print("This program generates 10 random numbers and finds the highest one.\n")

    # process & output
    for counter in range(0, 10):
        random_num = random.randint(0, 100)
        num_array.append(random_num)
        print("Random number generated: {}".format(random_num))

    # call function
    max_num = find_max(num_array)

    # output
    print("\nThe highest number is {}.".format(max_num))

    print("\nDone.")


if __name__ == "__main__":
    main()
