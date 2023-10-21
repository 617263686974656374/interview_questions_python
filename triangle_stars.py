# This program creates a right triangle with stars
error = 0


def stars(x):
    for i in range(x+1):
        print("* "*i)


while error < 3:
    try:
        stars(int(input("Enter the number of how many stars in the column should be displayed: ")))
        break
    except ValueError:
        print("Write only a number please")
        error += 1
else:
    print("You tried to Enter 3 times wrong Value.\nProgram is over...")
