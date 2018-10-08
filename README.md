{% comment "This comment section will be deleted in the generated project" %}

## Django Starter Skeleton

A minimalistic django(2.0) template. A one time setup script is also bundled.

### How to Start?

```
django-admin.py startproject --template=https://github.com/taranjeet/django-starter-skeleton/archive/master.zip --extension=py,md,html,sh,json my_project
cd my_project
chmod -R 755 scripts/*
./scripts/configure.sh
```

To generate `SECRET_KEY`, run `scripts/generate_secret_key.sh` and replace it in settings

### Support

Right now two version of Django namely v1.10(python 2.7) and v2.0(python 3) are supported. v1.10 is currently referenced via [django-1.10-python-2.7](https://github.com/taranjeet/django-starter-skeleton/tree/django-1.10-python-2.7) branch. v2.0 is the [master](https://github.com/taranjeet/django-starter-skeleton/tree/master) branch.

```
# for django v1.10
django-admin.py startproject --template=https://github.com/taranjeet/django-starter-skeleton/archive/django-1.10-python-2.7.zip --extension=py,md,html,sh,json my_project

# for django v2.0
django-admin.py startproject --template=https://github.com/taranjeet/django-starter-skeleton/archive/master.zip --extension=py,md,html,sh,json my_project
```

### Customizations

#### How to add support for mysql

Install [mysqlclient](https://pypi.org/project/mysqlclient/) and libmysqlclient-dev. Configure the following values in your environment.

```
DB_ENGINE='django.db.backends.mysql'
DB_NAME='dbname'
DB_USER='dbuser'
DB_PASSWORD='dbpass'
DB_HOST='localhost'
DB_PORT=3306
```

{% endcomment %}
# {{project_name}}

Created using Django.

## Setup Instructions

First make sure that you have the following installed.

* Python 3 and virtualenv

Now do the following to setup project

```
# assuming that the project is already cloned.

cd my_project

# one time
virtualenv -p $(which python3) pyenv

source pyenv/bin/activate

# one time or whenever any new package is added.
pip install -r requirements/dev.txt

# update settings
cp src/myproject/settings/local.sample.env src/myproject/settings/local.env

# generate a secret key or skip(has a default value) and then replace the value of `SECRET_KEY` in environment file
./scripts/generate_secret_key.sh

# update relevant variables in environment file

# run migrate
cd src
python manage.py migrate
```

To access webserver, run the following command

```
cd src
python manage.py runserver
```
