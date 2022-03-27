#!/usr/bin/env bash

set -ex

echo "Applying migrations..."
echo $SQLALCHEMY_DATABASE_URI

flask db upgrade

echo "migrations ok"

exec "$@"