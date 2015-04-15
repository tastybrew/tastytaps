=========
Tastytaps
=========

Tastytaps is an open-source beer board for displaying what's on tap.

Current status
==============

Very alpha and currently non-functional. We are working towards a minimum
viable product by mid 2015.

Project details
===============

:Code:           https://github.com/tastybrew/tastytaps
:Issue tracker:  https://github.com/tastybrew/tastytaps/issues
:License:        BSD 3-clause; see LICENSE_ file

.. _LICENSE: https://github.com/tastybrew/tastytaps/blob/master/LICENSE

Our unit tests are run by Travis CI every time we commit to the master branch.

.. image:: https://travis-ci.org/tastybrew/tastytaps.svg?branch=master
   :target: https://travis-ci.org/tastybrew/tastytaps/

Installation
============

Create a python virtualenv and pip install the requirements::

    pip install --nodeps -r requirements.txt

We follow the philosophy of `The Twelve-Factor App`_ as much as possible.
Once the virtualenv is created we create the necessary environment
variables when entering the virtualenv.

.. _The Twelve-Factor App: http://12factor.net/

This project requires the following environment variables. Adjust as
needed::

    # Add to your $VIRTUAL_ENV/bin/postactivate file.
    export DJANGO_SETTINGS_MODULE=tastytaps.settings
    export DJANGO_DEBUG='true'  # Defaults to False if unset.
    export DJANGO_SECRET='<your django secret>'
    export DATABASE_URL='postgres://tastytaps:tastytaps@localhost:5432/tastytaps'

Make sure to clear the settings when leaving the virtualenv::

    # Add to your $VIRTUAL_ENV/bin/predeactivate file.
    unset DJANGO_SETTINGS_MODULE
    unset DJANGO_DEBUG
    unset DJANGO_SECRET
    unset DATABASE_URL

Once the virtualenv and environment variables are set up, set up the
Django database and runserver as you would for any Django project.

To quickly set up a PostgreSQL role and database::

    # Enter password after the following. Use 'tastytaps' if using the
    # above DATABASE_URL.
    $ createuser --createdb --pwprompt --no-superuser --no-createrole tastytaps
    $ createdb --owner=tastytaps tastytaps
