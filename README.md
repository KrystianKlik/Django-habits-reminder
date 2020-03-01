# Django-habits-reminder

## Important

To make sending email avaible you need to go to settings.py and change some of this lines

```
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'krystianklik@gmail.com'
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASSWORD')
```

If you want to use Gmail just change `EMAIL_HOST_USER` and `EMAIL_HOST_PASSWORD`. Remember to allow less secure app to work on your gmail https://myaccount.google.com/lesssecureapps

### TypeScript

In order to run typescript just navigate to habits/typescript in console and type tsc -w

### Heroku and Celery

I did manage to run heroku and run workers with functions that I create but somehow it doesn't do anything. For better understaning check admin page

### SCSS

Sass is compiled on page load and you can find it in templates/habits/base.html in line
```
{% load sass_tags %}
<link href="{% sass_src 'main.scss' %}" rel="stylesheet" type="text/css" />
```

### Database

I'm using [ElephantSQL]('https://www.elephantsql.com/')