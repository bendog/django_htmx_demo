# Django HTMX Demo

Combining [Django](https://www.djangoproject.com/) with [HTMX](https://htmx.org/)

An example app for showing simple ajax calls using htmx in django templates. No API required.

## install and run

create the virtual env

    pipenv sync
    pipenv shell

setup the local database

    python manage.py migrate

run the local server

    python manage.py runserver

open <http://localhost:8000/> in your browser.

## thanks and acknowledgement

Thanks to Muhammed Ali [@khabdrick](https://github.com/khabdrick) for their blog post which was used as inspiration for this demo <https://www.section.io/engineering-education/how-to-build-templates-for-django-applications-with-htmx/>
