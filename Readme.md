# Josephs Interview Answers 

## Introduction 

This is my attempt at solving the Multipart/Multistep Wizard to get a users BioData, bidding setting and Google Ads Account Id

## Getting Setup

**Project Requirements**

* [Python >= 3.0](https://docs.python.org/3)
* [Django == 3.2.12](https://docs.djangoproject.com/en/3.2/)

**Setup**

* create a folder e.g bidnamic
* On folder creation clone the repository via terminal
```sh
git clone https://github.com/jbraide/bidnamic-fullstack-challenge.git
```

> *Note:* This needs to be done only once

**Create and activate virtual environment**

After creating a virtual environment (optional), activate it by running

```sh
python -m venv venv
```

For windows, activate it this way

```sh
venv/Scripts/activate
```

For other operating system like Linux and MacOS, use

```sh
source venv/bin/activate
```

**Installing project dependencies**

To install the project dependencies, use

```sh
pip install -r requirements.txt
```

**Migrating changes**

Make sure you run the following code after creating either a new django app, model or migration. This will ensure that the database is in sync and prevent unnecessary issues.

```sh
cd bidnamic_interview
python manage.py makemigrations
python manage.py migrate
```

**Running Tests**

To run the test 
```sh
python manage.py test multistepform.tests
```

## Functionality Description 
