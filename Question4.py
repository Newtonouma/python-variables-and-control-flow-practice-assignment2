def reversing(fruits):
    reversed = [string[::-1]
                for string in fruits]
    return reversed

#calling function and printing the value
fruits = ["apple", "banana", "cherry"]
result = reversing(fruits)
print("Reversed strings:", result)
