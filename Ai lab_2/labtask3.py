attendance_list = ["Present", "Present", "Absent", "Present", "Absent", "Present", "Absent", "Present", "Present", "Absent"]

#display full attendance using for loop
for i in range(len(attendance_list)): # means attendance_list ki length 10 times loop chly ga
    print("Student", i+1, "is", attendance_list[i])
    

present_count = 0
absent_count = 0
for j in attendance_list:
    if j == "Present":
        present_count += 1
    else:
        absent_count += 1

print("Total Present:", present_count)
print("Total Absent:", absent_count)


print(attendance_list[0:5]) # first five students attendance
print(attendance_list[-5:]) # last five students attendance

# reverse list
attendance_list.reverse()
print("Reversed attendance list:", attendance_list)


#calculate and display attendacne percentage
total_students = len(attendance_list) # which is 10
attendance_percentage =(present_count/total_students)*100
print("Attendance Percentage:", attendance_percentage)
