print("Enter the principal amount:")
p=int(input())

print("Enter the number of years:")
t=float(input())
print("Is the customer is senior citizen :(Y/N)")
ch=(input())
if(ch=="Y" or ch=="n"):
    r=10
else:
    r=12

SI=(p*t*r)/100
print("simple intrest:",SI)
