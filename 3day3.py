b=int(input("Enter length of array:"))
a=[]
e=[]
for i in range(0,b):
    c=input("Enter the string")
    a.append(c)
for i in range(0,b):
    d=len(a[i].split())
    e.append(d)
print("LIST =",a)
print("MAX words in a string =",max(e))
