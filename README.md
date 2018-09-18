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


{% endcomment %}
# {{project_name}}

Created using Django.

Steps to get the project running

```
./scripts/configure.sh
```

To start the project

```
# assuming virtual environment is already active
python manage.py runserver
```
