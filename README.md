# WebGL Jobs website #

This is a simple job-posting website written for Django.  It's made public
under an MIT License.

## Configuration ##

Check out the source, then create files in the root called `email_settings.py`
and `db_settings.py`, with contents like these:

    EMAIL_SUBJECT_PREFIX = "[WebGL Jobs] "
    EMAIL_HOST = "smtp.gmail.com"
    EMAIL_HOST_USER = "webgljobs@gmail.com"
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    EMAIL_HOST_PASSWORD = 'some kind of password'

and

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'webgljobs_db',
            'USER': 'webgljobs',
            'PASSWORD': 'a password',
            'HOST': 'a mysql server',
            'PORT': '',
        }
    }

You can also add a file called `main/templates/google_analytics.html` with
the Google Analytics code if you want.

## Dependencies ##

* [Django 1.3](http://pypi.python.org/pypi/Django/)
* [South](http://pypi.python.org/pypi/South)
* [Python-markdown](http://pypi.python.org/pypi/Markdown)