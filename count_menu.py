# Exercise from Sololearn
'''
You and three Friends go to a baseball game and zou offer to go to the concession stand for everyone.
They each order one thing, and you do as well. Nachos and Pizza both cost 6 $. A Cheeseburger meal costs 10 $
Water is 4 $ and Coke is 5 $. Tax is 7%

Determine the total cost of ordering four items from the concession stand. If one of your friends orders something that
isn't on the menu, you will order a Coke for them instead.
'''

customer_list = []

menu = {"Nachos": 6, "Pizza": 6, "Cheeseburger": 10, "Water": 4, "Coke": 5}
customer = input("Give a four items tha you've been asked to order that are separated by spaces: ").strip().split()

for x in customer:
    if x in menu.keys():
        customer_list.append(menu.get(x))
    else:
        customer_list.append(menu.get("Coke"))

tax = sum(customer_list) * 7 / 100
print("$", sum(customer_list) + tax)
