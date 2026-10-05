list1=[1,2.2,'three']  
print(list1)

#accessing element of list using index

print(list1[0])
print(list1[-1])

#modifying elements of list adding,removing elements

#modification of list
list1[0]=100
print(list1)

#adding elements in list
list1.append(200)
print(list1)

#inserting elements in list
list1.insert(0,400)
print(list1)

#extending list with another list
list2=[500,600]
list1.extend(list2)
print(list1)

#removing elements from list
list1.remove(100)
print(list1)



#sorting
list2=[3,1,4,2]
list2.sort()
print(list2)

list2.sort(reverse=True)
print(list2)

list2.reverse()
print(list2)

print(len(list2))

#using for loop to access list
for i in list2:
    print(i)
    
for i in range(0,11):
    print(i)
    
print("----------------")

for i in range(0,5,2):  #2 means step value
    print(i)
    
#slicing of list

print (list2[0:2])
print(list2[:3]) # means 0 to 3 index 3 not included
print(list2[1:]) # means 1 to end of list
print(list1[::]) # means whole list