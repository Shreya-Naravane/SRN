import sys
a=int(sys.argv[1])
b=int(sys.argv[2])
c=int(sys.argv[3])

if (a >= b) and (a >= c):
   largest = a
elif (b >= a) and (b >= c):
   largest = b
else:
   largest = c

print("The largest number is", largest)

