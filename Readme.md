# Josephs Interview Answers 

## Introduction 

This is my attempt at solving the Multipart/Multistep Wizard to get a users BioData, bidding setting and Google Ads Account Id

**How it works**

The application uses a 2 step MultiPart form for handling

> Step 1: Bio Data - (i.e title, first_name, surname ... address)
>
> Step 2: Bidding Information - (i.e bidding_settings, google_ads_id)

Bio Data information is stored in the session in the first step and then saved as one record to a single record to accomodate the bidding_setting and google_ads_id.

The solution also accomodates the requirements of being able to handle 

> Not being able to fill the form if date of birth is under 18
>
> option selected or inputted does not exist in the bidding settings (i.e High, Medium, Low)
>

There is also authentication befor being able to view all of the created applications

> *Note:* There is only a login route and No signup, so to have access create a superuser 


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

**Running the Application**

```sh
python manage.py runserver 127.0.0.1:4567
```

**Running Tests**

To run the test suite 

* for multistepform
```sh
python manage.py test multistepform.tests
```

* for view_applications
```sh
python manage.py test view_applications.tests
```
