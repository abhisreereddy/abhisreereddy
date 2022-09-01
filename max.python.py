def maximum(a, b, c):

	if (a >= b) and (a >= c):
		largest = a

	elif (b >= a) and (b >= c):
		largest = b
	else:
		largest = c
		
	return largest
a = 1101
b = 1011
c = 1001
print(maximum(a, b, c))
