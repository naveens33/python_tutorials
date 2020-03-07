### Component of functions

* Keyword def marks the start of function header.
* A function name to uniquely identify it. Function naming follows the same rules of writing identifiers in Python.
* Parameters (arguments) through which we pass values to a function. They are optional.
* A colon (:) to mark the end of function header.
* Optional documentation string (docstring) to describe what the function does.
* One or more valid python statements that make up the function body. Statements must have same indentation level (usually 4 spaces).
* An optional return statement to return a value from the function.

### Type of functions

* Built-in functions - Functions that are built into Python.
* User-defined functions - Functions defined by the users themselves.

### Pass by Reference or pass by value?
One important thing to note is, in Python every variable name is a reference. When we pass a variable to a function, a new reference to the object is created. Parameter passing in Python is same as reference passing in Java.

### Default arguments:
A default argument is a parameter that assumes a default value if a value is not provided in the function call for that argument.The following example illustrates Default arguments.

### Keyword arguments:
The idea is to allow caller to specify argument name with values so that caller does not need to remember order of parameters.

### *args **kwargs 

*args

The special syntax *args in function definitions in python is used to pass a variable number of arguments to a function

**kwargs

The special syntax **kwargs in function definitions in python is used to pass a keyworded, variable-length argument list. We use the name kwargs with the double star. The reason is because the double star allows us to pass through keyword arguments (and any number of them).

### Additional properties of the function

* Function can be assigned to a variable i.e they can be referenced.
* Function can be passed as an argument to another function.
* Function can be returned from a function.

### Build-In functions
|Function|Description|
|--------|-----------|
|all()	Returns True if all items in an iterable object are true
|any()	Returns True if any item in an iterable object is true
|ascii()	Returns a readable version of an object. Replaces none-ascii characters with escape character
|bin()	Returns the binary version of a number
|bool()	Returns the boolean value of the specified object
|bytearray()	Returns an array of bytes
|bytes()	Returns a bytes object
|callable()	Returns True if the specified object is callable, otherwise False
|chr()	Returns a character from the specified Unicode code.
|classmethod()	Converts a method into a class method
|compile()	Returns the specified source as an object, ready to be executed
|complex()	Returns a complex number
|delattr()	Deletes the specified attribute (property or method) from the specified object
|dict()	Returns a dictionary (Array)
|dir()	Returns a list of the specified object's properties and methods
|divmod()	Returns the quotient and the remainder when argument1 is divided by argument2
|enumerate()	Takes a collection (e.g. a tuple) and returns it as an enumerate object
|eval()	Evaluates and executes an expression
|exec()	Executes the specified code (or object)
|filter()	Use a filter function to exclude items in an iterable object
|float()	Returns a floating point number
|format()	Formats a specified value
|frozenset()	Returns a frozenset object
|getattr()	Returns the value of the specified attribute (property or method)
|globals()	Returns the current global symbol table as a dictionary
|hasattr()	Returns True if the specified object has the specified attribute (property/method)
|hash()	Returns the hash value of a specified object
|help()	Executes the built-in help system
|hex()	Converts a number into a hexadecimal value
|id()	Returns the id of an object
|input()	Allowing user input
|int()	Returns an integer number
|isinstance()	Returns True if a specified object is an instance of a specified object
|issubclass()	Returns True if a specified class is a subclass of a specified object
|iter()	Returns an iterator object
|len()	Returns the length of an object
|list()	Returns a list
|locals()	Returns an updated dictionary of the current local symbol table
|map()	Returns the specified iterator with the specified function applied to each item
|max()	Returns the largest item in an iterable
|memoryview()	Returns a memory view object
|min()	Returns the smallest item in an iterable
|next()	Returns the next item in an iterable
|object()	Returns a new object
|oct()	Converts a number into an octal
|open()	Opens a file and returns a file object
|ord()	Convert an integer representing the Unicode of the specified character
|pow()	Returns the value of x to the power of y
|print()	Prints to the standard output device
|property()	Gets, sets, deletes a property
|range()	Returns a sequence of numbers, starting from 0 and increments by 1 (by default)
|repr()	Returns a readable version of an object
|reversed()	Returns a reversed iterator
|round()	Rounds a numbers
|set()	Returns a new set object
|setattr()	Sets an attribute (property/method) of an object
slice()	Returns a slice object
sorted()	Returns a sorted list
@staticmethod()	Converts a method into a static method
str()	Returns a string object
sum()	Sums the items of an iterator
super()	Returns an object that represents the parent class
tuple()	Returns a tuple
type()	Returns the type of an object
vars()	Returns the __dict__ property of an object
zip()	Returns an iterator, from two or more iterators

https://docs.python.org/3/library/functions.html#enumerate

