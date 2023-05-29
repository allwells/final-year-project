#!/bin/bash

set -x

# Run tailwindcss with watch mode and go to background
# tailwindcss -i ./app/static/src/css/input.css -o ./app/static/dist/css/output.css --watch &
yarn watch &

flask run

trap 'pkill -ef tailwind' exit
