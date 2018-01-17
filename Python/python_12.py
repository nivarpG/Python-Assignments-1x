a=[]
avg=0
for i in range(0,10):
    elem=int(input("Enter element: "))
    a.append(elem)

#finding an average
avg=sum(a)/10

#print average
print(avg)

for i in range(0,10):
 #print Number Lesser than average
  if(a[i] < avg):
    print(a[i])

#print Number greater than average 
  elif(a[i] > avg):
    print(a[i])

#print Number equal to average 
  elif(a[i] == avg):
    print(a[i])
