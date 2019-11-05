# by Ariana Daney
# last modified november 5, 2019
# unit 6 project option 1

import random


def are_duplicates(nums):
    for x in range(len(nums)):
        for y in range(x + 1, len(nums)):
            if nums[x] == nums[y]:
                return True
    return False


num_of_runs = int(input("please enter a number of times you want to run this simulation"))
duplicate_variables = 0
for x in range(num_of_runs):
    birthdays = []
    for y in range(23):
        ran_num = random.randint(1, 365)
        birthdays.append(ran_num)
    print(are_duplicates(birthdays))
    if are_duplicates(birthdays) is True:
        duplicate_variables = duplicate_variables + 1
print(duplicate_variables/num_of_runs * 100)
print(duplicate_variables)






