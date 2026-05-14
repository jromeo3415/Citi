def two_sum(numbers, target):
    num_dict = {}
    for index, number in enumerate(numbers):
        num_dict[number] = index

    for index, number in enumerate(numbers):
        remainder = target - number
        if remainder in num_dict:
            return [index, num_dict[remainder]]
    return [-1, -1]

nums = [1, 2, 3, 4, 6, 8, 11]
target = 10

result = two_sum(nums, target)

print(result)