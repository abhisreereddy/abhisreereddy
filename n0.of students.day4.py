total=int(input("Enter the total users= "))
if(total<=0):
    print("VALUE ERROR")
    exit()
staff=int(input("Enter the staff users= "))
if(staff<=0):
    print("INVALID")
    exit()
a=staff/3
student=total-staff-a
print("Student users=",student)
