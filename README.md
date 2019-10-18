# boxioffice

> A combination online box office and actor database django webapp

## Setup

Create a .env file:

```bash
SECRET_KEY=
ALLOWED_HOSTS=
DEBUG=True
ISLOCAL=True
SOCIAL_AUTH_GITHUB_KEY=
SOCIAL_AUTH_GITHUB_SECRET=
AWS_STORAGE_BUCKET_NAME=
AWS_S3_REGION_NAME=
AWS_S3_ENDPOINT_URL=
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
MAILGUN_API_KEY=
MAILGUN_SMTP_SERVER=
MAILGUN_SMTP_LOGIN=
MAILGUN_SMTP_PASSWORD=
MAILGUN_BASE_URL=
STRIPE_SECRET_KEY=
STRIPE_PUBLISHABLE_KEY=
```

Setup the db:

You should be able to simply run the `automigrate.py` program.

## Handy notes

[Cookbook](https://github.com/nigma/heroku-django-cookbook/blob/master/README.md)

[Heroku config with ease](https://github.com/sdkcodes/heroku-config)

## Authors

[Jack Timmins](https://github.com/Tim-Jackins)
