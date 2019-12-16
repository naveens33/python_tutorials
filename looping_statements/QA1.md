# Interview Questions
1. Difference between iterable and iterator
    * Iterable is an object, which one can iterate over. It generates an Iterator when passed to iter() method. 
    * Iterator is an object, which is used to iterate over an iterable object using __next__() method. Iterators have __next__() method, which returns the next item of the object
2. What is iter()
    * The iter() is a method that returns an iterator for the given object
    * In case, the given object is not a iterable it will throw TypeError

3. What is break, continue and pass statement?
    
    |Statement|Definition|
    |---|-----|
    |Break|Allows loop termination when some condition is met and the control is transferred to the next statement.|
    |Continue|Allows skipping some part of a loop when some specific condition is met and the control is transferred to the beginning of the loop|
    |Pass|Used when you need some block of code syntactically, but you want to skip its execution. This is basically a null operation. Nothing happens when this is executed.|
