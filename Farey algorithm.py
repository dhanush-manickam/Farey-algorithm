# farey"s algorithm to approximate a decimal number

# Initializing some variables
# a,b is the first fraction 0/1
# c,d is the second fraction 1/1
a,b,c,d = 0,1,1,1
n = float(input("enter your decimal number between 0-1: "))
precision = len(str(n)) - 2

# loop that calculate the fraction
while round((a/b),precision)!=round(n,precision) or round((c/d),precision)!=round(n,precision):
	# this is the median part
	# e/f is the median of a/b and c/d
	# e/f is always less than c/d 
	e = a + c
	f = b + d
	# if the input decimal is less than e/f the new c/d
	if n < e/f:
		c,d = e,f
	# or else we want to set e/f as the new a/b
	else:
		a,b = e,f
		

# This block of code is specifically to print the fractional approximation of the decimal
if a/b == round(n,precision):
	print(f'This is the fractional approximation of the decimal {a}/{b}')
else:
	print(f'This is the fractional approximation of the decimal {c}/{d}')