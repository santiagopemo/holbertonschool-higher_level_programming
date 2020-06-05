# 0x0B. Python - Input/Output
## Resources :books:

* [7.2. Reading and Writing Files](https://intranet.hbtn.io/rltoken/c5ypFfQwcM-SZ-7tr3WuxA)
* [8.7. Predefined Clean-up Actions](https://intranet.hbtn.io/rltoken/1wqMFejKqBva-Lxws0lftw)
* [Dive Into Python 3: Chapter 11. Files ](https://intranet.hbtn.io/rltoken/8aSPOpBZj9B1DB6GfoEWfg)
* [JSON encoder and decoder](https://intranet.hbtn.io/rltoken/XBqM3BrA_rUBw6DXw4X98Q)
* [Learn to Program 8 : Reading / Writing Files](https://intranet.hbtn.io/rltoken/derf9VLFVDnSgX2n-drwnw)
* [Automate the Boring Stuff with Python ](https://intranet.hbtn.io/rltoken/Y77h8aeRoljlN643yKfdTg)

## Learning Objectives :bulb:
* Why Python programming is awesome (don’t forget to tweet today, with the hashtag #pythoniscool :))
* How to open a file
* How to write text in a file
* How to read the full content of a file
* How to read a file line by line
* How to move the cursor in a file
* How to make sure a file is closed after using it
* What is and how to use the with statement
* What is JSON
* What is serialization
* What is deserialization
* How to convert a Python data structure to a JSON string
* How to convert a JSON string to a Python data structure

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
- [x] **[0. Read file](./0-read_file.py)** - Write a function that reads a text file (UTF8) and prints it to stdout
- [x] **[1. Number of lines](./1-number_of_lines.py)** - Write a function that returns the number of lines of a text file
- [x] **[2. Read n lines](./2-read_lines.py)** - Write a function that reads n lines of a text file (UTF8) and prints it to stdout
- [x] **[3. Write to a file](./3-write_file.py)** - Write a function that writes a string to a text file (UTF8) and returns the number of characters written
- [x] **[4. Append to a file](./4-append_write.py)** - Write a function that appends a string at the end of a text file (UTF8) and returns the number of characters added
- [x] **[5. To JSON string](./5-to_json_string.py)** - Write a function that returns the JSON representation of an object (string)
- [x] **[6. From JSON string to Object](./6-from_json_string.py)** - Write a function that returns an object (Python data structure) represented by a JSON string
- [x] **[7. Save Object to a file](./7-save_to_json_file.py)** - Write a function that writes an Object to a text file, using a JSON representation
- [x] **[8. Create object from a JSON file](./8-load_from_json_file.py)** - Write a function that creates an Object from a “JSON file”
- [x] **[9. Load, add, save](./9-add_item.py)** - Write a script that adds all arguments to a Python list, and then save them to a file
- [x] **[10. Class to JSON](./10-my_class_2.py)** - Write a function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object
- [x] **[11. Student to JSON](./11-student.py)** - Write a class Student that defines a student
- [x] **[12. Student to JSON with filter](./12-student.py)** - Write a class Student that defines a student by: (based on 11-student.py)
- [x] **[13. Student to disk and reload](./13-student.py)** - Write a class Student that defines a student by: (based on 12-student.py)
- [x] **[14. Pascal's Triangle](./14-pascal_triangle.py)** - Create a function def pascal_triangle(n): that returns a list of lists of integers representing the Pascal’s triangle of n
### Advance :muscle:
- [x] **[15. Search and update](./100-append_after.py)** - Write a function that inserts a line of text to a file, after each line containing a specific string
- [ ] **[16. Log parsing](./101-stats.py)** - Write a script that reads stdin line by line and computes metrics
- [ ] **[17. Hack the VM](./read_write_heap.py)** - Write a script that finds a string in the heap of a running process, and replaces it

## Author :pencil:
**Santiago Peña Mosquera** - twitter [@Santiag11470161](https://twitter.com/Santiag11470161) - LinkedIn [Santiago Peña Mosquera](https://www.linkedin.com/in/santiago-pe%C3%B1a-mosquera-abaa20196/)