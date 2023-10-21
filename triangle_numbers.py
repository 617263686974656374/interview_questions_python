# This program creates a right triangle with numbers

def triangle(x):
    for i in range(1, x+1):
        num = str(i) + " "
        print(num * i)

triangle(5)
