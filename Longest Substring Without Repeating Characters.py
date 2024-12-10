def longest_unique_substring(s):
    char_index = {}
    start = 0
    max_length = 0
    substring = ""

    for i, char in enumerate(s):
        # If the character is already in the substring, move the start
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1

        # Update the last seen index of the character
        char_index[char] = i

        # Calculate the length of the current substring
        current_length = i - start + 1
        if current_length > max_length:
            max_length = current_length
            substring = s[start:i+1]

    return max_length, substring

# Example usage
input_string = "abcabcbb"
length, substring = longest_unique_substring(input_string)
print(f"The longest substring without repeating characters is '{substring}' with length {length}.")
