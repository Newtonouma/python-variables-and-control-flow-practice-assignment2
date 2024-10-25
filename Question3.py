def summation(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

#calling the function  and displaying result
numbers = [1, 2, 3, 4, 5]
result = summation(numbers)
print("The sum is:", result)
