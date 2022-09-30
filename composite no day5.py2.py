a=int(input("A="))
b=int(input("B="))
if(a<=0):
    print("INVALID")
    exit()
if(b<=0):
    print("INVALID")
    exit()
if(a==b):
    print("BOTH CAN'T BE SAME VALUE")
    exit()
elif(a>b):
    print("LARGE VALUE")
    exit()
else:
    f=0
    for i in range(a+1,b):
        f=0
        for j in range(1,i):
            if(i%j==0):
                f+=1
        if(f>1):
            print(i)
