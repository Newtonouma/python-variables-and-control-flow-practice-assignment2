def print_keys_even_values(input_dict):
    for key, value in input_dict.items():
        if value % 2 == 0:
            print(key)

#Display and function calling
example_dict = {'a': 2, 'b': 3, 'c': 4}
print_keys_even_values(example_dict)
