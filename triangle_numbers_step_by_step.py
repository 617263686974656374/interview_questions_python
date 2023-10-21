# This program creates a triangle with numbers step by step

def triangle(x):
    num = 1
    for i in range(0, x+1):
        for j in range(0, i+1):
            print(num, end=" ")
            num += 1
        print("\r")


triangle(5)
