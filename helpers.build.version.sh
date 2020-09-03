#!/bin/bash
# helpers.build.version.sh

# if there is no .git folder, we cannot get the version or the commit hash
if [ -d ".git" ]; then
    # get the values
    export git_version="$(git describe)"
    export git_commit="$(git rev-parse HEAD)"

    # print some statements
    echo "helpers.build.version.sh writing to version.json"
    echo "version: ${git_version}"
    echo "git_commit: ${git_commit}"

    # create a json string
    version_json="{\"version\":\"${git_version}\",\"git_commit\":\"${git_commit}\"}"

    # write to a new version.json file
    echo "${version_json}" > version.json
else
    echo "WARNING: .git folder does not exist, not exporting version.json"
fi;
