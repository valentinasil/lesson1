# The following is a list of dogs currently at Doggie Daycare
dogs = ['Skye','Mabel','Lassie','Buttercup']

# Do not change any of the code above this line!

# Write a line of below to print out the list of dogs currently at daycare
print(dogs)



# The following dogs have just arrived to daycare, programatically add each of them to the list of dogs at daycare
# Widget, Balto, Chloe
# When you are done adding all three dogs, print out the list of dogs currently at daycare
dogs.append('Widget')
dogs.append('Balto')
dogs.append('Chloe')
print(dogs)







# Sort the dogs alphabetically
# When you are done print out the list of dogs currently at daycare

dogs.sort()
print(dogs)



# Programatcially print out a list of the first three dogs.
print(dogs[:3])




# Mabel and Buttercup have been picked up by there owners, so they are no longer at doggie daycare
# Write some lines of code removing both from the list
# When you are done print out the list of dogs currently at daycare
dogs.remove('Mabel')
dogs.remove('Buttercup')
print(dogs)
