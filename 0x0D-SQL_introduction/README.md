# 0x0D. SQL - Introduction
## Resources :books:
### Read or watch:

* [What is Database & SQL?]()
* [A Basic MySQL Tutorial]()
* [Basic SQL statements: DDL and DML (no need to read the chapter “Privileges”)]()
* [Basic queries: SQL and RA]()
* [SQL technique: functions]()
* [SQL technique: subqueries]()
* [What makes the big difference between a backtick and an apostrophe?]()
* [MySQL Cheat Sheet]()
* [MySQL 5.7 SQL Statement Syntax]()
## Learning Objectives :bulb:
* At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General
* What’s a database
* What’s a relational database
* What does SQL stand for
* What’s MySQL
* How to create a database in MySQL
* What does DDL and DML stand for
* How to CREATE or ALTER a table
* How to SELECT data from a table
* How to INSERT, UPDATE or DELETE data
* What are subqueries
* How to use MySQL functions
## Requirements :white_check_mark:
### General
* Allowed editors: vi, vim, emacs
* All your files will be executed on Ubuntu 14.04 LTS using MySQL 5.7 (version 5.7.8-rc)
* All your files should end with a new line
* All your SQL queries should have a comment just before (i.e. syntax above)
* All your files should start by a comment describing the task
* All SQL keywords should be in uppercase (SELECT, WHERE…)
* A README.md file, at the root of the folder of the project, is mandatory
* The length of your files will be tested using wc

## Tasks
### Mandatory :page_with_curl:
- [x] **[0. List databases](./0-list_databases.sql)** - Write a script that lists all databases of your MySQL server
- [x] **[1. Create a database](./1-create_database_if_missing.sql)** - Write a script that creates the database hbtn_0c_0 in your MySQL server
- [x] **[2. Delete a database](./2-remove_database.sql)** - Write a script that deletes the database hbtn_0c_0 in your MySQL server
- [x] **[3. List tables](./3-list_tables.sql)** - Write a script that lists all the tables of a database in your MySQL server
- [x] **[4. First table](./4-first_table.sql)** - Write a script that creates a table called first_table in the current database in your MySQL server
- [x] **[5. Full description](./5-full_table.sql)** - Write a script that prints the full description of the table first_table from the database hbtn_0c_0 in your MySQL server
- [x] **[6. List all in table](./6-list_values.sql)** - Write a script that lists all rows of the table first_table from the database hbtn_0c_0 in your MySQL server
- [x] **[7. First add](./7-insert_value.sql)** - Write a script that inserts a new row in the table first_table (database hbtn_0c_0) in your MySQL server
- [x] **[8. Count 89](./8-count_89.sql)** - Write a script that displays the number of records with id = 89 in the table first_table of the database hbtn_0c_0 in your MySQL server
- [x] **[9. Full creation](./9-full_creation.sql)** - Write a script that creates a table second_table in the database hbtn_0c_0 in your MySQL server and add multiples rows
- [x] **[10. List by best](./10-top_score.sql)** - Write a script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server
- [x] **[11. Select the best](./11-best_score.sql)** - Write a script that lists all records with a score >= 10 in the table second_table of the database hbtn_0c_0 in your MySQL server
- [x] **[12. Cheating is bad](./12-no_cheating.sql)** - Write a script that updates the score of Bob to 10 in the table second_table
- [x] **[13. Score too low](./13-change_class.sql)** - Write a script that removes all records with a score <= 5 in the table second_table of the database hbtn_0c_0 in your MySQL server
- [x] **[14. Average](./14-average.sql)** - Write a script that computes the score average of all records in the table second_table of the database hbtn_0c_0 in your MySQL server
- [x] **[15. Number by score](./15-groups.sql)** - Write a script that lists the number of records with the same score in the table second_table of the database hbtn_0c_0 in your MySQL server
- [x] **[16. Say my name](./16-no_link.sql)** - Write a script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server
### Advance :muscle:
- [x] **[17. Go to UTF8](./100-move_to_utf8.sql)** - Write a script that converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci) in your MySQL server
- [x] **[18. Temperatures #0](./101-avg_temperatures.sql)** - Write a script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending)
- [x] **[19. Temperatures #1](./102-top_city.sql)** - Write a script that displays the top 3 of cities temperature during July and August ordered by temperature
- [x] **[20. Temperatures #2](./103-max_state.sql)** - Write a script that displays the max temperature of each state
## Author :pencil:
**Santiago Peña Mosquera** - twitter [@Santiag11470161](https://twitter.com/Santiag11470161) - LinkedIn [Santiago Peña Mosquera](https://www.linkedin.com/in/santiago-pe%C3%B1a-mosquera-abaa20196/)
