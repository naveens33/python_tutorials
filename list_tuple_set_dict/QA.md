# Interview Questions
1. Immutable built-in types (an immutable object can’t be changed after it is created)
    * Strings
    * Tuples
    * Numbers    
2. Mutable built-in types
    * Lists
    * Dictionaries
    * Set
3. Advantage of Mutable

    Mutable and immutable objects are handled differently in python. 
    Immutable objects are quicker to access and are expensive to change because it involves the creation of a copy.
    Whereas mutable objects are easy to change.
    Use of mutable objects is recommended when there is a need to change the size or content of the object.

4. Difference between lists, tuples, set and dictionaries
    
    |Lists|Tuples|Set|Dictionaries|
    |-----|------|---|------------|
    |List is a collection which is ordered|Collection of items which is ordered|Collection of Unordered and Un indexed items|Key:Value Pair in Python|
    |Lists are mutable (changeable)|Tuples are immutable (unchangeable)|Sets are mutable (changeable)|A dictionary is a collection which is changeable|
    |Brackets used to represent: []|Brackets used to represent: ()|Brackets used to represent: { }|Brackets used to represent: { }|
    |Allows duplicate members|Allows duplicate members|Does not take duplicate Values|Does not take duplicate keys|
    |Lists are like arrays declared in other languages|Tuples are faster than lists as they are immutable|Sets are not faster than lists||
    
5. Difference between Arrays and lists
    * Python does not have built-in support for Arrays, but you can be created by importing array module.
    
    Arrays and lists have the same way of storing data. But, arrays can hold only a single data type elements whereas lists can hold any data type elements.
    
6. How to randomize the items in an list?

    Using random module,
    
    ```
    from random import shuffle
    x = [12,34.56,True,"Hello",[1,2,3]]
    shuffle(x)
    print(x)
    ```
7. What is slicing?

    Slicing is a technique that allows us to retrieve only a part of a list, tuple, or string.

8. [::-1} does?

    It will reverse the order of the any iterable object
9. Can a object holds another object in python

     Yes, Everything in Python is an object and some objects can hold other objects, such as lists, tuples, dicts, classes, etc.
10. Difference between iterable and iterator
     * Iterable is an object, which one can iterate over. It generates an Iterator when passed to iter() method.
     * Iterator is an object, which is used to iterate over an iterable object using __next__() method. Iterators have __next__() method, which returns the next item of the object

11. What is iter()
     * The iter() is a method that returns an iterator for the given object
     * In case, the given object is not a iterable it will throw TypeError
12. How to create empty set

    set() function can be used to create sets. Note: to create an empty set you have to use set(), not {};

13. List Sort
14. Set Pop
15. 
16. What are negative indices?

    A negative index starts from right to left and starts with -1

