BREAD_PRICE = 185 
DISCOUNT_RATE = 0.60 
num_loaves = int (input ("Enter the number of day old loaves: ")) 

 
regular_price = num_loaves * BREAD_PRICE 
discount = regular_price * DISCOUNT_RATE 
total = regular_price - discount 


print ("Regular price: %5.2f" % regular_price) 
print ("Discount: %5.2f" % discount) 
print ("Total:  %5.2f" % total)
