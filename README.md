# SQLAlchemy Validations Lab

## Learning Goals

- Define constraints and validations in data processing.
- Ensure that only acceptable input is sent to the database using validations.

***

## Key Vocab

- **Constraint**: a rule enforced on the data columns of a table. Ensures that
  only appropriate data is saved to the database.
- **Validation**: an automatic check to ensure that data entered
  is sensible and feasible.
- **Forms**: A web form (or HTML form) is a place where users enter data or
  personal information that's then sent to a server for processing.

***

## Introduction

This project has starter code for a couple of models, `Author` and `Post`. To
get set up, run:

This is a **test-driven lab**. Run `pipenv install` to create your virtual
environment and `pipenv shell` to enter the virtual environment.

To generate a database using the provided models, from `lib/` run:

```bash
$ alembic upgrade head
```

***

## Basic Validations

Add validations to these models such that...

1. All authors have a name.
2. No two authors have the same name.
3. Author phone numbers are exactly ten digits.
4. All posts have a title.
5. Post content is at least 250 characters long.
6. Post summary is a maximum of 250 characters.
7. Post category is either `Fiction` or `Non-Fiction`.

Then run `pytest -x` to run your tests. Use these instructions and `pytest`'s
error messages to complete your work in the `lib/` folder.

***

## Custom Validations

Finally, add a custom validator to the `Post` model that ensures the title is
sufficiently clickbait-y. The validator should add a validation error if the
title does not contain:

- "Won't Believe"
- "Secret"
- "Top [number]"
- "Guess"

***

## Resources

- [Changing Attribute Behavior - SQLAlchemy][SQLAlchemy Validations]

[SQLAlchemy validations]: https://docs.sqlalchemy.org/en/14/orm/mapped_attributes.html#simple-validators
