shopping_list = [
    {"item": "Notebook", "price": 150, "purchased": False},
    {"item": "Pen", "price": 30, "purchased": True},
    {"item": "USB Drive", "price": 900, "purchased": False}
]

items_to_buy = []
remaining_cost = 0

for item in shopping_list:
    if item["purchased"] == False:
        items_to_buy.append(item["item"])
        remaining_cost = remaining_cost + item["price"]

print("Still need to buy:", items_to_buy)
print("Remaining cost:", remaining_cost)