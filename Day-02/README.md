# Day 2 — Python Coding & Problem Solving

Name: Telugu Shivani
Date: 28 October 2026
Day: 2

## 1. Coding Problem — Remove Duplicates from a List

### Approach

1. Create an empty list to store unique elements.
2. Traverse the input list using a `for` loop.
3. Check whether the current element is already present in the new list.
4. If it is not present, append it to the new list.
5. Return the new list after checking all elements.

This approach preserves the original order of the elements and does not use a one-line shortcut.

### Code


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


### Test Inputs and Outputs

| Input | Expected output |
|---|---|
| `[1, 2, 2, 3, 1, 4]` | `[1, 2, 3, 4]` |
| `[5, 5, 5, 5]` | `[5]` |
| `[1, 2, 3, 4]` | `[1, 2, 3, 4]` |
| `[]` | `[]` |


### Time and Space Complexity

- **Time complexity:** O(n²) in the worst case because checking whether an element exists in a list takes O(n), and this check may be repeated for every element.
- **Auxiliary space complexity:** O(n) because the new list can store up to n unique elements.

Here, n is the number of elements in the input list.

## 2. Coding Problem — Maximum Sum of a Contiguous Window

### Approach

1. Check whether `k` is valid. It must be greater than zero and no larger than the length of the list.
2. Calculate the sum of the first `k` elements.
3. Store this sum as the initial maximum sum.
4. Move the window one position at a time.
5. Subtract the element leaving the window and add the new element entering it.
6. Update the maximum sum whenever a larger sum is found.
7. Return the maximum sum.

This technique is called the **Sliding Window technique**. It avoids calculating the sum of every window from the beginning.

### Code


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

try:
    print(max_window_sum([1, 2, 3], 0))
except ValueError as error:
    print(error)


### Test Inputs and Outputs

| Input | Expected output |
|---|---|
| `([2, 1, 5, 1, 3, 2], 3)` | `9` |
| `([1, 2, 3, 4, 5], 2)` | `9` |
| `([-5, -2, -8, -1], 2)` | `-3` |
| `([10, 20, 30], 3)` | `60` |
| `([1, 2, 3], 0)` | `ValueError` |
| `([1, 2, 3], 4)` | `ValueError` |
| `([], 1)` | `ValueError` |

### Time and Space Complexity

Time complexity: O(n), because each element is processed at most a constant number of times.
Auxiliary space complexity: O(1), because only a few variables are used.

Here, n is the number of elements in the input list.

### 3. Coding Problem — Two Pointers Technique


### Approach

1.Initialize two pointers: left at the beginning of the list and right at the end.

2.Calculate the sum of the elements at both pointer positions.

3.If the sum equals the target, return True.

4.If the sum is smaller than the target, move the left pointer one step to the right.

5.If the sum is greater than the target, move the right pointer one step to the left.

6.Continue until the pointers meet.

7.If no matching pair is found, return False.

8.This technique works efficiently when the input list is sorted.

### Code

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

Test Inputs and Outputs

Input

Expected output

([1, 2, 4, 6, 8], 10)

True

([1, 3, 5, 7], 12)

True

([1, 2, 3, 4], 10)

False

([], 5)

False

([5], 5)

False

Time and Space Complexity

Time complexity: O(n), because each pointer moves through the list at most once.

Auxiliary space complexity: O(1), because only a few variables are used.

Here, n is the number of elements in the input list.

## 3. Debugging Challenge — Student Search

### Issue

The original code prints `"Student not found"` for every student who does not match the target name. This happens because the `else` belongs to the `if` statement inside the loop.

As a result, the program may print `"Student not found"` even when the student is present in the list.

### Fixed Code


students = ["Ravi", "Anil", "Kiran", "Suresh"]
target = "Kiran"

for student in students:
    if student == target:
        print("Student found:", student)
        break
else:
    print("Student not found")


### Test Inputs and Outputs

**Test case 1: Student exists**

Output:


Student found: Kiran


**Test case 2: Student does not exist**

If `target = "Rahul"`, the output is:


Student not found

### Explanation

The `break` statement stops the loop when the target student is found.

In Python, the `else` block of a `for` loop executes only when the loop finishes normally without encountering `break`.

Therefore, the program prints exactly one appropriate message.

### Time and Space Complexity

- **Time complexity:** O(n) in the worst case, because every student may need to be checked.
- **Auxiliary space complexity:** O(1), excluding the input list.

Here, n is the number of students.

## 4. What I Learned

- I learned how to remove duplicate elements from a list while preserving their original order.
- I understood how to use loops and conditions to solve coding problems.
- I learned how the Sliding Window technique helps find the maximum sum of a contiguous window efficiently.
- I understood how to validate invalid values of `k`.
- I practised handling edge cases, such as empty lists and negative numbers.
- I learned how `break` and the `for/else` construct help solve search problems correctly.
- I improved my understanding of time and space complexity.

## 5. What I Found Difficult

I found it challenging to understand how to preserve the original order while removing duplicates and how to update the window sum without recalculating the entire sum each time.

I also needed to understand how the `else` block of a `for` loop works and why it should not be confused with the `else` belonging to an `if` statement.

## Conclusion

Day 2 helped me improve my Python coding and problem-solving skills. I practised removing duplicates, implementing the Two-Pointers technique and Sliding Window technique, validating inputs, debugging loops, and analysing time and space complexity. These concepts will help me solve Python coding problems more efficiently during technical interviews.