# Interview Questions
1. Data types are supported in Python
    * Numbers
    * Strings
    * Lists
    * Tuples
    * Dictionaries
    * Set
2. Immutable built-in types (an immutable object can’t be changed after it is created)
    * Strings
    * Tuples
    * Numbers    
3. Mutable built-in types
    * Lists
    * Dictionaries
    * Set
4. Advantage of Mutable

    Mutable and immutable objects are handled differently in python. 
    Immutable objects are quicker to access and are expensive to change because it involves the creation of a copy.
    Whereas mutable objects are easy to change.
    Use of mutable objects is recommended when there is a need to change the size or content of the object.
5. Difference between lists, tuples, set and dictionaries
    
    |Lists|Tuples|Set|Dictionaries|
    |-----|------|---|------------|
    |List is a collection which is ordered|Collection of items which is ordered|Collection of Unordered and Un indexed items|Key:Value Pair in Python|
    |Lists are mutable (changeable)|Tuples are immutable (unchangeable)|Sets are mutable (changeable)|A dictionary is a collection which is changeable|
    |Brackets used to represent: []|Brackets used to represent: ()|Brackets used to represent: { }|Brackets used to represent: { }|
    |Allows duplicate members|Allows duplicate members|Does not take duplicate Values|Does not take duplicate keys|
    |Lists are like arrays declared in other languages|Tuples are faster than lists as they are immutable|Sets are not faster than lists||
    
6. Key points of Memory Allocation and Management in Python
    * Memory in Python is managed by Python private heap space. All Python objects and data structures are located in a private heap. This private heap is taken care of by Python Interpreter itself, and a programmer doesn’t have access to this private heap.
    * The method and variables are created on stack memory
    * The objects and instance variable are on heap memory
    * A New stack frame is create on invocation of a function/method
    * Stack frame are destroyed as soon as the function/method returns
    * Garbage collector is the mechanism to clean the dead object
    * The algorithm used in python for Garbage collection(GC) is called Reference counting
     
7. Compare memory allocation and management of python and c++/c/c#/java

    | |Python|C/C++/C#/Java|
    |---|---|-----|
    |Statement|a=5|int a=5;|
    |Data type declaration|No need. Dynamically typed|Mandatory. Static type|
    |What is 5?|An object created on heap memory|A primitive data store in 4 bytes or 2 bytes
    |What does a contains?|Reference to Object 5|Memory location where 5 is store|
    |a=a+1|a starts referring a new object whose value is 5|a continues to point to the same memory, with value equal to5|
    |a=5, b=6| Both a and b will refer to same object|a and b are two variables pointing to different memory location|
    
8. What is pass?
    * The pass statement is a null operation. Nothing happens when it executes
    * This statement used if the program requires no action but requires it syntactically
    
9. Type conversion in Python
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
    
10. Difference between Arrays and lists
    * Python does not have built-in support for Arrays, but you can be created by importing array module.
    
    Arrays and lists have the same way of storing data. But, arrays can hold only a single data type elements whereas lists can hold any data type elements.
    
