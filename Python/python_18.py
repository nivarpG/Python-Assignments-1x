a)

#print from 1 to 100 
for x in range(1,100):
  print(x)
#print the above in reverse order
for y in range(100,-1,-1):
  print(y)

b)

#program to print in increasing order
i_count = 0
while( i_count < 100):
  i_count+=1
  print(i_count)

#program to print the above in decreasing sequence
d_count = 101
while( d_count > 1):
  d_count-=1
  print(d_count)

c)

#program to print each character seperately in a string

str = "Hello World"
myList = list(str)
for x in myList:
  print(x)

