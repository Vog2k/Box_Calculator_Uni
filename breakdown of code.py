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
rezL = result % big

medium = int(result // 3)
rezM = result % medium

small = int(result // 1)
rezS = result % small
# Forth variable converting the name to x
x = result

print(big)
print(medium)
print(small)
print()

print("Just my little table for the remainder wont be in the final\n")
print("RemainderL", rezL)
print("RemainderM", rezM)
print("RemainderS", rezS)

print()

if x > 0:
    for i in range(1, x):
        if rezL >= 0:
            print(big, "[Big Boxes filled.]")
            if rezL == 9:
                print(rezL, "[Medium Boxes filled]")
            if rezL == 6:
                print(rezL, "[Medium Boxes filled]")
            if rezL == 4:
                print(rezL, "[Small Boxes filled.]")
            if rezL == 3:
                print(rezM, "[Medium Boxes filled.]")
            if rezL == 2:
                print(rezL, "[Small Boxes filled]")
            if rezL == 1:
                print(rezL, "[Small Boxes filled.]")

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

