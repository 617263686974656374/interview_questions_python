# This program (sum,multiply,divide,exponentiation,floor divide) numbers from User

def run_program(num1, num2, ch):
    if ch == 1:
        print(f"{num1} + {num2} = {sum(num1, num2)}")
    elif ch == 2:
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif ch == 3:
        print(f"{num1} / {num2} = {divide(num1, num2)}")
    elif ch == 4:
        print(f"{num1} ** {num2} = {exponentiation(num1, num2)}")
    elif ch == 5:
        print(f"{num1} // {num2} = {floor_divide(num1, num2)}")
    elif ch == 6:
        print(f"{num1} + {num2} = {sum(num1, num2)}\n{num1} * {num2} = {multiply(num1, num2)}\n"
              f"{num1} / {num2} = {divide(num1, num2)}\n{num1} ** {num2} = {exponentiation(num1, num2)}\n"
              f"{num1} // {num2} = {floor_divide(num1, num2)}")


def sum(num1, num2):
    return num1 + num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return round(num1 / num2, 2)


def exponentiation(num1, num2):
    return num1 ** num2


def floor_divide(num1, num2):
    return num1 // num2


print("*** Welcome in easy calculation ***")
mistake = 0
while mistake <= 3:
    try:
        choose = int(input("Entry number of your choose\n\t1: sum\t\t\t\t2: multiply\n\t3: divide\t\t\t"
                           "4: exponentiation\n\t5: floor divide\t\t6: all together\n"))
        if choose > 6:
            print("Wrong option. Write only numbers from 1 to 6")
            mistake += 1
            continue

        number_1 = int(input("Entry first number: "))
        number_2 = int(input("Entry second number: "))

        run_program(number_1, number_2, choose)
        break
    except ValueError:
        print("Write only a valid number please")
        mistake += 1
else:
    print("\n\tYour option was wrong more then 3 times.\n\tHave a nice day !!!")






