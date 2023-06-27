# Interview Questions
1. What is self in Python?
    
   * Self is an current instance or an object of a class. In Python, this is explicitly included as the first parameter.
   * It helps to differentiate between the methods and attributes of a class with local variables.
   * The self variable in the init method refers to the newly created object while in other methods,
   it refers to the object whose method was called.
   
2. Differece between classmethod and staticmethod
   1. class method will take cls as a first parameter where as static method no needed any specific parameter
   2. class method can able to access the class state where as static method cannot access the class state
   3. class method should be annotated/decorated with @classmethod decorator where as static method should be annotated 
      or decorated with @staticmethod decorator 

3. Pickling vs Unpickling
* Pickling: It is a process where a Python object hierarchy is converted into a byte stream.
* Unpickling: It is the inverse of Pickling process where a byte stream is converted into an object hierarchy.
    Module Interface :

            dumps() – This function is called to serialize an object hierarchy.

            loads() – This function is called to de-serialize a data stream.