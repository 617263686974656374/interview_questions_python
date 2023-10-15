# Find a factorial of a number
wrong_input = 0
while wrong_input < 3:
    try:
        factorial = 1
        print("-" * 40)
        num = int(input("Enter a number to find his factorial: "))
        print("-"*40)
        if num < 0:
            print("Factorial doesnt exist for negative numbers !")
            wrong_input += 1
        elif num == 0:
            print("Factorial for 0 is always 1")
            wrong_input += 1
        else:
            for i in range(1,num + 1):
                factorial = factorial * i
            print(f"The factorial of {num} is {factorial}")
            break
    except ValueError:
        print("Enter only a number !")
        wrong_input += 1
else:
    print("Program is over , while you entered not correct number 3 times")
