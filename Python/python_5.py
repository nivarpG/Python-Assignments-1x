a)

#program to print command line argument
#the Python sys module provides access to any command-line arguments via the sys.argv
import sys
#sys.argv is the list of command line arguments
print 'Argument List:' , str(sys.argv)

b)

#program to print biggest of three numbers via command line arguments
import sys

num1 = int(sys.argv[1]) 
num2 = int(sys.argv[2])
num3 = int(sys.argv[3])

 
if (num1 > num2) and (num1 > num3):
   biggest = num1
elif (num2 > num1) and (num2 > num3):
   biggest = num2
else:
   biggest = num3
 
print("The biggest number is",biggest)
  
