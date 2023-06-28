## Classes and Objects 

A class is a blueprint or a template that defines the properties (attributes) and behaviors (methods) that objects of that class will have. It encapsulates the common characteristics and functionalities that a group of objects share.

In Python, you define a class using the class keyword. Here's an example of a Student class:

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
```

In the above code, the Student class has two attributes: name and age. It also has a method called display_details() that prints the name and age of the student.

An object, also known as an instance, is created from a class. It represents a specific entity with its own unique set of attribute values. Objects have access to the attributes and methods defined in the class.

To create an object of the Student class and use its attributes and methods, you can do the following:

```python

# Creating objects
student1 = Student("Alice", 20)
student2 = Student("Bob", 21)

# Accessing attributes
print(student1.name)  # Output: Alice
print(student2.age)   # Output: 21

# Calling methods
student1.display_details()  # Output: Name: Alice\nAge: 20
student2.display_details()  # Output: Name: Bob\nAge: 21
```
In the code above, we create two Student objects: student1 and student2. We pass the name and age as arguments to the class's __init__ method during object creation, which initializes the object's attributes. We can then access the attributes using dot notation (object.attribute_name).

We also call the display_details() method on each object, which prints the student's name and age.

Each object created from the Student class is independent and maintains its own state. The self parameter in the class methods refers to the specific instance of the object being accessed, allowing us to access and manipulate the object's attributes and methods.

By creating multiple objects from the same class, we can represent different students, each with their own unique name and age. The class acts as a template, and the objects are the instances that embody the characteristics defined in the class.

## Different types of method in class
different types of methods can be defined to perform various tasks and provide different functionalities. Here are the common types of methods in a class:

* Instance Methods:

Instance methods operate on the instance of the class and can access instance attributes and other methods. These methods are defined without any special decorators and typically have the self parameter as the first parameter.

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

student1 = Student("Alice", 20)
student1.display_details()
# Output:
# Name: Alice
# Age: 20
```
In the Student class, the __init__ method is the constructor that initializes the name and age attributes of the instance. The display_details method is an instance method that prints the student's name and age.

* Class Methods:

Class methods operate on the class itself and have access to class attributes. They are defined using the @classmethod decorator and typically have the cls parameter as the first parameter.

```python
class Student:
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.increment_count()

    @classmethod
    def increment_count(cls):
        cls.count += 1

student1 = Student("Alice", 20)
student2 = Student("Bob", 21)

print(Student.count)  # Output: 2
```
In the Student class, the increment_count method is a class method that increments the count attribute, keeping track of the number of students created. The __init__ method is an instance method that calls the increment_count class method when a new student is created.

* Static Methods:

Static methods are self-contained methods that don't operate on instance or class attributes. They are defined using the @staticmethod decorator.

```python
class Student:
    @staticmethod
    def is_adult(age):
        return age >= 18

result = Student.is_adult(20)
print(result)  # Output: True
```
In the Student class, the is_adult method is a static method that takes an age as a parameter and determines if the student is an adult. Since the method doesn't require any instance-specific or class-specific data, it can be defined as a static method.