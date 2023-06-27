In Python, you can use various types of loops to repeatedly execute a block of code. The most commonly used loops are the for loop and the while loop. Here's a brief explanation of each:

## for loop
The for loop is used to iterate over a sequence (such as a list, tuple, string, or range) or any iterable object. It executes a block of code for each item in the sequence. Here's the basic syntax of a for loop:

```
for item in sequence:
    # code to be executed for each item
```

Here's an example that prints each item in a list:

```
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
```

## while loop
The while loop repeatedly executes a block of code as long as a specified condition is true. It's useful when you want to loop until a certain condition is met. Here's the basic syntax of a while loop:
```
while condition:
    # code to be executed as long as the condition is true
```    
Here's an example that counts from 1 to 5 using a while loop:

```
count = 1

while count <= 5:
    print(count)
    count += 1
```

## Loop Control Statements:
Python also provides loop control statements that allow you to control the flow of a loop. These statements include break, continue, and else.
* break: It terminates the loop prematurely and moves the execution to the next statement outside the loop.
* continue: It skips the rest of the current iteration and moves to the next iteration.
* else: It is executed when the loop condition becomes false, but not if the loop is terminated by a break statement.
Here's an example that demonstrates the usage of loop control statements:

```
fruits = ["apple", "banana", "cherry", "date"]

for fruit in fruits:
    if fruit == "banana":
        continue  # Skip the current iteration when the fruit is "banana"
    elif fruit == "date":
        break  # Terminate the loop when the fruit is "date"
    print(fruit)
else:
    print("All fruits have been iterated.")
```
This example will print "apple" and "cherry" but not "banana" because of the continue statement. The loop will be terminated when the fruit is "date" because of the break statement. The else block will be executed if the loop completes without encountering a break statement.

These are the basic looping constructs in Python. They allow you to repeat code execution until a condition is met or for a specified number of iterations.

## do while loop
Python does not have a built-in do-while loop like some other programming languages. However, you can achieve similar functionality using a while loop with a conditional check placed at the end of the loop body. This way, the loop body is always executed at least once before checking the condition. Here's an example:

```
while True:
    # code to be executed
    # ...
    # condition check
    if condition:
        break
```
In this example, the loop is initially set to run indefinitely with while True. The code inside the loop is executed, and then the condition is checked. If the condition evaluates to True, the loop is terminated using the break statement.

Here's a specific example that emulates a do-while loop, where a user is prompted to enter a positive number:

```
while True:
    number = int(input("Enter a positive number: "))
    if number > 0:
        break
    else:
        print("Invalid input. Try again.")

print("You entered a positive number:", number)
```
In this example, the code inside the loop asks the user to enter a positive number. The loop will continue until the user enters a positive number (condition number > 0) and then breaks out of the loop. If the user enters a non-positive number, an error message is displayed, and the loop continues.

By using the while True loop structure and appropriate conditional checks, you can achieve the behavior of a do-while loop in Python.