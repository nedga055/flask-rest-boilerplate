# CDO Data Science Team Rest API Boilerplate

This repository is intended to act as a boilerplate for all CDO Data Science Team Python Rest APIs.

*TODO: Add note on how to bootstrap a Rest API project using custom CLI tool* 

**NOTE:** At this point, this project is intended to be fluid and up for discussion. The choices surrounding methodologies and technologies are not set in stone but are some initial recommendations. Feel free to open issues and add direct comments to code blocks.

## Bootstrap

Create a copy of `app/main/config/example.local.cfg`, change the name to `app/main/config/local.cfg` and update configuration variables as desired.

Run the following on the command line to generate application secrets:

```
python generate_secrets.py
```

*TODO: Could set up a bootstrap script that will automatically do the entire bootstrapping process via one command.*

## Conda Environment

To initialize the conda environment, run the following in the root project directory:

```
conda env create -f environment.yml --prefix ./api_env
```

Note the `--prefix ./api_env`. This creates the environment in the project directory in a folder called `api_env`.

This will result in a long prefix in your command prompt. To address this, run the following:

```
conda config --set env_prompt '({name})'
```

To activate the environment:

```
conda activate ./api_env
```

Deactivate:

```
conda deactivate
```

If you add any new packages via conda or pip, make sure to update the `environment.yml`:

```
conda env export > environment.yml
```

To ensure you have all the dependencies defined in the `environment.yml`, run:

```
conda env update -p ./api_env --file environment.yml
```

## Application Configuration

Application configuration is managed via `.cfg` files located in the `app.main.config` package.

Defaults are stored in the `defaults.cfg` file, while local overrides can be done via a `local.cfg` file. Don't include one at all if you simply want to use the defaults.

Configuration files are broken up into sections, each of which contains keys with values. Here's an example:

```.ini
[database]
host = 127.0.0.1
port = 27017
name = db_name
user = db_user
passw = db_pass
``` 

In this example, `[database]` is the section, while the lines below are keys and their values available as part of the database section. It's important to note that all values are automatically considered to be a string. So when processing them to be used, make sure to convert them to the proper type as necessary.

See python documentation on [ConfigParser](https://docs.python.org/3/library/configparser.html) for more details. **Note:** `.ini` files can be used in place of `.cfg` files. They are interchangeable.

If additional configuration needs to be added, either update existing config classes in the config package's `__init__.py`, or add a new class.

## Development

Development of an application based off of the flask_rest_boilerplate should fall into one of the following categories:

    - CLI Commands
    - Controllers (API Routes)
    - Database models
    - Services
    - Utilities
    
When adding new code, it is advisable to build within one of these sections, though it isn't required and this can be extended as desired. 

### CLI Commands

CLI commands are any tasks/functions that are intended to be run via the command line. For example, a command line tool for creating new clients.

They are managed via the `app.main.commands` package.

For more information on how commands are created and managed, check out the flask-script documentation on [creating and running commands](https://flask-script.readthedocs.io/en/latest/#creating-and-running-commands).

Registering new commands is done in the `app.main` packages `__init__.py` within the `create_manager` function.

### Controllers (API Routes)

Controllers are what manage the REST API routes, or what can sometimes be referred to as resources.

Every resource conforms to the CRUD methodology (Create, Read, Update, Delete) and therefore support the following functions:

    - get (read)
    - post (create)
    - put (update)
    - delete (delete)
    
To facilitate the development of proper REST conventions, we are using [flask-restx](https://flask-restx.readthedocs.io/en/latest/) which is a wrapper around [flask-restful](https://flask-restful.readthedocs.io/en/latest/).

The purpose of [flask-restx](https://flask-restx.readthedocs.io/en/latest/) is to provide additional decorators that are used to automatically generate [Swagger](https://swagger.io/) documentation which will be available via the root URL of the application (locally, this will be http://127.0.0.1:5000).

Each `app.main.controller` package contains multiple resources that will make up an API namespace.

API namespaces are defined via DTOs (Data Transfer Objects) within the `app.main.utils.dto` package, accessible via the controller and registered in the `app` package in the `__init__.py` file.

Models that define the different data maintained by an individual namespace are also defined via the DTOs.

