# Boosts

## Description

A Django application for storing inspirational statements (called `Boosts`) and displaying them for the user. The user can share their `Boosts` with other users (their `Beasty`).

[![CircleCI](https://dl.circleci.com/status-badge/img/circleci/Y1ZCzLfk7VvFxn1NaACyjS/ENyXaR4r8up5rVUZaAc7so/tree/main.svg?style=shield&circle-token=78bff58ef7d68a6559243b0c34cc64153c4e2e0e)](https://dl.circleci.com/status-badge/redirect/circleci/Y1ZCzLfk7VvFxn1NaACyjS/ENyXaR4r8up5rVUZaAc7so/tree/main)

## Table of Contents

- [Boosts](#boosts)
  - [Description](#description)
  - [Table of Contents](#table-of-contents)
  - [Screenshots or GIFs](#screenshots-or-gifs)
  - [Technologies Used](#technologies-used)
  - [Features](#features)
    - [Current Features](#current-features)
    - [Upcoming Features](#upcoming-features)
  - [Known Issues and Areas for Improvement](#known-issues-and-areas-for-improvement)
  - [Prerequisites, Environment Variables, and Running the Application](#prerequisites-environment-variables-and-running-the-application)
    - [Prerequisites](#prerequisites)
    - [Environment Variables](#environment-variables)
    - [Running the Application](#running-the-application)
  - [Usage](#usage)
  - [Contribution Guidelines](#contribution-guidelines)
  - [License](#license)
  - [Acknowledgements](#acknowledgements)
  - [Contact Information](#contact-information)

## Screenshots or GIFs

## Technologies Used

## Features

### Current Features

- Celery for asynchronous task of sending emails.
- Custom `403` view and template.
- `RegistrationAcceptedMixin` to reduce repeating `test_func` code in `LoginRequiredMixin` and `UserPassesTestMixin`.
- User can send a `Boost` to another user.
- `utils.get_database_config_variables` function to get database configuration variables from Heroku database URL environment variable.

### Upcoming Features

- Add specific view for un-registered users.
- User can choose a time of day to receive a random `Boost` from their list.
- User can choose a time of day to receive a random `Boost` from their `Beastie`s' list.
- User can send a text to receive a random `Boost` from their list.
- User can have multiple `Beastie`s and can select which `Beastie` to send a `Boost` to.
- User can send an invite to be `Beastie`s with another user.
- Django `BaseCommand` to populate the database with sample `Boost`s.

## Known Issues and Areas for Improvement

- User has to have their `Beastie` assigned in Django Admin.
- Need to have `BretBeastie`'s `Boosts` in the database for app to function properly.

## Prerequisites, Environment Variables, and Running the Application

### Prerequisites

### Environment Variables

- All Environments

- Development
    - `TEST_EMAIL_ADDRESS`

- Production
    - `SECRET_KEY`
    - `ENVIRONMENT`
    - `EMAIL_HOST`
    - `EMAIL_HOST_USER`
    - `EMAIL_HOST_PASSWORD`
    - `EMAIL_PORT`

### Running the Application

1. Clone the repository
1. `cd` into the project directory
1. Create a `pipenv` virtual environment and install dependencies
1. Activate the virtual environment
1. Create a `.env` file in the project root directory
1. Perform database migrations
1. Running the tests

## Usage

- User registration
- User login
- Assign `Beastie` to user
- User `Boost` list
- User send a `Boost` to another user

## Contribution Guidelines

## License

## Acknowledgements

- WSV Custom User Model

## Contact Information

- [Back to Table of Contents](#table-of-contents)
