def max_window_sum(numbers, k):
    if k <= 0 or k > len(numbers):
        raise ValueError("k must be between 1 and the list length")

    window_sum = 0

    for i in range(k):
        window_sum += numbers[i]

    max_sum = window_sum

    for i in range(k, len(numbers)):
        window_sum = window_sum - numbers[i - k] + numbers[i]

        if window_sum > max_sum:
            max_sum = window_sum

    return max_sum


print(max_window_sum([2, 1, 5, 1, 3, 2], 3))
print(max_window_sum([1, 2, 3, 4, 5], 2))
print(max_window_sum([-5, -2, -8, -1], 2))
print(max_window_sum([10, 20, 30], 3))