# by ariana daney
# first modified 10-25-19
# unit 6 daily exercises

# ex. 1
names = ["Abigail", "Brenda", "Chad", "Doug", "Emma", "Francis", "George",
         "Harold", "Imogen", "Jackie", "Kurt", "Linda"]
print(names[3:5])
print(names[1:6])
print(names[5:12])
print(names[5:])
print(names[11])
print(names[-1])
print(names[1:8:2])
print(names[0:11:2])
print(names[::2])
print(names[11:8:-1])
print(names[11::-1])
print(names[::-1])


# ex. 2
def are_duplicates(nums):
    for x in range(len(nums)):
        for y in range(x + 1, len(nums)):
            if nums[x] == nums[y]:
                return True
    return False


print(are_duplicates([100, 2, 3, 4, 5, 100]))


# ex. 3


def add_numbers(nums):
    total = 0
    for x in nums:
        total += x
    return total


print(add_numbers([1, 2, 3, 4, 5]))

# ex. 4


def has22(nums):
    for x in range(len(nums)-1):
        if nums[x] == 2 and nums[x + 1] == 2:
            return True
    return False


print(has22([1, 2, 3, 4, 5, 2, 3, 2]))

# ex. 5


def is_sorted(nums):
    for x in range(1, len(nums)):
        if nums[x - 1] > nums[x]:
            return False
    return True


print(is_sorted(["c", "b"]))

# ex. 6


def remove_duplicates(nums):
    for x in range(len(nums)):
        for y in range(x + 1, len(nums)):
            if nums[x] == nums[y]:
                del y
    return nums


print(remove_duplicates([1, 2, 3, 4, 4, 5, 6]))
