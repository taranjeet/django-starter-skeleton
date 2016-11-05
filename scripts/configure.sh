#!/bin/bash

# cd ..

echo "Creating virtual env"
virtualenv --no-site-packages pyenv

echo "Activating virtual env"
source pyenv/bin/activate

echo "Installing requirements"
pip install -r requriements/dev.txt



if [ -f "bower.json" ]; then
    # before running bower install,
    # make sure {{project_name}}/static/bower_components exists

    if [ ! -d "{{project_name}}/static/bower_components" ]; then
        mkdir -p "{{project_name}}/static/bower_components"
    fi

    # create `.bowerrc` dynamically, so that template variable
    # project_name is substituted properly

cat <<'EOF' > ".bowerrc"
{
    "directory": "{{project_name}}/static/bower_components"
}
EOF
    echo "Running bower install"
    bower install
fi

# before running collectstatic, make sure that
# `root_dir/static` exists

if [ ! -d "static" ]; then
    mkdir "static"
fi

echo "Collecting static files"
python manage.py collectstatic --noinput

echo "Running migrations"
python manage.py migrate --noinput
