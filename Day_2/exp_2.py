# Get 5 numbers from user
numbers = []
for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Print the list
print("List:", numbers)

# Print its length
print("Length:", len(numbers))

# Print the largest number
print("Maximum:", max(numbers))

# Print the smallest number
print("Minimum:", min(numbers))

# Print the sum
print("Sum:", sum(numbers))

# Print the list in reverse using slicing
print("Reverse:", numbers[::-1])

# Convert the list to a set and print it
numbers_set = set(numbers)
print("Set:", numbers_set)

# Print the type of the list
print("List type:", type(numbers))

# Print the type of the set
print("Set type:", type(numbers_set))