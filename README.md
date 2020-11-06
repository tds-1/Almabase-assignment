# Almabase Assignment
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/1ac554483fac462797ffa5a8b9adf2fa?style=flat-square)]()
[![Build Status](https://api.travis-ci.org/fossasia/badgeyay.svg?branch=development&style=flat-square)]()

Almabase Assignment
  - Finding N most popular repositories of a given organization on Github base on number of forks.
  - Finding M top committees and their commit counts of each repository.

Link to the application - https://almabase-assignment-tds.herokuapp.com/

## Pre-requisites (to run App locally)
- Python 3.6 and pip should be preinstalled
- Github Access token


## Technology Stack

- Programming Languages
    - Python 3.6
    
- Frameworks
  - Django 3.1.2

- Frontend
    - HTML 5
    - CSS 3
    - Jinja
    - Bootstrap 4

- APIs
    - Github Api
        

## How To Use
1. Clone the repository
```sh
git clone https://github.com/tds-1/Almabase-assignment
```
2. Generate **Github access token** from Github Developer console (https://github.com/settings/tokens) and paste them in the .env file along with the secret key. env file looks like below:
```
SECRET_KEY=SECRET_KEY
TOKEN_ID=YOUR_TOKEN_ID

```
3. Create a **virtual environment**.
4. Install the dependenies
```sh
pip install -r requirements.txt
```
5. **Run** the django server on local host.
```sh 
python manage.py runserver
```


## Snapshots
- First page with which the interacts.
![alt text](https://github.com/tds-1/Almabase-assignment/blob/master/images/homepage.png)
- List of Repositories along with there information.
![alt text](https://github.com/tds-1/Almabase-assignment/blob/master/images/repo.png)
- List of top committees.
![alt text](https://github.com/tds-1/Almabase-assignment/blob/master/images/users.png)

## Note: Heroku wouldn't work with big values of n and m.