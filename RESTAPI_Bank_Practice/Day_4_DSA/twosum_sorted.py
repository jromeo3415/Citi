def two_sum(nums, target):

    left = 0
    right = len(nums) - 1

    while left < right:

        current_sum = nums[left] + nums[right]

        if current_sum == target:
            return [left, right]

        elif current_sum < target:
            left += 1

        else:
            right -= 1

    return []


nums = [1, 2, 3, 4, 6, 8, 11]
target = 10

result = two_sum(nums, target)

print(result)