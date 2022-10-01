x=int(input("Enter value of X: "))
n=int(input("Enter value of N: "))
print("1=pow\n2=Add\n3=Sub\n4=Mul\n5=Div")
choice=int(input("Choice:"))
if (choice==1):
    pow=x**n
    print("Pow(%d,%d)=%d"%(x,n,pow))
elif (choice==2):
    add=x+n
    print("Add(%d,%d)=%d"%(x,n,add))
elif (choice==3):
    sub=x-n
    print("Sub(%d,%d)=%d"%(x,n,sub))
elif (choice==4):
    mul=x*n
    print("Mul(%d,%d)=%d"%(x,n,mul))
elif (choice==5):
    try:
        div=x/n
        print("Div(%d,%d)=%d"%(x,n,div))
    except ZeroDivisionError:
        print ("ZeroDivisionError")
else:
    print("Invalid Input...!")
