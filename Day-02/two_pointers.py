def has_pair_with_sum(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]

        if current_sum == target:
            return True
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return False


print(has_pair_with_sum([1, 2, 4, 6, 8], 10))
print(has_pair_with_sum([1, 3, 5, 7], 12))
print(has_pair_with_sum([1, 2, 3, 4], 10))
print(has_pair_with_sum([], 5))
print(has_pair_with_sum([5], 5))