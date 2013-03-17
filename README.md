# A jobs website #

This is a simple job-posting website written using Django and Bootstrap.  Its
neatest feature is that it automatically Tweets jobs when they're approved,
and readers can sign up to spread the word by automatically re-tweeting those
tweets.

It's made public under an MIT License.

## Configuration ##

Check out the source, then create four files in the root:

`sitename_settings.py`:

    JOBS_BOARD_TITLE = "Jimbo's site for Python jobs"
    JOB_TYPE_DESCRIPTION = "Python Jobs"

`email_settings.py`:

    EMAIL_SUBJECT_PREFIX = "[Some Kind Of Jobs] "
    EMAIL_HOST = "smtp.gmail.com"
    EMAIL_HOST_USER = "something@gmail.com"
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    EMAIL_HOST_PASSWORD = "some kind of password"

`db_settings.py`:

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'jobsboard_db',
            'USER': 'jobsboard_user',
            'PASSWORD': 'a password',
            'HOST': 'a mysql server',
            'PORT': '',
        }
    }

`twitter_settings.py`:

    # For the job-tweeting Twitter app
    APP_CONSUMER_KEY = 'blah blah'
    APP_CONSUMER_SECRET = 'blah blah'

    # For your job board's own twitter account
    OWN_TWITTER_ACCOUNT_ID = "myjobsboardtwitterid"
    OWN_TWITTER_ACCOUNT_ACCESS_KEY = 'blah blah'
    OWN_TWITTER_ACCOUNT_ACCESS_SECRET = 'blah blah'

    TWITTER_HASHTAGS = "#somekind #job"

Next, add a file called `main/templates/google_analytics.html`; this can contain
with the Google Analytics code if you want, or should otherwise be empty.

Next, sync the DB and migrate it to bring it up to date:

    19:03 ~/jobsboard (master)$ ./manage.py syncdb
    19:11 ~/jobsboard (master)$ ./manage.py migrate


## Dependencies ##

* [Django 1.3](http://pypi.python.org/pypi/Django/)
* [South](http://pypi.python.org/pypi/South)
* [Python-markdown](http://pypi.python.org/pypi/Markdown)
