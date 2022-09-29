try:
	n=float(input("enter a numbers="))
	sn=n*n
	cn=n*n*n
	print("square number=",sn)
	print("cube number=",cn)
except ValueError:
	print("invalid")
