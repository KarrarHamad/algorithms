# Write a factorial function
# Write a find maximum in a list function
# Write linear search function
# Write a fibonacci sequence function
# Write a simple menu to choose between functionalities
# Ask the user for input and call the correct function
# block logget out users
# mark big o


def fact(n):

    factorial = 1

    for i in range(n):
        factorial *= i+1

    return factorial


num = int(input("factorial:"))
print(f"Factorial of {num} is {fact(num)}")
