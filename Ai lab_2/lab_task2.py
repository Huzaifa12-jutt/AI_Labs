numbers = []
for i in range(1, 16):
    numbers.append(i)
print("The first 15  numbers are:", numbers)

even_numbers = []
odd_numbers = []
for i in numbers:
    if i%2 == 0:
        even_numbers.append(i)
    else:
        odd_numbers.append(i)

print("The even numbers are:", even_numbers)
print("The odd numbers are:", odd_numbers)


numbers.sort(reverse=True) # sort origonal list descending order..
print("Descending order are:", numbers)

print("Middle five numbers are: ",numbers[5:10])
print(" The End of Task 2")