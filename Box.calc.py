# Box Calculator
# BY Timothy Leatau

# First variable asking for an input number from the user
first_number = int(input("Please enter you're first number :"))

print()  # Space to make the command look more free

# This line will show the user the equation then convert to boxes
print("Your results\n")

# Third variable adding both variables and storing it in a new variable named result
result = first_number

print(result)
print("-------------------------------------------")
print()

big = 0
med = 0
small = 0
if result >= 5:
    # Big box contains the result of the equation entered and a division sign along with the size being 5
    big = int(result // 5)
    rem = result % 5

    if rem > 0:
        medium = int(rem // 3)
        rem = rem % 3
    if rem > 0:
        small = int(rem // 1)

total = big + med + small
print(big)
print(med)
print(small)