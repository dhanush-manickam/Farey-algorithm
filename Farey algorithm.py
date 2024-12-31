# Initialize starting fractions
# a/b represents the first fraction (0/1)
# c/d represents the second fraction (1/1)
a, b, c, d = 0, 1, 1, 1

# Take user input for the decimal number to approximate
n = float(input("Enter a decimal number between 0 and 1: "))

# Calculate the required precision based on the length of the decimal input
precision = len(str(n)) - 2  # Subtract 2 to exclude '0.'

# Loop to calculate the fraction that approximates the given decimal
while round((a / b), precision) != round(n, precision) or round((c / d), precision) != round(n, precision):
    # Compute the mediant (e/f) of the fractions a/b and c/d
    e = a + c  # Numerator of the mediant
    f = b + d  # Denominator of the mediant

    # Adjust the fractions based on the input value
    # If n is less than e/f, update c/d to e/f
    if n < e / f:
        c, d = e, f
    # Otherwise, update a/b to e/f
    else:
        a, b = e, f

# Check if the final approximation matches the input value
# Print the fractional approximation
if a / b == round(n, precision):
    print(f'The fractional approximation of the decimal is {a}/{b}')
else:
    print(f'The fractional approximation of the decimal is {c}/{d}')
