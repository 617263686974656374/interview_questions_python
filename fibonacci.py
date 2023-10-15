# This program find a fibonacci of a number
wrong_input = 0

while wrong_input < 3:
    try:
        repeat = int(input("Enter, how many number of sequence want to see: "))
        num1, num2 = 0, 1
        count = 0

        if repeat <=0:
            print("*" * 50, "\n\t****\tPlease, enter a positive number\t\t****\n", "*" * 50)
            wrong_input += 1
        else:
            print("Fibonacci sequence:")
            while count < repeat:
                print(num1)
                fib = num1 + num2
                num1 = num2
                num2 = fib
                count += 1
            break
    except ValueError:
        print("-" * 50, "\n\t****\tEnter only a number, please\t\t****\n", "-" * 50)
        wrong_input += 1
else:
    print("Program is over, while you entered 3 times wrong value")
