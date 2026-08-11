import json
import random
import string


def order_tracker():
    
    try:
        with open("toolbox.json", "r") as file:
            existing_orders = json.load(file)
    except FileNotFoundError:
        existing_orders = []

    customer = input("enter your name:")
    item = input("your item:")
    price = float(input("price:"))
    order = {"customer": customer, "item": item, "price":price}

    existing_orders.append(order)

    with open("toolbox.json", "w") as file:
        json.dump(existing_orders,file)
        
    total = 0
    for order in existing_orders:
        total = total + order["price"]
    print(f"total sales = {total}")

def view_orders():
    try:
        with open("toolbox.json", "r") as file:
            orders = json.load(file)
    except FileNotFoundError:
        orders = []
        if len(orders) == 0:
            print("no orders yet")
        else :
            for order in orders:
                print(f"{order['customer']} bought for {order['item']} for {order['price']} ")
    

def expense_tracker():
    try:
        with open("expenses.json", "r") as file:
            expense_list = json.load(file)
    except FileNotFoundError:
        expense_list = []

    category = input("category:")
    amount = float(input("amount:"))
    expense = {"category": category, "amount": amount}
    expense_list.append(expense)

    with open("expenses.json", "w") as file:
        json.dump(expense_list,file)

    total = 0
    for expense in expense_list:
        total = total + expense["amount"]
    print(f"total expense = {total}")

def password_generator():
    length = int(input("password length:"))
    characters = string.ascii_letters + string.digits + string.punctuation

    password = ""
    for i in range(length):
        password = password + random.choice(characters)
    print(f"your password: {password}")    

while True:
    print("\n 1.Order 2.expense 3.password 4.view 5.quit")
    choice = input("pick one")
    if choice == "1":
        order_tracker()
    elif choice == "2":
        expense_tracker()
    elif choice == "3":
        password_generator()
    elif choice == "4":
        view_orders()
    elif choice == "5":
        break
    else:
        print("not a valid option")
