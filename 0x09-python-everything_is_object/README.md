# 0x09. Python - Everything is object
## Resources :books:

* [9.10. Objects and values](https://intranet.hbtn.io/rltoken/n1x09X-KJSllpJkJorBw2A)
* [9.11. Aliasing](https://intranet.hbtn.io/rltoken/3teQMNNfDeyGvCtZfjsf5g)
* [Immutable vs mutable types](https://intranet.hbtn.io/rltoken/JuPVygeoG27Q_qKxB2lP8g)
* [Mutation](https://intranet.hbtn.io/rltoken/UbL96sV3cIxewdQPW_zwRw)
* [9.12. Cloning lists](https://intranet.hbtn.io/rltoken/-t_1VsmKlgWHszL5y1YiKA)
* [Python tuples: immutable but potentially changing](https://intranet.hbtn.io/rltoken/IdBAdTYNLuS3YpRRQIam6Q)

## Learning Objectives :bulb:
* Why Python programming is awesome (don’t forget to tweet today, with the hashtag #pythoniscool :))
* What is an object
* What is the difference between a class and an object or instance
* What is the difference between immutable object and mutable object
* What is a reference
* What is an assignment
* What is an alias
* How to know if two variables are identical
* How to know if two variables are linked to the same object
* How to display the variable identifier (which is the memory address in the CPython implementation)
* What is mutable and immutable
* What are the built-in mutable types
* What are the built-in immutable types
* How does Python pass variables to functions

## Requirements :white_check_mark:

### Python Scripts
* 
### `.txt` Answer Files
* Only one line
* No Shebang
* All your files should end with a new line

## Tasks :page_with_curl:
### Mandatory
- [x] **[0. Who am I?](./0-answer.txt)** - What function would you use to print the type of an object?
- [x] **[1. Where are you?](./1-answer.txt)** - How do you get the variable identifier (which is the memory address in the CPython implementation)?
- [x] **[2. Right count](./2-answer.txt)** - In the following code, do a and b point to the same object?
```
>>> a = 89
>>> b = 100
```
- [x] **[3. Right count =](./3-answer.txt)** - In the following code, do a and b point to the same object?
```
>>> a = 89
>>> b = 89
```
- [x] **[4. Right count =](./4-answer.txt)** - In the following code, do a and b point to the same object?
```
>>> a = 89
>>> b = a
```
- [x] **[5. Right count =+](./5-answer.txt)** - In the following code, do a and b point to the same object?
```
>>> a = 89
>>> b = a + 1
```
- [x] **[6. Is equal](./6-answer.txt)** - What do these 3 lines print?
```
>>> s1 = "Holberton"
>>> s2 = s1
>>> print(s1 == s2)
```
- [x] **[7. Is the same](./7-answer.txt)** - What do these 3 lines print?
```
>>> s1 = "Holberton"
>>> s2 = s1
>>> print(s1 is s2)
```
- [x] **[8. Is really equal](./8-answer.txt)** - What do these 3 lines print?
```
>>> s1 = "Holberton"
>>> s2 = "Holberton"
>>> print(s1 == s2)
```
- [x] **[9. Is really the same](./9-answer.txt)** - What do these 3 lines print?
```
>>> s1 = "Holberton"
>>> s2 = "Holberton"
>>> print(s1 is s2)
```
- [x] **[10. And with a list, is it equal](./10-answer.txt)** - What do these 3 lines print?
```
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 == l2)
```
- [x] **[11. And with a list, is it the same](./11-answer.txt)** - 
What do these 3 lines print?
```
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 is l2)
```
- [x] **[12. And with a list, is it really equal](./12-answer.txt)** - What do these 3 lines print?
```
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 == l2)
```
- [x] **[13. And with a list, is it really the same](./13-answer.txt)** - What do these 3 lines print?
```
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 is l2)
```
- [x] **[14. List append](./14-answer.txt)** - What does this script print?
```
l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)
```
- [x] **[15. List add](./15-answer.txt)** - What does this script print?
```
l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(l2)
```
- [x] **[16. Integer incrementation](./16-answer.txt)** - What does this script print?
```
def increment(n):
    n += 1

a = 1
increment(a)
print(a)
```
- [x] **[17. List incrementation](./17-answer.txt)** - What does this script print?
```
def increment(n):
    n.append(4)

l = [1, 2, 3]
increment(l)
print(l)
```
- [x] **[18. List assignation](./18-answer.txt)** - What does this script print?
```
def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)
```
- [x] **[19. Copy a list object](./19-answer.txt)** - Write a function def copy_list(l): that returns a copy of a list.
- [x] **[20. Tuple or not?](./20-answer.txt)** - Is a a tuple? Answer with Yes or No.
```
a = ()
```
- [x] **[21. Tuple or not?](./21-answer.txt)** - Is a a tuple? Answer with Yes or No.
```
a = (1, 2)
```
- [x] **[22. Tuple or not?](./22-answer.txt)** - Is a a tuple? Answer with Yes or No.
```
a = (1)
```
- [x] **[23. Tuple or not?](./23-answer.txt)** - Is a a tuple? Answer with Yes or No.
```
a = (1, )
```
- [x] **[24. Richard Sim's special #0](./24-answer.txt)** - What does this script print?
```
a = (1)
b = (1)
a is b
```
- [x] **[25. Richard Sim's special #1](./25-answer.txt)** - What does this script print?
```
a = (1, 2)
b = (1, 2)
a is b
```
- [x] **[26. Richard Sim's special #2](./26-answer.txt)** - What does this script print?
```
a = ()
b = ()
a is b
```
- [x] **[27. Richard Sim's special #3](./27-answer.txt)** - Will the last line of this script print 139926795932424? Answer with Yes or No.
```
>>> id(a)
139926795932424
>>> a
[1, 2, 3, 4]
>>> a = a + [5]
>>> id(a)
```
- [x] **[28. Richard Sim's special #4](./28-answer.txt)** - Will the last line of this script print 139926795932424? Answer with Yes or No.
```
>>> a
[1, 2, 3]
>>> id (a)
139926795932424
>>> a += [4]
>>> id(a)
```
### Advance :muscle:
- [x] **[30. #pythonic](./)** - Write a function magic_string() that returns a string “Holberton” n times the number of the iteration
- [x] **[31. Low memory cost](./)** - Write a class LockedClass with no class or object attribute, that prevents the user from dynamically creating new instance attributes, except if the new instance attribute is called first_name.
- [x] **[32. int 1/3](./)** - Assuming we are using a CPython implementation of Python3 with default options/configuration:
* How many int objects are created by the execution of the first line of the script? (103-line1.txt)
* How many int objects are created by the execution of the second line of the script (103-line2.txt)
```
a = 1
b = 1
```
- [x] **[33. int 2/3](./)** - Assuming we are using a CPython implementation of Python3 with default options/configuration:
* Before the execution of line 2 (print("Love")), how many int objects have been created and are still in memory? (105-line1.txt)
Why? (optional blog post :))
```
print("I")
print("Love")
print("Python")
```
- [x] **[34. int 3/3](./)** - Assuming we are using a CPython implementation of Python3 with default options/configuration (For answers with numbers use integers, don’t spell out the word):
* How many string objects are created by the execution of the first line of the script? (106-line1.txt)
* How many string objects are created by the execution of the second line of the script (106-line2.txt)
* After the execution of line 3, is the string object pointed by a deleted? Answer with Yes or No (106-line3.txt)
* After the execution of line 4, is the string object pointed by b deleted? Answer with Yes or No (106-line4.txt)
* How many string objects are created by the execution of the last line of the script (106-line5.txt)
```
a = "HBTN"
b = "HBTN"
del a
del b
c = "HBTN"
```
## Author :pencil:
**Santiago Peña Mosquera** - twitter [@Santiag11470161](https://twitter.com/Santiag11470161) - LinkedIn [Santiago Peña Mosquera](https://www.linkedin.com/in/santiago-pe%C3%B1a-mosquera-abaa20196/)