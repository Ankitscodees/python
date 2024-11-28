def is_leap_year(year):
    """
    This function checks if a given year is a leap year.
    A leap year is divisible by 4, but not divisible by 100,
    unless it is also divisible by 400.
    """
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Test the function
test_year = 2024
if is_leap_year(test_year):
    print(f"{test_year} is a leap year!")
else:
    print(f"{test_year} is NOT a leap year.")
