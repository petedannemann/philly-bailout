# Philly Bailout Fund Administrative Site

## Goals

Overall, the goal of this project is to develop a system that enables PCBF to have cleaner,
searchable data; a system that is simpler to use (particularly for onboarding); and to add some
new features that will make it easier to meet the non-profit’s goals.

## Requirements

- Python 3
- Pip

## Installation

```bash
$ pip install -r requirements.txt
```

## Setup

```bash
$ python manage.py makemigrations  # make migrations
$ python manage.py migrate         # apply migrations
$ python manage.py createsuperuser # create a superuser
```

## Development

```bash
$ python manage.py runserver # start development server
```

## Production

```bash
$ export DJANGO_SETTINGS_MODULE=bailout.settings.prod
$ python manage.py runserver
```
