{% comment "This comment section will be deleted in the generated project" %}

A minimalistic django(1.8) template. A one time setup script is also bundled.

How to Start?

```
$ django-admin.py startproject --template=django-starter-skeleton.zip --extension=py,md,html,sh my_project
$ cd my_project
$ chmod 755 scripts/configure.sh
$ ./scripts/configure.sh
```

To generate `SECRET_KEY`, run `scripts/generate_secret_key.sh` and replace it in settings


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
