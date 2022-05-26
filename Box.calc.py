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

# Big box contains the result of the equation entered and a division sign along with the size being 5
big = int(result // 5)
medium = int(result // 3)
small = int(result // 1)

rezL = result % big
rezM = result % medium
rezS = result % small

# Forth variable converting the name to x
x = result
print(big, "Big")
print(medium, "Medium ")
print(small, "small")

print()

print()

print("RemainderL", rezL)
print("RemainderM", rezM)
print("RemainderS", rezS)

print()

split = rezL - 2

# TEST
"""if x > 0:
    for i in range(5, x):
        if rezL >= 0:
            print(big, "[Big Boxes filled.7]")
            if rezL == 9:
                print(rezL, "[Medium Boxes filled6]")
            for i in range(4, x):
                if rezL == 4:
                    print(rezL, "[Small Boxes filled4.]")
        break
    for i in range(3, x):
        if rezL == 6:
            print(rezL, "[Medium Boxes filled5]")
        if rezL >= 3:
            print(split, "[Medium Boxes filled5]")

        if rezL == 2:
            print(rezL, "[Small Boxes filled2]")
        if rezL == 1:
            print(rezL, "[Small Boxes filled.1]")

        break"""


if x > 0:
    for i in range(1, x):
        if x % 5 <= 10:
            print()
            print(big, "[Big Boxes filled]")
            break
        elif x % 3 >= 3:
            print()
            print(medium, "[Medium Boxes filled]")
            break
        elif x % 1 == 1:
            print(small, "[Small Boxes filled]")
            break

"""Test case: Testing that the users inputs compiles 
input: (None)
expected output: crash
actual output: crash
result fail"""

"""Test case: Testing that the users inputs compiles 
input: (9, 9)
expected output: 3 Big boxes and 1 medium
actual output: 3 Big boxes
result fail"""

"""Test case: Testing that the users inputs compiles 
input: (10, 10)
expected output:4 [Big Boxes filled.]
actual output:4 [Big Boxes filled.]
result pass"""

"Code runs well i just cant find the right way to implement 3's that well "
