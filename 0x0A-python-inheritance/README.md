# 0x0A. Python - Inheritance
## Resources :books:

* [Inheritance](https://intranet.hbtn.io/rltoken/E2Bs3bxX8GuSEKuWqswU7g)
* [Multiple inheritance](https://intranet.hbtn.io/rltoken/auwnZOKkBZ97JaLtrMryuA)
* [Inheritance in Python](https://intranet.hbtn.io/rltoken/ycewwwPmDpXqRp2R1FW51w)
* [Learn to Program 10 : Inheritance Magic Methods](https://intranet.hbtn.io/rltoken/F8LUzmvPI4yur1Z37ZM1fQ)

## Learning Objectives :bulb:
* Why Python programming is awesome (don’t forget to tweet today, with the hashtag #pythoniscool :))
* What is a superclass, baseclass or parentclass
* What is a subclass
* How to list all attributes and methods of a class or instance
* When can an instance have new attributes
* How to inherit class from another
* How to define a class with multiple base classes
* What is the default class every class inherit from
* How to override a method or attribute inherited from the base class
* Which attributes or methods are available by heritage to subclasses
* What is the purpose of inheritance
* What are, when and how to use isinstance, issubclass, type and super built-in functions

## Requirements :white_check_mark:

### Python Scripts
* Allowed editors: vi, vim, emacs
* All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
* All your files should end with a new line
* The first line of all your files should be exactly #!/usr/bin/python3
* A README.md file, at the root of the folder of the project, is mandatory
* Your code should use the PEP 8 style (version 1.7.*)
* All your files must be executable
* The length of your files will be tested using wc
### Python Test Cases
* Allowed editors: vi, vim, emacs
* All your files should end with a new line
* All your test files should be inside a folder tests
* All your test files should be text files (extension: .txt)
* All your tests should be executed by using this command: python3 -m doctest ./tests/*
* All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
* All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
* All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
* We strongly encourage you to work together on test cases, so that you don’t miss any edge case

## Tasks :page_with_curl:
### Mandatory
- [x] **[0. Lookup](./0-lookup.py)** - Write a function that returns the list of available attributes and methods of an object
- [x] **[1. My list](./1-my_list.py)** - Write a class MyList that inherits from list
- [x] **[2. Exact same object](./2-is_same_class.py)** - Write a function that returns True if the object is exactly an instance of the specified class ; otherwise False.
- [x] **[3. Same class or inherit from](./3-is_kind_of_class.py)** - Write a function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise False.
- [x] **[4. Only sub class of](./4-inherits_from.py)** - Write a function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False.
- [x] **[5. Geometry module](./5-base_geometry.py)** - Write an empty class BaseGeometry.
- [x] **[6. Improve Geometry](./6-base_geometry.py)** - Write a class BaseGeometry (based on 5-base_geometry.py).
- [x] **[7. Integer validator](./7-base_geometry.py)** - Write a class BaseGeometry (based on 6-base_geometry.py).
- [x] **[8. Rectangle](./8-rectangle.py)** - Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py).
- [x] **[9. Full rectangle](./9-rectangle.py)** - Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py). (task based on 8-rectangle.py)
- [x] **[10. Square #1](./10-square.py)** - Write a class Square that inherits from Rectangle (9-rectangle.py)
- [x] **[11. Square #2](./11-square.py)** - Write a class Square that inherits from Rectangle (9-rectangle.py). (task based on 10-square.py).
### Advance :muscle:
- [x] **[12. My integer](./100-my_int.py)** - Write a class MyInt that inherits from int
- [x] **[13. Can I?](./101-add_attribute.py)** - Write a function that adds a new attribute to an object if it’s possible

## Author :pencil:
**Santiago Peña Mosquera** - twitter [@Santiag11470161](https://twitter.com/Santiag11470161) - LinkedIn [Santiago Peña Mosquera](https://www.linkedin.com/in/santiago-pe%C3%B1a-mosquera-abaa20196/)
