Polymorphism is a fundamental concept in object-oriented programming that allows objects of different classes to be treated as objects of a common superclass. In Python, polymorphism is achieved through method overriding and method overloading.

## Method Overriding:
Method overriding occurs when a subclass provides its own implementation of a method that is already defined in its superclass. The overridden method in the subclass is called instead of the superclass's method when invoked on an object of the subclass.

### Example:
```python
class Person:
    def __init__(self, name):
        self.name = name

    def display_info(self):
        print(f"Name: {self.name}")

class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id

    def display_info(self):
        super().display_info()
        print(f"Student ID: {self.student_id}")

person = Person("Alice")
person.display_info()   # Output: Name: Alice

student = Student("Bob", 12345)
student.display_info()
# Output:
# Name: Bob
# Student ID: 12345
```
In the above code, we have a base class Person and a derived class Student that inherits from Person. Both classes have a method named display_info(), but the Student class overrides the method with its own implementation.

The Person class has an __init__() method to initialize the name attribute and a display_info() method to display the person's name.

The Student class extends Person and adds an additional attribute student_id. It overrides the display_info() method to first call the parent class's display_info() method using the super() function and then displays the student's ID.

When we create an instance of the Person class and call the display_info() method, it only displays the person's name.

When we create an instance of the Student class and call the display_info() method, it first calls the parent class's display_info() method to display the person's name and then displays the student's ID.

This is an example of method overriding, where the derived class provides its own implementation of a method that is already defined in the base class, allowing objects of the derived class to exhibit different behavior when the method is called.

## Method Overloading:
Method overloading refers to defining multiple methods with the same name but different parameters in a class. However, unlike some other programming languages, Python does not support method overloading based on the number or types of parameters. Instead, you can achieve a similar effect using default parameter values or variable-length argument lists.

### Example:

```python
class CalculateArea:
    def area(self,x,y=None):
        if y ==None:
            print(3.14*x*x)
        else:
            print(x*y)


if __name__=='__main__':
    c=CalculateArea()
    c.area(5)
    c.area(5,8)
```

In the CalculateArea class, there is a single method named area() that can be called with different numbers of parameters. The method determines whether the second parameter y is provided or not.

If the second parameter y is not provided (i.e., y is None), the method assumes that the calculation is for the area of a circle and calculates the area using the formula 3.14 * x * x, where x is the radius. The result is then printed.

If the second parameter y is provided, the method assumes that the calculation is for the area of a rectangle and calculates the area using the formula x * y, where x and y are the lengths of the sides. The result is then printed.

In the main section, an instance of the CalculateArea class is created with c = CalculateArea(). Then, the area() method is called twice with different sets of arguments.

First, c.area(5) is called with a single argument, which invokes the area() method with x = 5 and y = None. As y is None, the method calculates the area of a circle with radius x (5) using the formula 3.14 * x * x. The result, which is the area of the circle, is printed.

Next, c.area(5, 8) is called with two arguments, which invokes the area() method with x = 5 and y = 8. As y is provided, the method calculates the area of a rectangle with sides of length x (5) and y (8) using the formula x * y. The result, which is the area of the rectangle, is printed.

Overall, this program demonstrates the concept of method overloading by allowing a single method to be called with different numbers of parameters, resulting in different behaviors and calculations based on the provided arguments.