In Python, the assert statement is used as a debugging tool to check if a given condition is true. It provides a way to test assumptions and verify that the code behaves as expected. The syntax for the assert statement is as follows:

```python
assert condition, message
```

Here, condition is the expression that needs to evaluate to True. If the condition is False, an AssertionError is raised. The optional message parameter can be used to provide additional information about the assertion.

Let's consider a simple example to demonstrate the usage of the assert statement:

```python
def divide(a, b):
    assert b != 0, "Cannot divide by zero"
    return a / b
```
In this example, the divide function takes two parameters a and b. The assert statement is used to ensure that b is not equal to zero. If b is zero, the assertion fails, and an AssertionError is raised with the specified message. This helps in catching potential issues and preventing unwanted behavior.

Here's an example of how you can use the divide function:

```python
result = divide(10, 5)
print(result)  # Output: 2.0

result = divide(10, 0)
# Raises an AssertionError with the message "Cannot divide by zero"
```

In the second case, where b is zero, the assert statement fails, and an AssertionError is raised with the specified message.

It's important to note that assert statements are typically used during development and debugging, and they can be disabled in production code by using the -O optimization flag when running Python.