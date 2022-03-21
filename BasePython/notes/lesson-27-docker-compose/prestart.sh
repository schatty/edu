#!/usr/bin/env bash

set -ex

echo "Apply migrations"

flask db upgrade

echo "migrations ok"

exec "$@"