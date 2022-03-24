#!/usr/bin/env bash

set -ex

echo "Applying migrations..."

flask db upgrade

echo "migrations ok"

exec "$@"