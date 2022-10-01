random_list = [1,2,8,3,2,2,2,5,1]
frequency = {}

# iterating over the list
for item in random_list:
   # checking the element in dictionary
   if item in frequency:
      # incrementing the counr
      frequency[item] += 1
   else:
      # initializing the count
      frequency[item] = 1

# printing the frequency
print(frequency)
