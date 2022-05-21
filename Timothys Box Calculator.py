num1 = int(input("Please enter number:"))  # Num1 is my variable, requires users input
print()  # Spaces in between to make the terminal look less cramped
num2 = int(input("Please enter second number:"))  # Num2 is my variable, requires users input
print()  # Spaces in between to make the terminal look less cramped

result = num1 + num1

big = int(result / 5)

medium = int(result / 3)

small = int(result / 1)



if result >= 0:
    print("\nBig Box:", big, "\nMedium Box:", medium, "\nSmall Box", small)
