def reverse_string(s):
    """
    This function reverses a string using recursion.
    """
    if len(s) == 0:
        return s
    else:
        return s[-1] + reverse_string(s[:-1])

# Test the function
input_string = "recursion"
reversed_string = reverse_string(input_string)
print(f"The reverse of '{input_string}' is '{reversed_string}'")
