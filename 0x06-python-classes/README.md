# 0x06. Python - Classes and Objects
## Resources :books:

* [Object Oriented Programming](https://intranet.hbtn.io/rltoken/izl1kO1isRJo6h_Ce2pmhw)
* [Object-Oriented Programming](https://intranet.hbtn.io/rltoken/K5t1QFchQYs7rkt62uMo7A)
* [Properties vs. Getters and Setters](https://intranet.hbtn.io/rltoken/LZg7XYGGZj49Gu2276afpA)
* [Learn to Program 9 : Object Oriented Programming](https://intranet.hbtn.io/rltoken/aFk7Ki8TPw5vZZBx2JXvIQ)
* [Python Classes and Objects](https://intranet.hbtn.io/rltoken/CFTUXsxbTVu4xb698_2bmQ)
* [Object Oriented Programming](https://intranet.hbtn.io/rltoken/DK1vkIQ0xT1fmMrmBcSGiA)

## Learning Objectives :bulb:
* Why Python programming is awesome (don’t forget to tweet today, with the hashtag #pythoniscool :))
* What is OOP
* “first-class everything”
* What is a class
* What is an object and an instance
* What is the difference between a class and an object or instance
* What is an attribute
* What are and how to use public, protected and private attributes
* What is self
* What is a method
* What is the special __init__ method and how to use it
* What is Data Abstraction, Data Encapsulation, and Information Hiding
* What is a property
* What is the difference between an attribute and a property in Python
* What is the Pythonic way to write getters and setters in Python
* How to dynamically create arbitrary new attributes for existing instances of a class
* How to bind attributes to object and classes
* What is and what does contain __dict__ of a class and of an instance of a class
* How does Python find the attributes of an object or class
* How to use the getattr function

## Requirements :white_check_mark:

* Allowed editors: vi, vim, emacs
* All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
* All your files should end with a new line
* The first line of all your files should be exactly #!/usr/bin/python3
* A README.md file, at the root of the folder of the project, is mandatory
* Your code should use the PEP 8 style (version 1.7.*)
* All your files must be executable
* The length of your files will be tested using wc
* All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
* All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
* All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')

## Tasks :page_with_curl:
### Mandatory
- [x] **[0. My first square](./0-square.py)** - Write an empty class Square that defines a square
- [x] **[1. Square with size](./1-square.py)** - Write a class Square that defines a square (based on 0-square.py)
- [x] **[2. Size validation](./2-square.py)** - Write a class Square that defines a square (based on 1-square.py)
- [x] **[3. Area of a square](./3-square.py)** - Write a class Square that defines a square (based on 2-square.py)
- [x] **[4. Access and update private attribute](./4-square.py)** - Write a class Square that defines a square (based on 3-square.py)
- [x] **[5. Printing a square](./5-square.py)** - Write a class Square that defines a square (based on 4-square.py)
- [x] **[6. Coordinates of a square](./6-square.py)** - Write a class Square that defines a square (based on 5-square.py)
### Advance :muscle:
- [x] **[7. Singly linked list](./100-singly_linked_list.py)** - Write a class Node that defines a node of a singly linked list
- [x] **[8. Print Square instance](./101-square.py)** - Write a class Square that defines a square (based on 6-square.py)
- [x] **[9. Compare 2 squares](./102-square.py)** - Write a class Square that defines a square (based on 4-square.py)
- [x] **[10. ByteCode -> Python #5 ](./103-magic_class.py)** - Write the Python class MagicClass that does exactly the same as the following Python bytecode:
```
Disassembly of __init__:
 10           0 LOAD_CONST               1 (0)
              3 LOAD_FAST                0 (self)
              6 STORE_ATTR               0 (_MagicClass__radius)

 11           9 LOAD_GLOBAL              1 (type)
             12 LOAD_FAST                1 (radius)
             15 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
             18 LOAD_GLOBAL              2 (int)
             21 COMPARE_OP               9 (is not)
             24 POP_JUMP_IF_FALSE       60
             27 LOAD_GLOBAL              1 (type)
             30 LOAD_FAST                1 (radius)
             33 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
             36 LOAD_GLOBAL              3 (float)
             39 COMPARE_OP               9 (is not)
             42 POP_JUMP_IF_FALSE       60

 12          45 LOAD_GLOBAL              4 (TypeError)
             48 LOAD_CONST               2 ('radius must be a number')
             51 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
             54 RAISE_VARARGS            1
             57 JUMP_FORWARD             0 (to 60)

 13     >>   60 LOAD_FAST                1 (radius)
             63 LOAD_FAST                0 (self)
             66 STORE_ATTR               0 (_MagicClass__radius)
             69 LOAD_CONST               3 (None)
             72 RETURN_VALUE

Disassembly of area:
 17           0 LOAD_FAST                0 (self)
              3 LOAD_ATTR                0 (_MagicClass__radius)
              6 LOAD_CONST               1 (2)
              9 BINARY_POWER
             10 LOAD_GLOBAL              1 (math)
             13 LOAD_ATTR                2 (pi)
             16 BINARY_MULTIPLY
             17 RETURN_VALUE

Disassembly of circumference:
 21           0 LOAD_CONST               1 (2)
              3 LOAD_GLOBAL              0 (math)
              6 LOAD_ATTR                1 (pi)
              9 BINARY_MULTIPLY
             10 LOAD_FAST                0 (self)
             13 LOAD_ATTR                2 (_MagicClass__radius)
             16 BINARY_MULTIPLY
             17 RETURN_VALUE
```

## Author :pencil:
**Santiago Peña Mosquera** - twitter [@Santiag11470161](https://twitter.com/Santiag11470161) - LinkedIn [Santiago Peña Mosquera](https://www.linkedin.com/in/santiago-pe%C3%B1a-mosquera-abaa20196/)