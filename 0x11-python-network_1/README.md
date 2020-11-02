# 0x11. Python - Network #1
## Resources :books:
### Read or watch:

* [Quickstart with Requests package]()
* [Requests package]()
## Learning Objectives :bulb:
* At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General
* How to fetch internet resources with the Python package urllib
* How to decode urllib body response
* How to use the Python package requests #requestsiswaysimplerthanurllib
* How to make HTTP GET request
* How to make HTTP POST/PUT/etc. request
* How to fetch JSON resources
* How to manipulate data from an external service
## Requirements :white_check_mark:
### General
* Allowed editors: vi, vim, emacs
* All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
* All your files should end with a new line
* The first line of all your files should be exactly #!/usr/bin/python3
* A README.md file, at the root of the folder of the project, is mandatory
* Your code should use the PEP 8 style (version 1.7.*)
* All your files must be executable
* The length of your files will be tested using wc
* All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
* You must use get to access to dictionary value by key (it won’t throw an exception if the key doesn’t exist in the dictionary)
* Your code should not be executed when imported (by using if __name__ == "__main__":)
## Tasks
### Mandatory :page_with_curl:
- [x] **[0. What's my status? #0](./0-hbtn_status.py)** - Write a Python script that fetches https://intranet.hbtn.io/status
- [x] **[1. Response header value #0](./1-hbtn_header.py)** - Write a Python script that takes in a URL, sends a request to the URL and displays the value of the X-Request-Id variable found in the header of the response
- [x] **[2. POST an email #0](./2-post_email.py)** - Write a Python script that takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response (decoded in utf-8)
- [x] **[3. Error code #0](./3-error_code.py)** - Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in utf-8)
- [x] **[4. What's my status? #1](./4-hbtn_status.py)** - Repo
- [x] **[5. Response header value #1](./5-hbtn_header.py)** - Repo
- [x] **[6. POST an email #1](./6-post_email.py)** - Write a Python script that takes in a URL and an email address, sends a POST request to the passed URL with the email as a parameter, and finally displays the body of the response
- [x] **[7. Error code #1](./7-error_code.py)** - Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response
- [x] **[8. Search API](./8-json_api.py)** - Write a Python script that takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter
- [x] **[9. My Github!](./10-my_github.py)** - Repo
### Advance :muscle:
- [x] **[10. Time for an interview!](./100-github_commits.py)** - The Holberton School staff evaluates candidates applying for a back-end position with multiple technical challenges, like this one
- [x] **[11. Twitter Auth](./103-search_twitter.py)** - Repo
## Author :pencil:
**Santiago Peña Mosquera** - twitter [@Santiag11470161](https://twitter.com/Santiag11470161) - LinkedIn [Santiago Peña Mosquera](https://www.linkedin.com/in/santiago-pe%C3%B1a-mosquera-abaa20196/)
