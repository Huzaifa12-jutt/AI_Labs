# #list comprehension
# squares=[n ** 2 for n in range(1,6)]
# print(squares)

# evens=[n for n in range(1,21) if n % 2 == 0] # store in n 
# print(evens)

#tuples
# dimensions=(200,50)
# print(dimensions)


fruits=('apple','bannana','cherry')
for index , fruits in enumerate(fruits):  # enumerate multiple data write
    print(index,fruits)
    
#dictionary
print()
print("Dictionary")
student={
    
    "name":"Huzaifa",
    "Regid":"Huzaifa",
    "course":"Python"
}
print(student["name"])
student['course']='Java'  # update value
print(student['course'])

#delete 
del student['Regid']
print(student)

# pop used for delete when backup is required
removed_value=student.pop('course')
print(removed_value)
print(student)