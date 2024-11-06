# A function that removes duplicates from a list
def de_dupe(items):
    result = []
    for item in items:
        if item not in result:
            result.append(item)
    return result


# Example run
numbers = [1, 2, 2, 2, 3, 1, 2, 5, 5]

de_duped_nums = de_dupe(numbers)

print(de_duped_nums)
