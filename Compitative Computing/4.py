# Read input values from the user
n, k = map(int, input("Enter the number of schoolchildren and the number of apples separated by a space: ").split())

# Calculate the number of apples that remain in the basket
remaining_apples = k % n

# Print the number of remaining apples
print(remaining_apples)
