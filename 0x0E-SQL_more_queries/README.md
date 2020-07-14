# 0x0E. SQL - More queries
## Resources :books:
### Read or watch:

* [How To Create a New User and Grant Permissions in MySQL]()
* [How To Use MySQL GRANT Statement To Grant Privileges To a User]()
* [MySQL constraints]()
* [SQL technique: subqueries]()
* [Basic query operation: the join]()
* [SQL technique: multiple joins and the distinct keyword]()
* [SQL technique: join types]()
* [SQL technique: union and minus]()
* [MySQL Cheat Sheet]()
* [The Seven Types of SQL Joins]()
* [MySQL Tutorial]()
* [SQL Style Guide]()
* [MySQL 5.7 SQL Statement Syntax]()
## Learning Objectives :bulb:
* At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General
* How to create a new MySQL user
* How to manage privileges for a user to a database or table
* What’s a PRIMARY KEY
* What’s a FOREIGN KEY
* How to use NOT NULL and UNIQUE constraints
* How to retrieve datas from multiple tables in one request
* What are subqueries
* What are JOIN and UNION
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
- [x] **[0. My privileges!](./0-privileges.sql)** - Write a script that lists all privileges of the MySQL users user_0d_1 and user_0d_2 on your server (in localhost)
- [x] **[1. Root user](./1-create_user.sql)** - Write a script that creates the MySQL server user user_0d_1
- [x] **[2. Read user](./2-create_read_user.sql)** - Write a script that creates the database hbtn_0d_2 and the user user_0d_2
- [x] **[3. Always a name](./3-force_name.sql)** - Write a script that creates the table force_name on your MySQL server
- [x] **[4. ID can't be null](./4-never_empty.sql)** - Write a script that creates the table id_not_null on your MySQL server
- [x] **[5. Unique ID](./5-unique_id.sql)** - Write a script that creates the table unique_id on your MySQL server
- [x] **[6. States table](./6-states.sql)** - Write a script that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your MySQL server
- [x] **[7. Cities table](./7-cities.sql)** - Write a script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL server
- [x] **[8. Cities of California](./8-cities_of_california_subquery.sql)** - Write a script that lists all the cities of California that can be found in the database hbtn_0d_usa
- [x] **[9. Cities by States](./9-cities_by_state_join.sql)** - Write a script that lists all cities contained in the database hbtn_0d_usa
- [x] **[10. Genre ID by show](./10-genre_id_by_show.sql)** - Write a script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked
- [x] **[11. Genre ID for all shows](./11-genre_id_all_shows.sql)** - Write a script that lists all shows contained in the database hbtn_0d_tvshows
- [x] **[12. No genre](./12-no_genre.sql)** - Write a script that lists all shows contained in hbtn_0d_tvshows without a genre linked
- [x] **[13. Number of shows by genre](./13-count_shows_by_genre.sql)** - Write a script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
- [x] **[14. My genres](./14-my_genres.sql)** - Write a script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
- [x] **[15. Only Comedy](./15-comedy_only.sql)** - Write a script that lists all Comedy shows in the database hbtn_0d_tvshows
- [x] **[16. List shows and genres](./16-shows_by_genre.sql)** - Write a script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows
### Advance :muscle:
- [x] **[17. Not my genre](./100-not_my_genres.sql)** - Enter password
- [x] **[18. No Comedy tonight!](./101-not_a_comedy.sql)** - Write a script that lists all shows without the genre Comedy in the database hbtn_0d_tvshows
- [x] **[19. Rotten tomatoes](./102-rating_shows.sql)** - Write a script that lists all shows from hbtn_0d_tvshows_rate by their rating
- [x] **[20. Best genre](./103-rating_genres.sql)** - Write a script that lists all genres in the database hbtn_0d_tvshows_rate by their rating
## Author :pencil:
**Santiago Peña Mosquera** - twitter [@Santiag11470161](https://twitter.com/Santiag11470161) - LinkedIn [Santiago Peña Mosquera](https://www.linkedin.com/in/santiago-pe%C3%B1a-mosquera-abaa20196/)
