# Boosts

[![CircleCI](https://dl.circleci.com/status-badge/img/circleci/Y1ZCzLfk7VvFxn1NaACyjS/ENyXaR4r8up5rVUZaAc7so/tree/main.svg?style=shield&circle-token=78bff58ef7d68a6559243b0c34cc64153c4e2e0e)](https://dl.circleci.com/status-badge/redirect/circleci/Y1ZCzLfk7VvFxn1NaACyjS/ENyXaR4r8up5rVUZaAc7so/tree/main)

## Description

### Boosts: Your Digital Repository of Inspiration

In a world where every day brings new challenges, finding moments of inspiration is more important than ever. That's where Boosts comes in – your personal sanctuary for capturing and cherishing the sparks of joy, gratitude, and motivation that light up your life.

**Features at a Glance:**

- **Preserve Your Inspirational Gems:** With Boosts, you can easily save statements of appreciation, gratitude, and inspiration. Whether it's a heartwarming comment from a loved one, a line from your favorite book, or a personal mantra that keeps you grounded, Boosts ensures that these precious moments are never forgotten.

- **Curate Your Collection of Inspirations:** Life is a journey of ups and downs, and sometimes, all it takes to lift your spirits is a reminder of the positive vibes that surround you. Our application lets you review your collection of 'Inspirational's anytime, offering a much-needed boost of positivity and motivation when you need it most.

- **Share the Joy with Your Beastie:** What's better than experiencing moments of inspiration? Sharing them with your 'Beastie'! In Boosts, a 'Beastie' isn't just your best friend; they're your partner in positivity, your ally in appreciation, and your fellow traveler on the road to personal growth. Easily share your Inspirational's with your Beastie, spreading the joy and reinforcing the bonds that matter most.

### Elevate Your Everyday with Boosts

Boosts isn't just an app; it's your companion in cultivating a more inspired, grateful, and connected life. By providing a space to save and share your most uplifting moments, Boosts helps you and your Beastie navigate life's journey with a lighter heart and a spirit full of inspiration.

Join the Boosts community today and transform the way you see the world, one Inspirational at a time.





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

In the development of the Boosts Django application, we have utilized a range of powerful tools and technologies to ensure a robust, scalable, and efficient platform. Below is a brief overview of each technology and its role within our application:

### Python
A versatile and powerful programming language that serves as the foundation of our application. Python's readability and rich ecosystem of libraries make it an ideal choice for web development.

### Django
A high-level Python web framework that encourages rapid development and clean, pragmatic design. Django is used to build the core functionality of the Boosts application, providing a structured and scalable approach to web development.

### Celery
An asynchronous task queue/job queue based on distributed message passing. Celery is used for handling the background tasks of the Boosts application, allowing for efficient processing of long-running operations without blocking the main application thread.

### django-celery-beat
An extension to Celery that adds support for storing the periodic task schedule in the Django database. It allows for dynamic, database-driven scheduling of tasks.

### pipenv
A tool that aims to bring the best of all packaging worlds to the Python world. Pipenv is used for managing project dependencies and ensuring a consistent development environment across all team members' machines.

### Heroku
A cloud platform as a service (PaaS) supporting several programming languages. Heroku is used to deploy, manage, and scale the Boosts application, providing an easy-to-use platform for deploying web applications.

### Redis
An in-memory data structure store, used as a database, cache, and message broker. Redis supports the Boosts application by providing high-speed data storage and retrieval, enhancing performance for dynamic content.

### django-redis
A full-featured Redis cache/session backend for Django. This integrates Redis with Django, offering a seamless caching mechanism for the application's data, thus improving response times and reducing database load.

### gunicorn
A Python WSGI HTTP Server for UNIX. Gunicorn 'Green Unicorn' is a Python WSGI HTTP Server for UNIX, used as the web server for the Boosts application when deployed, offering a robust and efficient way to serve Python web applications.

### whitenoise
A simple static file serving for Python web apps. With Whitenoise, the Boosts application can serve its static files directly from Gunicorn, simplifying deployment and reducing the configuration overhead.

### coverage
A tool for measuring code coverage of Python programs. This tool is crucial for maintaining high-quality code in the Boosts application, ensuring that all parts of the application are adequately tested.

### docutils
A modular system for processing documentation into useful formats, such as HTML, XML, and LaTeX. Docutils is used in the Boosts application for generating documentation from reStructuredText sources, making it easier to maintain and update documentation.

### python-dotenv
A Python library that reads key-value pairs from a `.env` file and sets them as environment variables. This is used in the Boosts application for managing environment-specific settings, making the application more secure and configurable.

## Features

### Current Features

Django Boosts Application offers a unique blend of functionality and technical sophistication designed to inspire and connect users. Here are the highlights of what it brings to the table:

- **Inspirational Statements Creation**: Users can craft and save their own motivational or inspirational statements, personalizing their experience and creating content that resonates with them.

- **Personal Inspirational List**: Each user can view their collection of 'Inspirational' statements, allowing easy access to their custom motivational content whenever they need a boost.

- **Beastie Feature**: Every user gets a 'Beastie' – our playful twist on the concept of a 'bestie' or best friend. This feature adds a layer of engagement and fun to the user experience.

- **Sharing with Beasties**: With just a click of a button, users can share their inspirational statements with their 'Beastie', making motivation and positive vibes spread easily among friends.

- **Asynchronous Email Sending**: Leveraging Celery, the application ensures that emails, such as those sharing Inspirational statements with a Beastie, are sent asynchronously. This enhances the application's performance and user experience by not blocking the main thread during email dispatch.

- **Integration with Python-Redis**: The application utilizes `python-redis` for efficient caching and session storage, significantly improving load times and scalability.

- **Custom User Model**: Features a `CustomUser` model that includes a `registration_accepted` field. This field is crucial for controlling access to the application, ensuring that only approved users can create and share Inspirational statements.

- **`base.mixins.RegistrationAcceptedMixin`**: This mixin is used to restrict access to the application's views, ensuring that only users with `registration_accepted` status can interact with the core features of the application.

- **Custom 403 Page**: Enhances user experience during authentication and permission issues by providing a custom 403 page. This page offers useful information to users about their authentication status and what actions they can take, making the application more user-friendly and secure.

- **`utils.get_database_config_variables` Function**:  Seamlessly extract and return database configuration variables by parsing the Heroku database URL environment variable. This utility ensures that applications can dynamically access database credentials and settings, facilitating secure and efficient database connections in Heroku-hosted environments.

These features combine to create a user-centered, performance-oriented application that not only motivates and inspires but also does so with an emphasis on user experience and technical excellence.


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

<a href=mailto:FlynntKnapp@gmail.com>FlynntKnapp@gmail.com</a>

[Back to Table of Contents](#table-of-contents)
