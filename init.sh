#!/bin/sh

INIT_FILE=/var/lib/postgresql/data/initialized

if [ ! -f "$INIT_FILE" ]; then
    

    echo "Running init..."
    flask db init
    echo "Running db migrate..."
    flask db migrate -m "Initial migration"
    echo "Running db upgrade..."
    flask db upgrade

    touch "$INIT_FILE"
fi

exec "$@"
