num1 = int(input("Please enter number:"))  # Num1 is my variable, requires users input
print()  # Spaces in between to make the terminal look less cramped
num2 = int(input("Please enter second number:"))  # Num2 is my variable, requires users input
print()  # Spaces in between to make the terminal look less cramped

result = num1 + num1

big = int(result / 5)

medium = int(result / 3)

small = int(result / 1)

x = result

if x > 0:
    for i in range(5, x):
        if x % 5 == 0:
            print("Big box |5|:", big)

            print("Small box |1|:", small)
            break
        elif x % 3 == 0:
            print("Medium box |3|:", medium)
            print("Small box |1|:", small)

            break
        elif x % 1 == 0:
            print("Small box |1|:", small)
            break
else:
    print('give a positive number')

"""if x > 0:
    for i in range(3, x):
        if x % 3 == 0:
            print("BIG. MED BOX2",big,  medium)
            break
        else:
            print("ALL BOXES2",big , medium , small)
            break
else:
    print('give a positive number')

if x > 0:
    for i in range(1, x):
        if x % 1 == 0:
            print("SMALL3", small)
            break
else:
    print('give a positive number')"""


"""if result >= 0:# is odd use 5s and 3s first
    print("\nBig Box:", big, "\nMedium Box:", medium, "\nSmall Box", small)
else:
    print()"""