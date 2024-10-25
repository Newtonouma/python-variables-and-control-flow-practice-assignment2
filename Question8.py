def keys_of_values_greater_than_n(input, n):
    keys = []  #an empty list to add keys
    for key, value in input.items():
        # Check whether the value is greater than n
        if value > n:
            keys.append(key)  # Add the key to the result list if the condition is met
    return keys

dictionary = {'a': 5, 'b': 12, 'c': 3}
n = 4
result = keys_of_values_greater_than_n(dictionary, n)
print("Keys of values greater than", n, "is:", result)
