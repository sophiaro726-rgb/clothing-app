Fashion Fit

Fashion Fit is a personal project designed to help real-life retail customers find clothing pieces based on measurements and real-life reviews. Online shopping was created to make it convenient to purchase from home, but the main challenge is not being able to try on clothes. This project was created to help shoppers search for items by comparing others’ experiences, attempting to get the closest fit possible. Instead of relying on the predetermined sizes on the brand’s website, the Fashion Fit community can work together to determine what “size” truly fits them best. 

Features

~ Home Screen with access to multiple frontend pages

~ Login and Signup pages + recognition of existing accounts

~ Logout mechanics + user-synced submissions

~ Review submission for already created and logged-in accounts with both optional and required fields

~ Hashed passwords for security 

~ Unit and integration testing 

~ Search with a variety of optional features: category, size, year, color, height, weight, gender

~ Case-insensitive search

~ Picture upload and display 

~ Conditional requirements for fields (height and weight)

~ Dockerfile for observational purposes

~ EC2 instance in AWS 


Technologies Used

~ HTML

~ CSS

~ Python

~ PostgreSQL

~ Psycopg2

~ Pytest

~ Bcrypt

~ Flask

~ Git and GitHub

~ Jinja2 (from Flask)

~ Docker

~ AWS (EC2)


What I Learned

While working on this project, I learned how to:

~ Use Git and GitHub

~ Create and organize files

~ Build a basic website using both HTML and Python simultaneously 

~ Make changes and push them to GitHub

~ Create unit and integration tests

~ Create POST and GET app routes using Flask

~ Store different data types (text, ints, images) inside an SQL table

~ CSS styling 

~ How to hash passwords using bytes and converting to string

~ How to create a Dockerfile

~ How to hide .env from being pushed into GitHub

~ Using AWS and creating an instance in EC2


Future Improvements

~ Improve the design

~ Add Google Lens search feature for customers who don’t know the name of their item, using APIs to detect articles and where they come from

Links & Resources

~ https://www.postgresql.org/docs/current/libpq-pgpass.html - Used to create a private password file so outside users cannot access the database (.pgpass).

~ https://www.w3schools.com - Used for HTML tags, CSS styling templates, and SQL attributes.

~ https://flask.palletsprojects.com/en/stable/quickstart/#sessions - Introduction for Flask, using some of the following section’s examples as templates or guidance: Routing, URL building, HTTP Methods, Static Files, Rendering Templates, Accessing Request Data, File Uploads, and Sessions. 

~ https://flask.palletsprojects.com/en/stable/testing/- Flask unit and integration tests inside the file test_.py

~ https://docs.pytest.org/en/stable/getting-started.html - Introduction to pytest to run unit and integration tests.

~ https://jinja.palletsprojects.com/en/stable/templates/ - Jinja template from Flask website for presentation purposes. Allows for search.html to display results based on CSS styling instead of a printed list. 

~ https://pypi.org/project/python-dotenv/ - .env Introduction and examples used to keep passwords/secret keys stored on all platforms. Upgraded from just the .pgpass saved on the desktop.

~ https://www.psycopg.org/docs/module.html - psycopg parameters used for the .connect() function 

~ https://docs.docker.com/reference/samples/flask/ - Creating a Dockerfile to run for observability by actually running the app instead of just reading code

~ https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-connect-tutorial.html  - Set up for SSH client on Windows device for AWS launcher 

~ https://docs.docker.com/engine/install/ubuntu/ - Setting up the Docker within the instance in EC2 




Author

Sophia Rosas

Rutgers University - New Brunswick 

Class of ‘28

Computer Science (BA) Major
