#!/bin/bash

set -e

python manage.py migrate

if [ -f electronics/fixtures/networknode_fixture.json ]; then
  python manage.py loaddata electronics/fixtures/networknode_fixture.json
fi

if [ -f electronics/fixtures/users_fixture.json ]; then
  python manage.py loaddata electronics/fixtures/users_fixture.json
fi

exec python manage.py runserver 0.0.0.0:8000
