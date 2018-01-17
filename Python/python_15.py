a)

myList = ['pravin', 'kumar', 'ramu', 'mithun', 'jaya'];
str = input("Enter a name to check its presence : ")
if(str in myList):
  print(str, "exists in the list")
else:
  print(str, "doesn't exists in the list")
  
b)
# Perform above task without using membership operator.
myList = ['pravin', 'kumar', 'ramu', 'mithun', 'jaya'];
str = input("Enter a name to check its presence : ")
for x in myList:
  if(x == str):
    print(str, " exists in the list")
 

c)

# Print the elements of the list in reverse direction.
myList = ['pravin', 'kumar', 'ramu', 'mithun', 'jaya'];
myList.reverse();
print(myList)

  

