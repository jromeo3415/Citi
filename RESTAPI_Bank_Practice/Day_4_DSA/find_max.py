def find_max(numbers):
    biggest = numbers[0]
    for number in numbers:
        if number > biggest: biggest = number

    return biggest

nums = [2, 3, 66, 3, 463, 77, 9, 0]
print(find_max(nums))