# sorting an array by pairs

# sort by 2nd element
pairs = [(5, 10), (3, 20), (5, 5), (1, 15)]

# called sorted_by_second = sorted() to sort by first element
sorted_by_second = sorted(pairs, key=lambda x: x[1])

print(sorted_by_second)
# Output: [(5, 5), (5, 10), (1, 15), (3, 20)] 


# sorting in desending order:
numbers = [7, 3, 11, 2, 5]
numbers.sort(reverse=True)
print(numbers)
