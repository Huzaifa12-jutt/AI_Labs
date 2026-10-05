print("Welcome to my program")
names=[]
print("------------------------")

print("Enter 6 students names")
for i in range(6):
    names.append(input("Enter name: "))
print("The names are: ",names)

print("------------------------")

#print first name
print("The first name is: ",names[0])

#print last name
print("The last name is: ",names[-1]) # -1 show last element.
print("------------------------")

#add new student at the end of list
names.append(input("Enter new name at end: "))
print("The new list is: ",names)
print("------------------------")

#insert new studebnt position 2
names.insert(2,input("Enter new name at position 2: "))
print("The new list is: ",names)
print("------------------------")

#remove student by name
names.remove(input("Enter name to remove: "))
print("The new list is: ",names)
print("------------------------")

#print final list  along with length of list
print("The final list is: ",names)
print("Length of my list is: ",len(names))
print("End of Task 1")
print("------------------------")

