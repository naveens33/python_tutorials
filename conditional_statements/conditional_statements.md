Conditional statements in Python allow you to control the flow of your program based on certain conditions. There are several types of conditional statements in Python, including the if statement, the if-else statement, and the if-elif-else statement. Here's a brief explanation of each:

## if statement
The if statement is used to execute a block of code only if a specified condition is true. It has the following syntax:

```
if condition:
    # code to be executed if the condition is true
```

Here's an example:

```
x = 5
if x > 0:
    print("x is positive")
```

## if-else statement
The if-else statement allows you to execute one block of code if a condition is true, and another block of code if the condition is false. It has the following syntax:
```
if condition:
    # code to be executed if the condition is true
else:
    # code to be executed if the condition is false
```
Here's an example:

```
x = 5
if x % 2 == 0:
    print("x is even")
else:
    print("x is odd")
```

## if-elif-else statement
The if-elif-else statement is used when you have multiple conditions to check. It allows you to specify multiple conditions and execute different blocks of code based on the first condition that evaluates to true. It has the following syntax:

```
if condition1:
    # code to be executed if condition1 is true
elif condition2:
    # code to be executed if condition2 is true
else:
    # code to be executed if all conditions are false
```
Here's an example:

```
x = 5
if x > 0:
    print("x is positive")
elif x < 0:
    print("x is negative")
else:
    print("x is zero")
```

These are the basic conditional statements in Python. They allow you to make decisions and control the flow of your program based on different conditions.


## Implement Switch Statements with the match and case Keywords in Python 3.10

```
match term:
    case pattern-1:
         action-1
    case pattern-2:
         action-2
    case pattern-3:
         action-3
    case _:
        action-default
```

Example:
```
lang = input("What's the programming language you want to learn? ")
match lang:
    case "JavaScript":
        print("You can become a web developer.")
    case "Python":
        print("You can become a Data Scientist")
    case "PHP":
        print("You can become a backend developer")
    case "Solidity":
        print("You can become a Blockchain developer")
    case "Java":
        print("You can become a mobile app developer")
    case _:
        print("The language doesn't matter, what matters is solving problems.")
```

Note that the underscore symbol is what you use to define a default case for the switch statement in Python.