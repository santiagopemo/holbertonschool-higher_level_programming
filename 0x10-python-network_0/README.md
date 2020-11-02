# 0x10. Python - Network #0
## Resources :books:
### Read or watch:

* [HTTP (HyperText Transfer Protocol) (except: “TRACE” Request Method, “CONNECT” Request Method, Language Negotiation and “Options MultiView” and Character Set Negotiation)]()
* [HTTP Cookies]()
## Learning Objectives :bulb:
* At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General
* What a URL is
* What HTTP is
* How to read a URL
* The scheme for a HTTP URL
* What a domain name is
* What a sub-domain is
* How to define a port number in a URL
* What a query string is
* What an HTTP request is
* What an HTTP response is
* What HTTP headers are
* What the HTTP message body is
* What an HTTP request method is
* What an HTTP response status code is
* What an HTTP Cookie is
* How to make a request with cURL
* What happens when you type google.com in your browser (Application level)
## Requirements :white_check_mark:
### General
* Allowed editors: vi, vim, emacs
* - A README.md file, at the root of the folder of the project, is mandatory
* All your scripts will be tested on Ubuntu 14.04 LTS
* All your Bash scripts should be exactly 3 lines long (wc -l file should print 3)
* All your files should end with a new line
* All your files must be executable
* The first line of all your bash files should be exactly #!/bin/bash
* The second line of all your Bash scripts should be a comment explaining what is the script doing
* All curl commands must be have the option -s (silent mode)
* All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
* The first line of all your Python files should be exactly #!/usr/bin/python3
* Your code should use the PEP 8 style (version 1.7.*)
* All your modules should be documented: python3 -c 'print(__import__("my_module").__doc__)'
* All your classes should be documented: python3 -c 'print(__import__("my_module").MyClass.__doc__)'
* All your functions (inside and outside a class) should be documented: python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
## Tasks
### Mandatory :page_with_curl:
- [x] **[0. cURL body size](./0-body_size.sh)** - Write a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
- [x] **[1. cURL to the end](./1-body.sh)** - Write a Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response
- [x] **[2. cURL Method](./2-delete.sh)** - Write a Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response
- [x] **[3. cURL only methods](./3-methods.sh)** - Write a Bash script that takes in a URL and displays all HTTP methods the server will accept
- [x] **[4. cURL headers](./4-header.sh)** - Repo
- [x] **[5. cURL POST parameters](./5-post_params.sh)** - POST params
- [x] **[6. Find a peak](./6-peak.py)** - Technical interview preparation
### Advance :muscle:
- [x] **[7. Only status code](./100-status_code.sh)** - Write a Bash script that sends a request to a URL passed as an argument, and displays only the status code of the response
- [x] **[8. cURL a JSON file](./101-post_json.sh)** - Write a Bash script that sends a JSON POST request to a URL passed as the first argument, and displays the body of the response
- [x] **[9. Catch me if you can!](./102-catch_me.sh)** - Write a Bash script that makes a request to 0.0.0.0:5000/catch_me that causes the server to respond with a message containing You got me!, in the body of the response
## Author :pencil:
**Santiago Peña Mosquera** - twitter [@Santiag11470161](https://twitter.com/Santiag11470161) - LinkedIn [Santiago Peña Mosquera](https://www.linkedin.com/in/santiago-pe%C3%B1a-mosquera-abaa20196/)
