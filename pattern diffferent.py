n=input("enter the character to be printerd=")
r=int(input("Max number of time to be printed="))
if(r<=0):
	print("invalid")
	exit()
else:
	for i in range(0,r):
		for j in range(0,i+1):
			print(n,end=" ")
		print()
