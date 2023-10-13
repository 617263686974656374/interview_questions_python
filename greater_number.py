# Program to find a grater number of two numbers

def maximum(a,b):
    if a > b:
        print(f"First number {a} is greater than second number {b}")
    elif b > a:
        print(f"Second number {b} is greater than first number {a}")
    else:
        print("Numbers have same value !")


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("-" * 50)

maximum(a, b)
