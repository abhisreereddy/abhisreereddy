a=int(input("Enter the numbers of elements"))
if(a>0):
    b=[]
    for i in range(0,a):
        c=int(input("Enter the number :"))
        b.append(c)
    o=0
    e=0
    for i in b:
        if(i%2==0):
            s=i*i
            e=e+s
        else:
            t=i*i
            o=o+t
    print("EVEN=",e)
    print("ODD=",o)
else:
    print("The entered number is invalid")
