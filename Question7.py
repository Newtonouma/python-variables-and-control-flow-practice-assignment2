def remove_duplicates(list):
    new_list = []  #an empty list to store unique elements
    for item in list:
        if item not in new_list:  # Check whether the current item is already in the new list
            new_list.append(item)  # Adding unique item into the new list
    return new_list

duplicates_list = [1, 2, 2, 3, 4, 4, 5]
result = remove_duplicates(duplicates_list)
print("List without duplicates is :", result)
