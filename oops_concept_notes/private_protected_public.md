In Python, there is no strict enforcement of access modifiers like private, protected, or public as in some other programming languages. However, there are naming conventions and attributes that provide a way to achieve similar functionality. Let's discuss each of these access levels:

* Private members

  By convention, private members in Python are prefixed with a double underscore (__). These members are intended to be accessed only within the class itself and are not meant to be accessed directly from outside the class. However, they can still be accessed using name mangling.
* Protected members 

  By convention, protected members in Python are prefixed with a single underscore (_). These members are intended to be accessed within the class itself and its subclasses. However, they can still be accessed from outside the class.
* Public members 

  Public members in Python have no special prefixes. They are accessible from anywhere, both inside and outside the class.

```python
class Student:
    def __init__(self, name, roll_number):
        self.name = name               # Public attribute
        self._roll_number = roll_number   # Protected attribute
        self.__grade = 'A'             # Private attribute

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Roll Number: {self._roll_number}")
        print(f"Grade: {self.__grade}")

    def __calculate_percentage(self):   # Private method
        return 85.5

student = Student("Alice", 12345)

print(student.name)                  # Output: Alice
print(student._roll_number)          # Output: 12345
print(student.__grade)               # Output: AttributeError: 'Student' object has no attribute '__grade'

student.display_info()
# Output:
# Name: Alice
# Roll Number: 12345
# Grade: A

print(student.__calculate_percentage())    # Output: AttributeError: 'Student' object has no attribute '__calculate_percentage'
```
In this example, the Student class has three attributes: name, _roll_number, and __grade. The name attribute is public, _roll_number is protected (indicated by a single underscore prefix), and __grade is private (indicated by a double underscore prefix).

The display_info() method is a public method that displays the values of all the attributes. It can access all the attributes, including the private attribute __grade.

The __calculate_percentage() method is a private method that calculates and returns the percentage of the student. It can only be accessed within the class and raises an AttributeError when called from outside the class.

Outside the class, we can access the public and protected attributes (name and _roll_number) using the dot notation. However, accessing the private attribute (__grade) directly raises an AttributeError.

Calling the public method display_info() provides information about all the attributes.

Attempting to call the private method __calculate_percentage() from outside the class raises an AttributeError since private methods are not accessible outside the class.

Remember that the use of underscores as prefixes (_ and __) indicates the intended level of accessibility and follows naming conventions, but it does not enforce strict access control like in some other programming languages.