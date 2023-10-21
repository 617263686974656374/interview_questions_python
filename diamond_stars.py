# This Program make a Diamond - stars

def pyramid(x):
    for i in range(x+1):
        print("  " * (x-i) + "* " * (2*i-1))

    for i in range(x-1, 0, -1):
        print("  " * (x-i) + "* " * (2*i-1))

pyramid(5)
