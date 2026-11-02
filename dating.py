#!/usr/bin/env python3
# Created By: Kaylee R
# Date: 10, 27, 2026
# This program gets the users age and checks if
#  they are eligible to date
# the grandparents grandchild.


import constants


def main():
    age_str = input("Enter your age: ")

    # check if age is a valid input
    try:
        age_int = int(age_str)
        if age_int < 0:
            print("A negative number is not a valid age")
        elif age_int > 120:
            print("No human can live that long")
        elif age_int > constants.MIN_AGE and age_int < constants.MAX_AGE:
            print("You are eligible!")
        else:
            print("You are not eligible for my grandchild")
    except:
        print("{} is not a valid age".format(age_str))
    finally:
        print("Thank you for you interest")


if __name__ == "__main__":
    main()
