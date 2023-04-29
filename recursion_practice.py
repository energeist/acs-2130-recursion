# 1 - Compute the factorial of a number N

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print("exercise #1")
print(f"Printing 5!: {factorial(5)}")

# 2 - Computer the sum of natural numbers until N

def natural(n):
    if n == 1:
        return 1
    return n + natural(n-1)

print("exercise #2")
print(natural(5))

# 3 - Write a function for multiply(a,b), where a and b are both positive
# integers, but you can only use the + or - operators

def multiply(a,b):
    if b == 1:
        return a
    else:
        return a + multiply(a,b-1)
    
print("exercise #3")
print(multiply(4,5))
    
# 4 - Write a recursive function that allows raising a float to a positive
# or negative integer power

def raise_to_power(float_num, exponent):
    if exponent < 0:
        return 1/float_num * raise_to_power(float_num, exponent + 1)
    elif exponent > 0 :
        return float_num * raise_to_power(float_num, exponent - 1)
    return 1

print("exercise #4")
print(raise_to_power(3,-1))
print(raise_to_power(3,3))
#5 - Find the Greatest Common Divisor of 2 numbers using recursion

def greatest_common_divisor(a, b):
    if (b != 0):
        return greatest_common_divisor(b, a % b)
    else:
        return a

print("exercise #5")
print(greatest_common_divisor(18,28))
# 6 - Write a recursive function to reverse a string.

string = "cat is running"
def reverse_string(string):
    words = string.split()
    if len(words) == 1:
        return words[0]
    return words[-1] + " " + reverse_string(" ".join(words[:len(words)-1]))

print("exercise #6")
print(reverse_string(string))