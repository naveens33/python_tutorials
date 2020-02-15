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