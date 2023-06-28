Inheritance is a fundamental concept in object-oriented programming that allows a class to inherit attributes and methods from another class. In Python, inheritance is achieved by creating a subclass that extends a base class. The subclass, also known as the derived class, inherits all the attributes and methods of the base class. There are several types of inheritance that you can utilize based on your specific requirements. The common types of inheritance are:

## Single Inheritance:
Single inheritance involves inheriting attributes and methods from a single base class. A subclass extends the functionality of a single superclass.

```python
class ParentClass:
    pass

class ChildClass(ParentClass):
    pass
```
## Multiple Inheritance:
Multiple inheritance allows a subclass to inherit attributes and methods from multiple base classes. The subclass incorporates the features of multiple parent classes.

```python
class ParentClass1:
    pass

class ParentClass2:
    pass

class ChildClass(ParentClass1, ParentClass2):
    pass
```
## Multilevel Inheritance:
Multilevel inheritance involves a chain of inheritance where a subclass inherits from a derived class, which itself inherits from another class. It forms a hierarchy of classes.

```python
class GrandparentClass:
    pass

class ParentClass(GrandparentClass):
    pass

class ChildClass(ParentClass):
    pass
```
## Hierarchical Inheritance:
Hierarchical inheritance occurs when multiple subclasses inherit from a single superclass. It allows the creation of a class hierarchy where one base class serves as a parent for multiple child classes.

```python
class ParentClass:
    pass

class ChildClass1(ParentClass):
    pass

class ChildClass2(ParentClass):
    pass
```
## Hybrid Inheritance:
Hybrid inheritance combines multiple types of inheritance, such as single, multiple, multilevel, or hierarchical inheritance, to create a complex class hierarchy.

```python
class ParentClass1:
    pass

class ParentClass2:
    pass

class ChildClass(ParentClass1, ParentClass2):
    pass
```    
Each type of inheritance provides flexibility in structuring classes and enables code reuse by inheriting attributes and methods from existing classes. It is essential to choose the appropriate type of inheritance based on the relationships between classes and the desired behavior of the program.

## super()

The super() function is used to refer to the superclass or parent class within a derived class. It allows you to access and call methods or attributes of the superclass from the subclass. Here's an example that demonstrates the use of super() with a Student class:

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

student = Student("Alice", 12345)
student.display_info()
```
In this example, we have a base class Person and a derived class Student that inherits from Person. Both classes have an __init__() method and a display_info() method.

Inside the Student class, the __init__() method is overridden to add an additional attribute student_id. The super().__init__(name) line is used to call the __init__() method of the parent class, Person, and pass the name argument to initialize the name attribute of the Person class.

Similarly, the display_info() method is overridden in the Student class to add the student ID. The super().display_info() line is used to call the display_info() method of the parent class, Person, and display the person's name.

When we create an instance of the Student class with the name "Alice" and student ID 12345, and then call the display_info() method, it first calls the display_info() method of the parent class, which displays the name "Alice". Then, the display_info() method of the Student class displays the student ID.

The super() function enables you to leverage the functionality of the parent class within the derived class, allowing for code reuse and customization of behavior in the subclass.