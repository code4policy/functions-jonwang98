def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b

def square(a):
    return a * a

def cube(a):
    return a * a * a

def square_n_times(a, n):
    return square(a) * n

print("I'm going use the calculator functions to divide 5 by 6")
x = divide(5,6)
print(x)

print("I'm going use the calculator functions to square 5 three times and sum the results")
x = square_n_times(5,3)
print(x)