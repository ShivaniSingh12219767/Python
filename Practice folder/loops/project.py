def karatsuba_multiply(num1, num2):
    n = max(len(num1), len(num2))

    # Base case for single-digit multiplication
    if n == 1:
        return str(int(num1) * int(num2))

    # Pad zeros to make the numbers of equal length
    num1 = num1.zfill(n)
    num2 = num2.zfill(n)

    # Split the numbers into two halves
    mid = n // 2
    high1, low1 = num1[:mid], num1[mid:]
    high2, low2 = num2[:mid], num2[mid:]

    # Recursive steps
    z0 = karatsuba_multiply(low1, low2)
    z2 = karatsuba_multiply(high1, high2)
    z1 = karatsuba_multiply(str(int(high1) + int(low1)), str(int(high2) + int(low2)))

    # Intermediate calculations
    p1 = int(z2) * 10**(2 * mid)
    p2 = (int(z1) - int(z2) - int(z0)) * 10**mid

    # Calculate the result
    result = p1 + p2 + int(z0)

    return str(result)


# Define the two 64-digit numbers
num1 = '3141592653589793238462643383279502884197169399375105820974944592'
num2 = '2718281828459045235360287471352662497757247093699959574966967627'

# Calculate the product using the Karatsuba algorithm
product = karatsuba_multiply(num1, num2)

print(product)
