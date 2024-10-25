def maximum_in_tuple(numbers):
    largest_number = numbers[0]

    for num in numbers:
        # changing the largest number if the current number is greater
        if num > largest_number:
            largest_number = num
    return largest_number


numbers = (10, 20, 30, 40, 50)
result = maximum_in_tuple(numbers)
print("The largest number in the tuple is:", result)
