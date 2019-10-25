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
    for x in nums:
        for y in nums[x+1:]:
            if x == y:
                return True
    return False


print(are_duplicates([1, 2, 3, 4, 5, 2]))


# ex. 3
def add_numbers(nums):
    total = 0
    for x in range:
        total = x + (x+1)


are_duplicates([nums])