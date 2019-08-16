{% comment "This comment section will be deleted in the generated project" %}

## Django Starter Skeleton

A minimalistic django(2.0) template. A one time setup script is also bundled.

### How to Start?

```bash
django-admin.py startproject --template=https://github.com/taranjeet/django-starter-skeleton/archive/master.zip --extension=py,md,html,sh,json --name=Makefile my_project

# next look into setup instructions section
```

To generate `SECRET_KEY`, run `scripts/generate_secret_key.sh` and replace it in settings

### Support

Right now two version of Django namely v1.10(python 2.7) and v2.0(python 3) are supported. v1.10 is currently referenced via [django-1.10-python-2.7](https://github.com/taranjeet/django-starter-skeleton/tree/django-1.10-python-2.7) branch. v2.0 is the [master](https://github.com/taranjeet/django-starter-skeleton/tree/master) branch.

```bash
# for django v1.10
django-admin.py startproject --template=https://github.com/taranjeet/django-starter-skeleton/archive/django-1.10-python-2.7.zip --extension=py,md,html,sh,json my_project

# for django v2.0
django-admin.py startproject --template=https://github.com/taranjeet/django-starter-skeleton/archive/master.zip --extension=py,md,html,sh,json --name=Makefile my_project
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

#### Uwsgi Config

```
[uwsgi]
uid = ubuntu
gid = ubuntu

chdir = /home/ubuntu/demo-app/src
home = /home/ubuntu/demo-app/pyenv
module = demoapp.wsgi:application
env = DJANGO_SETTINGS_MODULE=demoapp.settings.live
master = true
processes = 3
socket = /run/uwsgi/demoapp.sock
logto = /var/log/uwsgi/demoapp.log
chown-socket = ubuntu:ubuntu
chmod-socket = 664
vacuum = true
```

#### Nginx Config

```
server{
    listen 80;
    server_name server_ip_or_web_address;

    location / {
            include uwsgi_params;
            uwsgi_pass unix:/run/uwsgi/demoapp.sock;
    }

    location /static {
            root /home/ubuntu/demo-app/src;

    }

    location /media {
            root /home/ubuntu/demo-app/src;
    }
}
```
{% endcomment %}
# {{project_name}}

Created using Django.

## Setup Instructions

First make sure that you have the following installed.

* Python 3 and virtualenv

Now do the following to setup project

```bash
# assuming that the project is already cloned.

cd {{project_name}}

# one time
virtualenv -p $(which python3) pyenv

source pyenv/bin/activate

# one time or whenever any new package is added.
pip install -r requirements/dev.txt

# update settings
cp src/{{project_name}}/settings/local.sample.env src/{{project_name}}/settings/local.env

# generate a secret key or skip(has a default value) and then replace the value of `SECRET_KEY` in environment file(here local.env)
./scripts/generate_secret_key.sh

# update relevant variables in environment file

# run migrate
cd src
python manage.py migrate
```

To access webserver, run the following command

```bash
cd src
python manage.py runserver
```
