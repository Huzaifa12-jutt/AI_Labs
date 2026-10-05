list_fruit=[("Apple",150),("Banana",200),("Cherry",590),("Mango",590),("Orrange",350)]

# part a:
for fruit, price in list_fruit:
    print(fruit, price)
    
# part b:
print("Part b:")
fruit_names=[fruit for fruit, price in list_fruit] # prices ko separate kr dia
print(fruit_names)

# part c  
print("Total Price of all fruits: ")
total_price=sum([price for fruit, price in list_fruit])# devide in 2 diffrent
print(total_price)

# part d:
list_fruit[0]=("Apple",800)
print(list_fruit)

