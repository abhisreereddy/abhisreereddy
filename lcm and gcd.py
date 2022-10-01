a=int(input("Enter First Number: "))
b=int(input("Enter Second Number: "))
for i in range(1,a+1):
    if(a%i==0 and b%i==0):
        gcd=i
print("GCD of %d and %d is %d"%(a,b,gcd))
lcm=(a*b)/gcd
print("LCM of %d and %d is %d"%(a,b,lcm))



#three numbers
a=int(input("Enter First Number: "))
b=int(input("Enter Second Number: "))
c=int(input("Enter Third Number: "))
for i in range(1,a+1):
    if(a%i==0 and b%i==0 and c%i==0):
        gcd=i
print("GCD of %d, %d and %d is %d"%(a,b,c,gcd))
lcm=(a*b*c)/gcd
print("LCM of %d, %d and %d is %d"%(a,b,c,lcm))
