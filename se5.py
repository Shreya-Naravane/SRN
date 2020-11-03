import sys 
marks=float(sys.argv[1])
if(90<marks<100):
	print("DIV 1.")
if(75<marks<90):
	print("DIV 2.")
if(35<marks<75):
	print("DIV 3.")
if(marks<35):
	print("The person is failed.")
