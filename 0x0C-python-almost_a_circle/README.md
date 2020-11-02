# 0x0C. Python - Almost a circle
## Resources :books:

* [args/kwargs](https://intranet.hbtn.io/rltoken/SON4gFe6PsxruKOjLYGfig)
* [JSON encoder and decoder](https://intranet.hbtn.io/rltoken/TY4rfu2AZtXlRmPVNZm1Lw)
* [unittest module](https://intranet.hbtn.io/rltoken/T7uxwxtGdbRRW9pkD4eO0g)
* [Python test cheatsheet](https://intranet.hbtn.io/rltoken/SfEo3RQeAXXYI9yabFRw3g)

## Learning Objectives :bulb:
* What is Unit testing and how to implement it in a large project
* How to serialize and deserialize a Class
* How to write and read a JSON file
* What is *args and how to use it
* What is **kwargs and how to use it
* How to handle named arguments in a function

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
* All your modules should be documented: python3 -c 'print(__import__("my_module").__doc__)'
* All your classes should be documented: python3 -c 'print(__import__("my_module").MyClass.__doc__)'
* All your functions (inside and outside a class) should be documented: python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
### Python Unit Tests
* Allowed editors: vi, vim, emacs
* All your files should end with a new line
* All your test files should be inside a folder tests
* You have to use the unittest module
* All your test files should be python files (extension: .py)
* All your test files and folders should start with test_
* Your file organization in the tests folder should be the same as your project: ex: for models/base.py, unit tests must be in: tests/test_models/test_base.py
* All your tests should be executed by using this command: python3 -m unittest discover tests
* You can also test file by file by using this command: python3 -m unittest tests/test_models/test_base.py
* We strongly encourage you to work together on test cases so that you don’t miss any edge case

## Tasks :page_with_curl:
### Mandatory
- [x] **[0. If it's not tested it doesn't work](./tests/)** - All your files, classes and methods must be unit tested and be PEP 8 validated
- [x] **[1. Base class](./models/base.py)** - Write the first class Base
- [x] **[2. First Rectangle](./models/rectangle.py)** - Write the class Rectangle that inherits from Base
- [x] **[3. Validate attributes](./models/rectangle.py)** - Update the class Rectangle by adding validation of all setter methods and instantiation
- [x] **[4. Area first](./models/rectangle.py)** - Update the class Rectangle by adding the public method def area(self): that returns the area value of the Rectangle instance
- [x] **[5. Display #0](./models/rectangle.py)** - Update the class Rectangle by adding the public method def display(self): that prints in stdout the Rectangle instance with the character # - you don’t need to handle x and y here
- [x] **[6. __str__](./models/rectangle.py)** - Update the class Rectangle by overriding the __str__ method so that it returns `[Rectangle] (<id>) <x>/<y> - <width>/<height>`
- [x] **[7. Display #1](./models/rectangle.py)** - Update the class Rectangle by improving the public method def display(self): to print in stdout the Rectangle instance with the character # by taking care of x and y
- [x] **[8. Update #0](./models/rectangle.py)** - Update the class Rectangle by adding the public method def update(self, *args): that assigns an argument to each attribute
- [x] **[9. Update #1](./models/rectangle.py)** - Update the class Rectangle by updating the public method def update(self, *args): by changing the prototype to update`(self, *args, **kwargs)` that assigns a key/value argument to attributes
- [x] **[10. And now, the Square!](./models/square.py)** - Write the class Square that inherits from Rectangle
- [x] **[11. Square size](./models/square.py)** - Update the class Square by adding the public getter and setter size
- [x] **[12. Square update](./models/square.py)** - Update the class Square by adding the public method def update`(self, *args, **kwargs)` that assigns attributes
- [x] **[13. Rectangle instance to dictionary representation](./models/rectangle.py)** - Update the class Rectangle by adding the public method def to_dictionary(self): that returns the dictionary representation of a Rectangle
- [x] **[14. Square instance to dictionary representation](./models/square.py)** - Update the class Square by adding the public method def to_dictionary(self): that returns the dictionary representation of a Square
- [x] **[15. Dictionary to JSON string](./models/base.py)** - Update the class Base by adding the static method def to_json_string(list_dictionaries): that returns the JSON string representation of list_dictionaries
- [x] **[16. JSON string to file](./models/base.py)** - Update the class Base by adding the class method def save_to_file(cls, list_objs): that writes the JSON string representation of list_objs to a file
- [x] **[17. JSON string to dictionary](./models/base.py)** - Update the class Base by adding the static method def from_json_string(json_string): that returns the list of the JSON string representation json_string
- [x] **[18. Dictionary to Instance](./models/base.py)** - Update the class Base by adding the class method def `create(cls, **dictionary)`: that returns an instance with all attributes already set
- [x] **[19. File to instances](./models/base.py)** - Update the class Base by adding the class method def load_from_file(cls): that returns a list of instances
### Advance :muscle:
- [x] **[20. JSON ok, but CSV?](./models/)** - Update the class Base by adding the class methods def save_to_file_csv(cls, list_objs): and def load_from_file_csv(cls): that serializes and deserializes in CSV
- [x] **[21. Let's draw it](./models/base.py)** - Update the class Base by adding the static method def draw(list_rectangles, list_squares): that opens a window and draws all the Rectangles and Squares

## Author :pencil:
**Santiago Peña Mosquera** - twitter [@Santiag11470161](https://twitter.com/Santiag11470161) - LinkedIn [Santiago Peña Mosquera](https://www.linkedin.com/in/santiago-pe%C3%B1a-mosquera-abaa20196/)
