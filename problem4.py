def find_first_non_repeated_char(string):
    char_frequency = {}
    for char in string:
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1

    for char in string:
        if char_frequency[char] == 1:
            return char
    return None


input_string = "aabbccdeeffg"
result = find_first_non_repeated_char(input_string)

if result is not None:
    print("First non-repeated character:", result)
else:
    print("No non-repeated character found.")