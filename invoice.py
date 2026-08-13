customer = input("enter the customer name:")
items = []
while True:
    name = input("item:")
    if name == "done" :
        break
    quantity = float(input("quantity:"))
    price = int(input("price:"))
    line_total = quantity * price
    item = {"name": name , "quantity": quantity , "price": price, "line_total": line_total}
    items.append(item)
grand_total = 0
for line in items:
    grand_total = grand_total + line["line_total"]
    print (f"grand total:{grand_total} ")

with open("invoice.txt", "w") as file:
    file.write(f"customer : {customer}\n")
    for item in items:
        file.write(f"{item['name']} x{item['quantity']} x{item['price']} = {item['line_total']}\n")
    file.write(f"grand_total: {grand_total}")