#!/bin/bash

# cd ..

echo "Creating virtual env"
virtualenv --no-site-packages pyenv

echo "Activating virtual env"
source pyenv/bin/activate

echo "Installing requirements"
pip install -r requirements/dev.txt

# changing root directory
cd "src"

# before running collectstatic, make sure that
# `root_dir/static` exists

mkdir "{{project_name}}/static"
echo "Creating Static directory"
if [ ! -d "static" ]; then
    mkdir "static"
fi

echo "Collecting static files"
python manage.py collectstatic --noinput

echo "Running migrations"
python manage.py migrate --noinput
