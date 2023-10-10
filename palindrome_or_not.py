# Program to check if the given number or word is palindrome or not

try:
    check = input("Write a number to check if is palindrome: ")

    double_check = check == check[::-1]
    if double_check:
        print("Is palindrome")
    else:
        print("Is not palindrome")
except ValueError:
    print("Write only a number, please !")
