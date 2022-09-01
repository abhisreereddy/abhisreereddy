#Python program to calculate simple interest

P = float(input("Enter the principal amount : "))

N = float(input("Enter the number of years : "))

R = float(input("Enter the rate of interest : "))

#calculate simple interest by using this formula
SI = (P * N * R)/100

#print
print("Simple interest : {}".format(SI))
