# This program finding the given number is positive or negative
while True:
    try:
        check_number = int(input("Enter the number: "))

        if check_number > 0:
            print(f"Your number {check_number} is positive")
            break
        elif check_number == 0:
            print(f"Your number {check_number} is zero")
            break
        else:
            print(f"Your number {check_number} is negative")
            break
    except ValueError:
        print("Entry only number,please !")
