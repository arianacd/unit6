# by Ariana Daney
# last modified november 6, 2019
# unit 6 project option 1

import random


def are_duplicates(nums):
    """
    this function finds duplicate birthdays by comparing a list to itself
    :param nums: the list
    :return: true if there is a duplicate and false if there is not
    """
    for x in range(len(nums)):
        for y in range(x + 1, len(nums)):
            if nums[x] == nums[y]:
                return True
    return False


def main():
    num_of_runs = int(input("please enter a number of times you want to run this simulation"))
    duplicate_variables = 0
    for x in range(num_of_runs):
        birthdays = []
        for y in range(23):
            ran_num = random.randint(1, 365)
            birthdays.append(ran_num)
        if are_duplicates(birthdays) is True:
            duplicate_variables = duplicate_variables + 1
    print("there were duplicate birthdays", duplicate_variables / num_of_runs * 100, "% of the time")
    print(duplicate_variables, "of the", num_of_runs, "simulations had duplicate birthdays")


main()
