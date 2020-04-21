#!/bin/bash

PREFIX=./api_env

usage() {
  echo -n "./app.sh [OPTION]...

 Options:
  -e, --export      Export the conda environment
  -i, --init        Initialize the application
  -s, --secrets     Generate application secrets
  -u, --update      Update the conda environment
  -t, --test        Run test suite
  -h, --help        Display this help and exit
"
}

if [ $# -gt 0 ]; then
  while [ "$1" != "" ]; do
    case $1 in
      -i | --init )
        echo "Initializing application"
        # Create local config file if it doesn't already exist
        EXAMPLE_FILE=./app/main/config/example.local.cfg
        FILE=./app/main/config/local.cfg
        if [ -f "$EXAMPLE_FILE" ] && [ ! -f "$FILE" ]; then
          echo "Creating local configuration file."
          cp "$EXAMPLE_FILE" "$FILE"
        fi

        # Create conda environment
        if [ ! -d "$PREFIX" ]; then
          echo "Creating conda environment"
          conda env create -f environment.yml --prefix "$PREFIX"
        fi
        ;;
      -u | --update )
        echo "Updating conda environment"
        conda env update -p "$PREFIX" --file environment.yml
        ;;
      -t | --test )
        echo "Running test suite"
        python -m unittest discover -s ./app/main/tests/
        ;;
      -e | --export )
        echo "Exporting conda environment"
        conda env export > environment.yml
        ;;
      -s | --secrets )
        python generate_secrets.py
        ;;
      -h | --help )
        usage
        ;;
    esac
    shift
  done
else
  echo "No arguments were provided.
  "
  usage
fi
