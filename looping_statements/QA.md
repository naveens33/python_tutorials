# Interview Questions
1. Difference between iterable and iterator
    * Iterable is an object, which one can iterate over. It generates an Iterator when passed to iter() method. 
    * Iterator is an object, which is used to iterate over an iterable object using __next__() method. Iterators have __next__() method, which returns the next item of the object
2. What is iter()
    * The iter() is a method that returns an iterator for the given object
    * In case, the given object is not a iterable it will throw TypeError
    