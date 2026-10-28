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

