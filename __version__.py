'''
__version__.py file

Imports version information from a version.json file with the following form:

{"version": "<git version tag>", "git_commit": "<git commit hash>"}

Sets the following variables:
__VERSION__: The version (tag) of the project
__GIT_COMMIT__: The hash associated with the current commit.
'''
from os import path
import json

from app.main.errors.api_errors import MissingVersionError

# Import version JSON
version_file = path.abspath(path.join(path.dirname(__file__), "version.json"))
version_data = {}
try:
    with open(version_file, "r") as f:
        # Load the json from the loaded file
        version_data = json.load(f)
except FileNotFoundError:
    # Tell the user the version file is missing and how to create it.
    raise MissingVersionError("The version.json file is missing. Please run `./app.sh -vf`.")

# version (a.k.a the git tag)
try:
    __VERSION__ = version_data["version"]
except KeyError:
    # Re-raise the key error with a custom message.
    raise KeyError("The version.json is missing the version key. Please run `./app.sh -vf`.")

try:
    __GIT_COMMIT__ = version_data["git_commit"]
except KeyError:
    # Re-raise the key error with a custom message.
    raise KeyError("The version.json is missing the git_commit key. Please run `./app.sh -vf`.")
