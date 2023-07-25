# Boosts

* A Django application for a user to create, read, update, and delete (CRUD) "Inspirational"s.
* A "Inspirational" is a short inspirational statement, quote, or other message that a user can post to their profile.
* A user can receive a random "Inspirational" each day.
* A user can send an email or text message to receive a random "Inspirational" at any time.
* A user can share their "Inspirational"s with other users.

## Table of Contents

## Items Which are not Best Practices

### `config/settings/development.py` and `config/settings/production.py` uses imports of `*` from `config/settings/common.py`.
* This may be fixed in future when project is migrated to use either `pydantic` or some other coding conventions for settings.
* Even though this works as needed, it seems that it is usually not good to import `*` from a module.

## Production Links

## Django Applications

## Models

- [x] CustomUser
- [x] Inspirational

## Views
* `CustomUser`:
    - [x] Create
    - [x] Read
    - [x] Update
* `Inspirational`:
    - [x] Create
    - [ ] Read
    - [x] List
    - [ ] Update
    - [ ] Delete
    - [x] Share

## Templates

## Interesting Features

* [Custom 403 Server Error Page](./notes/custom_403.md)

## New Knowledge

## PyPI Packages

## Resources

### [`pypi`](https://pypi.org/)

* <https://pypi.org/project/Django/>
* <https://pypi.org/project/djangorestframework/>
* <https://pypi.org/project/docutils/>
* <https://pypi.org/project/gunicorn/>
* <https://pypi.org/project/whitenoise/>
* <https://pypi.org/project/psycopg2/>
* <https://pypi.org/project/tzdata/>
* <https://pypi.org/project/python-dotenv/>

### CSS Framework

* <https://getbootstrap.com/>
* [Get started with Bootstrap](https://getbootstrap.com/docs/5.3/getting-started/introduction/)
* <https://getbootstrap.com/docs/5.3/components/>
    * <https://getbootstrap.com/docs/5.3/components/navbar/>
    * <https://getbootstrap.com/docs/5.3/components/pagination/>
* <https://getbootstrap.com/docs/5.3/forms/>
    * <https://getbootstrap.com/docs/5.3/forms/form-control/>
    * <https://getbootstrap.com/docs/5.3/forms/layout/>

### Django

* [`django.views.generic.edit.CreateView`](https://docs.djangoproject.com/en/4.1/ref/class-based-views/generic-editing/#django.views.generic.edit.CreateView)
* [The Forms API](https://docs.djangoproject.com/en/4.1/ref/forms/api/)
* [`django.forms.Field`](https://docs.djangoproject.com/en/4.1/ref/forms/fields/#django.forms.Field)

### Third Party Resources

* [Django DeleteView - www.pythontutorial.net](https://www.pythontutorial.net/django-tutorial/django-deleteview/)
