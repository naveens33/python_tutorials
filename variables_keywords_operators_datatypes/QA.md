# Interview Questions
1. Data types are supported in Python
    * Numbers
    * Strings
    * Lists
    * Tuples
    * Dictionaries
    * Set

2. Key points of Memory Allocation and Management in Python
    * Memory in Python is managed by Python private heap space. All Python objects and data structures are located in a private heap. This private heap is taken care of by Python Interpreter itself, and a programmer doesn’t have access to this private heap.
    * The method and variables are created on stack memory
    * The objects and instance variable are on heap memory
    * A New stack frame is create on invocation of a function/method
    * Stack frame are destroyed as soon as the function/method returns
    * Garbage collector is the mechanism to clean the dead object
    * The algorithm used in python for Garbage collection(GC) is called Reference counting
     
3. Compare memory allocation and management of python and c++/c/c#/java

    | |Python|C/C++/C#/Java|
    |---|---|-----|
    |Statement|a=5|int a=5;|
    |Data type declaration|No need. Dynamically typed|Mandatory. Static type|
    |What is 5?|An object created on heap memory|A primitive data store in 4 bytes or 2 bytes
    |What does a contains?|Reference to Object 5|Memory location where 5 is store|
    |a=a+1|a starts referring a new object whose value is 6|a continues to point to the same memory, with value equal to 6|
    |a=6, b=6| Both a and b will refer to same object|a and b are two variables pointing to different memory location|
    
4. What is pass?
    * The pass statement is a null operation. Nothing happens when it executes
    * This statement used if the program requires no action but requires it syntactically
    
5. Type conversion in Python
    * int() – converts any data type into integer type
    * float() – converts any data type into float type
    * ord() – converts characters into integer
    * hex() – converts integers to hexadecimal
    * oct() – converts integer to octal
    * tuple() – This function is used to convert to a tuple.
    * set() – This function returns the type after converting to set.
    * list() – This function is used to convert any data type to a list type.
    * dict() – This function is used to convert a tuple of order (key,value) into a dictionary.
    * str() – Used to convert integer into a string.
    * complex(real,imag) – This functionconverts real numbers to complex(real,imag) number.

6. What is PyMalloc?

    To speed-up memory operations and reduce fragmentation Python uses a special manager on top of the general-purpose allocator, called PyMalloc.

7. is not in operator

    is: returns true when 2 operands are true  (Example: “a” is ‘a’)

    not: returns the inverse of the boolean value

    in: checks if some element is present in some sequence

8. Types - Mutable and Immutable

   |Class|Description|Immutable(Cannot be changed)|
   |-----|-----------|---------|
   |bool|Boolean Value|yes|
   |int|Integer|yes|
   |float|Float|yes|
   |list|mutable sequence of objects|no|
   |tuple|immutable sequence of objects|yes|
   |str|string|yes|
   |set|unordered set of distinct object|no|
   |frozenset|immutable from of set class|yes|
   |dict|dictionary|no|

   https://medium.com/@meghamohan/mutable-and-immutable-side-of-python-c2145cf72747