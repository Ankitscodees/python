def generate_power_set(input_set):
    """
    This function generates all unique subsets (the power set) of a given list.
    """
    # Start with an empty subset
    power_set = [[]]
    
    for item in input_set:
        # Add each item to existing subsets
        new_subsets = [subset + [item] for subset in power_set]
        power_set.extend(new_subsets)
    
    return power_set

# Test the function
input_list = [1, 2, 3]
result = generate_power_set(input_list)

print(f"The power set of {input_list} is:")
for subset in result:
    print(subset)
