The math module provides a wide range of mathematical functions and constants. To use the math module, you need to import it at the beginning of your Python script or interactive session. Here's an overview of some commonly used functions and constants available in the math module:

## Mathematical Functions

* math.sqrt(x): Returns the square root of x.
* math.pow(x, y): Returns x raised to the power of y.
* math.exp(x): Returns the exponential value of x (e^x).
* math.log(x): Returns the natural logarithm of x (base e).
* math.log10(x): Returns the base 10 logarithm of x.
* math.sin(x), math.cos(x), math.tan(x): Returns the trigonometric sine, cosine, and tangent of x (in radians).
* math.radians(x): Converts the angle x from degrees to radians.
* math.degrees(x): Converts the angle x from radians to degrees.
* math.ceil(x): Returns the smallest integer greater than or equal to x.
* math.floor(x): Returns the largest integer less than or equal to x.
* math.fabs(x): Returns the absolute value of x.
* math.isinf(x): Returns True if x is positive or negative infinity, False otherwise.
* math.isnan(x): Returns True if x is not a number (NaN), False otherwise.

## Mathematical Constants

* math.pi: The mathematical constant π (pi).
* math.e: The mathematical constant e.

Here's an example that demonstrates the usage of some of these functions:
```

# Mathematical Functions
print(math.sqrt(25))           # Output: 5.0
print(math.pow(2, 3))          # Output: 8.0
print(math.exp(2))             # Output: 7.38905609893065
print(math.log(10))            # Output: 2.302585092994046
print(math.log10(100))         # Output: 2.0
print(math.sin(math.pi/2))     # Output: 1.0
print(math.cos(math.pi))       # Output: -1.0
print(math.tan(math.pi/4))     # Output: 0.9999999999999999
print(math.radians(90))        # Output: 1.5707963267948966
print(math.degrees(1.5708))    # Output: 89.95437383553924
print(math.ceil(4.3))          # Output: 5
print(math.floor(4.7))         # Output: 4
print(math.fabs(-4.5))         # Output: 4.5
print(math.isinf(float('inf')))  # Output: True
print(math.isnan(float('nan')))  # Output: True

# Mathematical Constants
print(math.pi)                 # Output: 3.141592653589793
print(math.e)                  # Output: 2.718281828459045
```

These are just a few examples of the functions and constants provided by the math module in Python. The module offers many more functions for mathematical calculations, trigonometry, exponentiation, logarithms, and more. You can refer to the Python documentation for the math module for a comprehensive list of available functions and their descriptions.




