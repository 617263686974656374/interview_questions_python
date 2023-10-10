# This program find if the given number is prime or not

number = int(input("Write a number to check if is prime: "))

for i in range(2, number):
    if (number % i) == 0:
        print(f"Number {number} is not prime")
        break
    else:
        print(f"Number {number} is a prime")
        break

