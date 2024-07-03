# Read input values from the user
A, B, C = map(int, input("Enter the lengths of the three sides of the triangle separated by spaces: ").split())

# Check if the given sides form a valid triangle
if (A + B > C) and (A + C > B) and (B + C > A):
    print("Yes")
else:
    print("No")
