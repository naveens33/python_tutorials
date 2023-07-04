A generator is a special type of iterator that generates a sequence of values on-the-fly. Unlike normal functions that return a value and then terminate, generators use the yield statement to produce a series of values one at a time, suspending their state between each yield. This makes generators efficient for generating large sequences or infinite sequences without consuming excessive memory.

To define a generator, you can use a function that contains one or more yield statements. Here's an example of a generator that generates the Fibonacci sequence:

```python
def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
```

In this example, the fibonacci_generator function uses an infinite loop to generate Fibonacci numbers. It yields the current Fibonacci number (a) and then updates a and b to calculate the next Fibonacci number.

To use the generator, you can iterate over it using a for loop or by calling the next() function. Here are a few examples:

```python
fib_gen = fibonacci_generator()

# Generate and print the first 10 Fibonacci numbers
for _ in range(10):
    print(next(fib_gen))

# Output:
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34
```
In this example, we create an instance of the fibonacci_generator generator and use next() to retrieve the next value from the generator in each iteration of the loop.

Generators provide an elegant way to generate values on-demand and are particularly useful when dealing with large data sets or when you want to avoid loading all the values into memory at once. They can be used in many scenarios, such as processing large files, generating infinite sequences, or performing lazy evaluation.