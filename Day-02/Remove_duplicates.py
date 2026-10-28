def remove_duplicates(numbers):
    unique_numbers = []

    for number in numbers:
        if number not in unique_numbers:
            unique_numbers.append(number)

    return unique_numbers


print(remove_duplicates([1, 2, 2, 3, 1, 4]))
print(remove_duplicates([5, 5, 5, 5]))
print(remove_duplicates([1, 2, 3, 4]))
print(remove_duplicates([]))