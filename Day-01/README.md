# Day 1 — Python Fundamentals & Problem Solving
Name: Telugu Shivani
Date: 26 October 2026
Day: 1

## 1. Coding Problem — First Non-Repeating Character

### Approach

1. Remove spaces from the input string using `replace()`.
2. Create an empty dictionary to store the frequency of each character.
3. Traverse the string and count each character using `dict.get()`.
4. Traverse the string again in its original order.
5. Return the first character whose frequency is `1`.
6. If no non-repeating character exists, return a suitable message.

The solution ignores spaces and is case-sensitive. Uppercase and lowercase characters are treated differently.

## Code
def first_non_repeating(text):
    text = text.replace(" ", "")
    freq = {}

    
    for char in text:
        freq[char] = freq.get(char, 0) + 1

    
    for char in text:
        if freq[char] == 1:
            return char

    return "No non-repeating character found"


print(first_non_repeating("programming"))
print(first_non_repeating("aabbcdd"))
print(first_non_repeating("aabbcc"))
print(first_non_repeating("a b c"))



### Test Inputs and Outputs

| Input | Expected output |
|---|---|
| `"programming"` | `"p"` |
| `"aabbcdd"` | `"c"` |
| `"aabbcc"` | `"No non-repeating character found"` |
| `"a b c"` | `"a"` |



### Time and Space Complexity

- **Time complexity:** O(n), because the algorithm traverses the string twice.
- **Auxiliary space complexity:** O(k), where k is the number of distinct characters stored in the dictionary.

Here, n is the length of the input string.

## 2. Concept Question — Python Data Structures

### List vs Tuple vs Set vs Dictionary

| Feature | List | Tuple | Set | Dictionary |
|---|---|---|---|---|
| Ordered | Yes | Yes | No positional order | Yes |
| Duplicates | Allowed | Allowed | Not allowed | Keys must be unique |
| Mutable | Yes | No | Yes | Yes |
| Main use | Ordered collections | Fixed collections | Unique values | Key-value mapping |
| Example | `[1, 2, 2]` | `(10, 20)` | `{1, 2}` | `{"name": "Ravi"}` |

### Scenario 1: Store Unique Student IDs

I would use a **set** because it stores only unique values and supports efficient average-case membership checks.

### Code

student_ids = {101, 102, 103, 101}

print(student_ids)
print(101 in student_ids)


### Output


{101, 102, 103}
True

The duplicate ID `101` is stored only once. Set display order is not guaranteed.

### Scenario 2: Store Student Profile Fields

I would use a **dictionary** because student details can be stored as key-value pairs.

### Code

student = {
    "name": "Ravi",
    "email": "ravi@example.com",
    "phone": "9999999999"
}

print(student["name"])
print(student.get("grade", "Not assigned"))

### Output


Ravi
Not assigned


The dictionary allows us to access values using meaningful keys. The `get()` method returns a default value when the requested key does not exist.

## 3. Debugging Challenge — Student Search

### Issue

The original code prints `"Student not found"` for every student who does not match `"Kiran"`.

This happens because the `else` belongs to the `if` statement inside the loop. Therefore, the `else` executes whenever an individual student does not match, even if Kiran appears later in the list.

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

**Test case 1: Kiran exists**

Output:


Student found: Kiran

**Test case 2: Kiran does not exist**

If the target is changed to `"Rahul"`, the output is:


Student not found


### Explanation

The `break` statement stops the loop when the target student is found.

The `else` block of a `for` loop executes only when the loop finishes without encountering `break`.

This ensures that exactly one correct message is printed.

### Time and Space Complexity

- **Time complexity:** O(n) in the worst case, because every student may need to be checked.
- **Auxiliary space complexity:** O(1), excluding the input list.

Here, n is the number of students.

## 4. What I Learned

- I learned how to use a dictionary to count the frequency of characters.
- I understood how to find the first non-repeating character using two passes through a string.
- I learned the differences between lists, tuples, sets, and dictionaries.
- I understood why sets are useful for storing unique student IDs.
- I learned how dictionaries store student information as key-value pairs.
- I practised using loops, conditions, `break`, and the `for/else` construct.
- I learned how to test edge cases, such as empty strings and strings containing only spaces.
- I improved my understanding of time and space complexity.

## 5. What I Found Difficult

I found it challenging to understand how a dictionary counts character frequencies and how to find the first non-repeating character without repeatedly using `count()`.

I also found it difficult to understand why the original student-search loop printed the not-found message multiple times and how `for/else` fixes the problem.


## Conclusion

Day 1 helped me strengthen my Python fundamentals and problem-solving skills. I practised dictionary frequency counting, compared Python data structures, corrected a loop-related bug, and learned to test edge cases and analyse complexity. These concepts will help me prepare for Python developer interviews.