def check_whether_has_pair_with_sum(numbers, sum):
    seen = set()  # empty set for numbers already seen
    for num in numbers:
        complement = sum - num
        if complement in seen:  # Check for complement in the set
            return True  #return True if in
        seen.add(num)
    return False

list = [2, 7, 11, 15]
target = 9
result = check_whether_has_pair_with_sum(list, target)
print("Is there a pair with the sum", target, "?", result)
