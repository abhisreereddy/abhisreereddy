def pow(x,n):
    return(x**n)
def add(x,n):
    return(x+n)
def sub(x,n):
    return(x-n)
def mul(x,n):
    return(x*n)
def div(x,n):
    return(x/n)
x=int(input("x:"))
n=int(input("n:"))
print("enter your choice:")
print("1.power")
print("2.addition")
print("3.subtraction")
print("4.multiplication")
print("5.division")
while True:
    choice=input("enter choice:")
    if choice in ('1','2','3','4','5'):
        if(choice=='1'):
            print('pow(x,n)=',pow(x,n))
        elif(choice=='2'):
            print('add(x,n)=',add(x,n))
        elif(choice=='3'):
            print('sub(x,n)=',sub(x,n))
        elif(choice=='4'):
            print('mul(x,n)=',mul(x,n))
        elif(choice=='5'):
            print('div(x,n)=',div(x,n))
        else:
            print('operator does not exist')
