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

### Database Models

For now, this boilerplate only supports the use of [MongoDB](https://www.mongodb.com/) via [mongoengine](http://mongoengine.org/) which is a Document-Object Mapper (like an ORM for MYSQL databases) for working with MongoDB in Python.

New document models are added in the `app.main.models` package.

The benefit of using a Document-Object Mapper is it provides an abstraction layer over top of your NoSQL database of choice with built in save/delete functionality as well as persistent object store with query and filtering capabilities.

For example, if you have an instance of the `Client` document model, you automatically have access all documents stored in the `client` container. They can be retrieved by calling:

```python
from app.main.models.client import Client
all_clients = Client.objects().all()
```

Alternatively, you can access a single client by client_id:

```python
from bson.objectid import ObjectId
from app.main.models.client import Client
client_id = ObjectId("5e6fc3128611120971f673f2")
client = Client.objects(id=client_id).first()
```

Refer to the [mongoengine documentation](https://mongoengine-odm.readthedocs.io/) for any additional details.

### Services

Services are static methods, or a collection of static methods via a class, that are intended to implement application functionality. They are to live within the `app.main.services` package.

More often they are used to access and process data to and from the database, such as the `client_service`, but sometimes can also be used for generic functionality, such as retrieving the currently authenticated client.

### Utilities

The `app.main.utilities` packages is intended to be used for any utility functionality such as Date utility functions (if it weren't already baked into python).

Initially, it includes the definition of data transfer objects (DTOs) that define the namespaces and models that make up the Rest API. 

## Authentication

API authentication is imperative to help ensure the security of client/user data in any application. 

To this end, we are using the [flask_jwt_extended](https://flask-jwt-extended.readthedocs.io/en/stable/) package to automatically manage endpoint authentication.

To authenticate, a user will need to retrieve an `access_token` via an `/authorize` endpoint. This endpoint, or any like it, will request user/client credentials and return an `access_token` on successful authentication.

The user will then provide the `access_token` via the `Authorization` header, prefixed the by the key term `Bearer`, when making any API requests that require authentication.

Endpoints are deemed to require authentication by adding the `@jwt_required` decorator to individual resource methods.

Because [JWT Tokens](https://jwt.io/) are being used for authentication, you can store any data you want to be accessibly via authenticated routes by specifying it via the `identity` argument when creating an access token during authentication.