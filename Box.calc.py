# Box Calculator
# BY Timothy Leatau

# First variable asking for an input number from the user
first_number = int(input("Please enter you're number :"))

print()  # Space to make the command look more free

# This line will show the user the equation then convert to boxes
print("Your results\n")

# Third variable adding both variables and storing it in a new variable named result
result = first_number

print(result)
print("-------------------------------------------")
print()

# Box variables, The big box can hold up to 5, While the medium box contains 3 and the small box contains 1
big = 0
med = 0
small = 0

if result >= 5:  # If the result is more than or equal to 5
    big = int(result // 5)  # Result/Users input divided by 5
    rem = result % 5

    if rem >= 3:
        med = int(rem // 3)
        rem = rem % 3

    if rem > 0:
        small = int(rem // 1)
        rem = rem % 1
else:
    if first_number == str(""):
        print("Please enter a number")

total = big + med + small
print(big, "Large box filled")
print(med, "Medium box filled")
print(small, "Small box filled")

"""Test case: Testing that the users inputs compiles 
input: 5
expected output: 1 Big box is filled
actual output: 1 Big box is filled with medium being 0 and small also being 0
result pass"""

"""Test case: Testing that the users inputs compiles 
input: (None)
expected output: crash
actual output: crash
result fail"""

"""Test case: Testing that the users inputs compiles 
input: (string)
expected output: crash
actual output: crash
result fail"""
