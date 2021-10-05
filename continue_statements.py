#!/usr/bin/env python3

# Created by: Haokai Li
# Created on: Oct 2021
# This Program is about break statements

import random


def main():
    # This function is about break statements
    loop_number = 0
    answer_number = 0

    # input
    user_string = input("How many numbers are you going to add: ")
    print("")

    # process
    try:
        user_number = int(user_string)
        for loop_number in range(user_number):
            # input
            add_string = input("Enter the number to add: ")
            # process
            try:
                add_number = int(add_string)
                if add_number < 0:
                    continue
                else:
                    answer_number = answer_number + add_number

            except Exception:
                # output
                print("You didn't enter an integer.")
        # output
        print("Sum of just the positive numbers is = {}".format(answer_number))

    except Exception:
        # output
        print("You didn't enter an integer.")
        print("")

    print("\nDone.")


if __name__ == "__main__":
    main()
