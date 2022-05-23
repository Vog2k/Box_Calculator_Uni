# Box Calculator
# BY Timothy Leatau

# First variable asking for an input number from the user
first_number = int(input("Please enter you're first number :"))

print()  # Space to make the command look more free

# Second variable asking for an input number from the user
second_number = int(input("Please enter you're second number :"))

print()  # Space to make the command look more free

# This line will show the user the equation then convert to boxes
print("Your results\n")

# Third variable adding both variables and storing it in a new variable named result
result = first_number + second_number

print(first_number, "+", second_number, "=", result)
print("-------------------------------------------")
print()

# Big box containg the result of the equation entered and a division sign along with the size being 5
big = int(result // 5)

medium = int(result // 3)
"""'/' IS DIVIDE"""
small = int(result // 1)
# Forth variable convering the name to x
x = result
"""Trying to make the Big box fill first before heading to the next avaliable number being 3/medium box ect"""

print()

print(big, "Big")
print(medium, "Medium ")
print(small, "small")
print()

rezL = result % big
rezM = result % medium
rezS = result % small

print("RemainderL", rezL)
print("RemainderM", rezM)
print("RemainderS", rezS)


print()

if x > 0:
    for i in range(1, x):
        if rezL >= 0:
            print(big, "[Big Boxes filled1]")
            if rezL == 3:
                print("med", rezL)
            if rezL == 1:
                print("small", rezL)
            if rezL == 2:
                print("small", rezL)


        break
