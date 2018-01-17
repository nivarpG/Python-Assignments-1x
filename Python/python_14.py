listA = ['101','102','103','104','105','106','107','108','109','110'];
listB = ['pravin', 'kumar', 'nivarp','ramu', 'jidesh', 'karthick', 'jaya', 'madhan', 'balu' , 'kavin' ];

# Print all names on to screen
print(listB)

# Read the index from the user and print the corresponding name from both list.

index = int(input("Please enter the index: "))
print(listA[index] + "--" + listB[index])

# Print the names from 4th position to 9th position

print(listA[4] + "," + listB[9])

# Print all names from 3rd position till end of the list
print(listB[3:9])

# Repeat list elements by specified number of times ( N- times, where N is entered by user)
n = int(input("Please enter a number"))
print(listB[1] * n)

# Concatenate two lists and print the output.
print(listA + listB)

# Print element of list A and B side by side.( i.e. List-A First element , List-B First element )
for x in range(0,10):
  print(listA[x] + "-->" + listB[x])
