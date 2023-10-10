# This program check if input number from User is odd or even and if User enter string or float number then
# print message that he have to Enter only valid number
while True:
    try:
        check_number = int(input("Entry number: "))
        if check_number % 2 == 0:
            print(f"Your number {check_number} is odd")
            break
        else:
            print(f"Your number {check_number} is even")
            break
    except ValueError:
        print("Enter only valid number !")
