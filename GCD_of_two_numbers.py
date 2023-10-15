# This program find  GCD (Greatest Common Divisor) or HCF (Highest Common Factor) of two numbers is the largest
# number that divides both of them.
def gcd(a, b):
    if (b == 0):
        return a
    return gcd(b, a % b)


wrong_input = 0

while wrong_input < 3:
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        if(gcd(num1, num2)):
            print(f"GCD of {num1} and {num2} is: {gcd(num1, num2)}")
            break
        else:
            print("Not found")
            break
    except ValueError:
        print("Enter only a number, please")
        wrong_input += 1
else:
    print("You entered 3 times wrong value. Program is over")
