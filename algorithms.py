# Write a factorial function
# Write a find maximum in a list function
# Write linear search function
# Write a fibonacci sequence function
# Write a simple menu to choose between functionalities
# Ask the user for input and call the correct function
# block logget out users
# mark big o
prompt = """
Choose an option:

1. Login
2. Factorial
3. Find Max
4. Linear Search
5. Fibonacci
6. Exit
        """

logged_in = False


def login():
    global logged_in
    username = input("Username: ")
    password = input("Password: ")

    if username == "admin" and password == "admin":
        logged_in = True
        print("Login Successful!")
    else:
        logged_in = False
        print("Login Failed!")


def require_login():
    if not logged_in:
        print("Access Denied, please login.")
        return False
    return True


def factorial(n):
    if not require_login():
        return
    if n == 1 or n == 0:
        return 1
    else:
        return (n * factorial(n-1))


def find_max(numbers):
    if not require_login():
        return
    nums = numbers[0]

    for num in numbers:
        if num > nums:
            nums = num

    return nums


def linear_search(numbers, target):
    if not require_login:
        return
    index = -1
    for i in range(len(numbers)):
        if numbers[i] == target:
            return i

    return index


while True:
    print(prompt)
    choice = input("Your choice: ")

    if choice == "1":
        login()
    elif choice == "2":

        num = int(input("Enter a number: "))
        result = factorial(num)
        print("The factorial of", num, "is", result)

    elif choice == "3":
        num = input("Enter the list seperated by spaces: ")
        nums = [int(n) for n in num.split()]
        result = find_max(nums)
        print("The maximum number is", result)

    elif choice == "6":
        break

print("Program ended")
