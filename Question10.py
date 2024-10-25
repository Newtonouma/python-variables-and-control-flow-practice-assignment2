def changing_tuples_to_dict(tuple_list):
    result_dict = {}
    for item in tuple_list:
        key, value = item  # making the tuple to be in keys and valuess
        result_dict[key] = value  # Adding them into the dictionary
    return result_dict


list = [("apple", 5), ("banana", 3), ("cherry", 7)]
result = changing_tuples_to_dict(list)
print("Resulting dictionary:", result)
