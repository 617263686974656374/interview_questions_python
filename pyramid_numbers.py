# This Program make a Pyramid - numbers


def pyramid(x):
    for i in range(1, x+1):
        num = str(i) + ' '
        print("  " * (x-i) + num * (2*i-1))


pyramid(9)
