#!/bin/bash

PREFIX=./api_env

usage() {
  echo -n "./app.sh [OPTION]...

 Options:
  -d, --dev             Run in development mode
  -e, --export          Export the conda environment
  -i, --init            Initialize the application
  -r, --run             Run the Flask server
  -s, --secrets         Generate application secrets
  -t, --test            Run test suite
  -u, --update          Update the conda environment
  -h, --help            Display this help and exit
  -vf, --versionfile    Produces version.json file
"
}

DEV=false
INIT=false
RUN=false
TEST=false
UPDATE=false

if [ $# -gt 0 ]; then
  while [ "$1" != "" ]; do
    case $1 in
      -i | --init )
        INIT=true
        ;;
      -u | --update )
        UPDATE=true
        ;;
      -d | --dev )
        DEV=true
        ;;
      -r | --run )
        RUN=true
        ;;
      -t | --test )
        TEST=true
        ;;
      -e | --export )
        echo "Exporting conda environment"
        conda env export > environment.yml
        ;;
      -vf | --versionfile )
        echo "Creating version.json file"
        source ./helpers.build.version.sh
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

# Initialize conda environment
if [ "$INIT" = true ]; then
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
fi

# Update the conda environment
if [ "$UPDATE" = true ]; then
  echo "Updating conda environment"
  conda env update -p "$PREFIX" --file environment.yml
fi

# Run the test suite
if [ "$TEST" = true ]; then
  echo "Running test suite"
  python manage.py test
fi

# Run the application server, either in dev or production
if [ "$DEV" = true ] || [ "$RUN" = true ]; then
  source activate $PREFIX
  if [ "$DEV" = true ]; then
    echo "Running the development server"
    python manage.py run_dev
  elif [ "$RUN" = true ]; then
    echo "Running the production server"
    python manage.py run
  fi
fi
