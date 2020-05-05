# 0x01. Python - if/else, loops, functions
## Resources :books:

* [More Control Flow Tools ](https://intranet.hbtn.io/rltoken/R7uTXYVOjUilq6rCjsQcFg)
* [Myths about Indentation](https://intranet.hbtn.io/rltoken/Y-HaMMJBKPseiVDo_v9PVg)
* [IndentationError](https://intranet.hbtn.io/rltoken/AorC2VSZ4yCOx-AbatvKLA)
* [How To Use String Formatters in Python 3](https://intranet.hbtn.io/rltoken/arGQeiwUbFn3JOoYpw84yA)
* [Learn to Program](https://intranet.hbtn.io/rltoken/mlo-dauC8pSM_NrO5VYobw)
* [Learn to Program 2 : Looping](https://intranet.hbtn.io/rltoken/mlo-dauC8pSM_NrO5VYobw)
* [PEP 8 – Style Guide for Python Code](https://intranet.hbtn.io/rltoken/mq1IFaMhqpk2IHE0dC6UuQ)
* [Install and usage](https://intranet.hbtn.io/rltoken/nzvAoWKw6zCTiWUPdkbXWw)

## Learning Objectives :bulb:
* Why Python programming is awesome (don’t forget to tweet today, with the hashtag #pythoniscool :))
* Why indentation is so important in Python
* How to use the if, if ... else statements
* How to use comments
* How to affect values to variables
* How to use the while and for loops
* How is Python’s for different from C‘s?
* How to use the break and continues statements
* How to use else clauses on loops
* What does the pass statement do, and when to use it
* How to use range
* What is a function and how do you use functions
* What does return a function that does not use any return statement
* Scope of variables
* What’s a traceback
* What are the arithmetic operators and how to use them

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
### C Scripts
* Allowed editors: vi, vim, emacs
* All your files will be compiled on Ubuntu 14.04 LTS
* Your programs and functions will be compiled with gcc 4.8.4 using the flags -Wall -Werror -Wextra and -pedantic
* All your files should end with a new line
* Your code should use the Betty style. It will be checked using betty-style.pl and betty-doc.pl
* You are not allowed to use global variables
* No more than 5 functions per file
* In the following examples, the main.c files are shown as examples. You can use them to test your functions, but you don’t have to push them to your repo (if you do we won’t take them into account). We will use our own main.c files at compilation. Our main.c files might be different from the one shown in the examples
* The prototypes of all your functions should be included in your header file called lists.h
* Don’t forget to push your header file
* All your header files should be include guarded

## Tasks :page_with_curl:
### Mandatory
- [x] **[0. Positive anything is better than negative nothing](./0-positive_or_negative.py)** - This program will assign a random signed number to the variable number each time it is executed. Complete the source code in order to print whether the number stored in the variable number is positive or negative.
- [x] **[1. The last digit](./1-last_digit.py)** - This program will assign a random signed number to the variable number each time it is executed. Complete the source code in order to print the last digit of the number stored in the variable number.
- [x] **[2. I sometimes suffer from insomnia. And when I can't fall asleep, I play what I call the alphabet game](./2-print_alphabet.py)** - Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.
- [x] **[3. When I was having that alphabet soup, I never thought that it would pay off](./3-print_alphabt.py)** - Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.
- [x] **[4. Hexadecimal printing](./4-print_hexa.py)** - Write a program that prints all numbers from 0 to 98 in decimal and in hexadecimal (as in the following example)
- [x] **[5. 00...99](./5-print_comb2.py)** - Write a program that prints numbers from 0 to 99.
- [x] **[6. Inventing is a combination of brains and materials. The more brains you use, the less material you need](./6-print_comb3.py)** - Write a program that prints all possible different combinations of two digits.
- [x] **[7. islower](./7-islower.py)** - Write a function that checks for lowercase character.
- [x] **[8. To uppercase](./8-uppercase.py)** - Write a function that prints a string in uppercase followed by a new line.
- [x] **[9. There are only 3 colors, 10 digits, and 7 notes; it's what we do with them that's important ](./9-print_last_digit.py)** - Write a function that prints the last digit of a number.
- [x] **[10. a + b](./10-add.py)** - Write a function that adds two integers and returns the result.
- [x] **[11. a ^ b](./11-pow.py)** - Write a function that computes a to the power of b and return the value.
- [x] **[12. Fizz Buzz](./12-fizzbuzz.py)** - Write a function that prints the numbers from 1 to 100 separated by a space.
- [x] **[13. Insert in sorted linked list](./13-insert_number.c)** - Write a function in C that inserts a number into a sorted singly linked list.
### Advance :muscle:
- [x] **[14. Smile in the mirror](./100-print_tebahpla.py)** - Write a program that prints the ASCII alphabet, in reverse order, alternating lowercase and uppercase (z in lowercase and Y in uppercase) , not followed by a new line.
- [x] **[15. Remove at position](./101-remove_char_at.py)** - Write a function that creates a copy of the string, removing the character at the position n (not the Python way, the “C array index”).
- [x] **[16. ByteCode -> Python #2](./102-magic_calculation.py)** - Write the Python function def magic_calculation(a, b, c): that does exactly the same as the following Python bytecode:
```
3           0 LOAD_FAST                0 (a)
              3 LOAD_FAST                1 (b)
              6 COMPARE_OP               0 (<)
              9 POP_JUMP_IF_FALSE       16

  4          12 LOAD_FAST                2 (c)
             15 RETURN_VALUE

  5     >>   16 LOAD_FAST                2 (c)
             19 LOAD_FAST                1 (b)
             22 COMPARE_OP               4 (>)
             25 POP_JUMP_IF_FALSE       36

  6          28 LOAD_FAST                0 (a)
             31 LOAD_FAST                1 (b)
             34 BINARY_ADD
             35 RETURN_VALUE

  7     >>   36 LOAD_FAST                0 (a)
             39 LOAD_FAST                1 (b)
             42 BINARY_MULTIPLY
             43 LOAD_FAST                2 (c)
             46 BINARY_SUBTRACT
             47 RETURN_VALUE
```
## Author :pencil:
**Santiago Peña Mosquera** - twitter [@Santiag11470161](https://twitter.com/Santiag11470161) - LinkedIn [Santiago Peña Mosquera](https://www.linkedin.com/in/santiago-pe%C3%B1a-mosquera-abaa20196/)
