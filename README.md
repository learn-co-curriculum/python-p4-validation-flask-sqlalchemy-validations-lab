# Flask-SQLAlchemy Validations Lab

## Learning Goals

- Define validations in data processing.
- Ensure that only acceptable input is sent to the database using validations.

---

## Key Vocab

- **Constraint**: a rule enforced on the data columns of a table. Ensures that
  only appropriate data is saved to the database.
- **Validation**: an automatic check to ensure that data entered is sensible and
  feasible.
- **Forms**: A web form (or HTML form) is a place where users enter data or
  personal information that's then sent to a server for processing.

---

## Introduction

This is a **test-driven lab**.

Run `pipenv install` to create your virtual environment and `pipenv shell` to
enter the virtual environment.

```console
pipenv install && pipenv shell
```

This project has starter code for a couple of models, `Author` and `Post`. To
get create the database from the initial migration, run:

```console
$ cd server
$ flask db upgrade
$ python seed.py
```

---

## Basic Validations

Add validators to the `Author` and `Post` models such that:

1. All authors have a name.
2. No two authors have the same name.
3. Author phone numbers are exactly ten digits.
4. Post content is at least 250 characters long.
5. Post summary is a maximum of 250 characters.
6. Post category is either `Fiction` or `Non-Fiction`.
7. Post title is sufficiently clickbait-y and must contain one of the following:
   - "Won't Believe"
   - "Secret"
   - "Top"
   - "Guess"

You should not need to run another migration, unless you altered model
constraints.

Run `pytest -x` to run your tests. Use these instructions and `pytest`'s error
messages to complete your work in the `server/` folder.

---

## Resources

- [Changing Attribute Behavior - SQLAlchemy][SQLAlchemy Validations]

[SQLAlchemy validations]:
  https://docs.sqlalchemy.org/en/14/orm/mapped_attributes.html#simple-validators
