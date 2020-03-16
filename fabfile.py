# TODO: DON'T COMMIT

from fabric import task
from invoke import run as local

conda = "/c/Tools/anaconda3/etc/profile.d/conda.sh"
prefix = "./api_env"


@task
def create_env(c):
    print("Creating environment...")
    c.run("{} env create -f environment.yml --prefix {}".format(conda, prefix))


@task
def export_env(c):
    print("Exporting environment...")
    c.run("conda env export > environment.yml")


@task
def update(c):
    print("Updating environment...")
    c.run("conda env update -p {} --file environment.yml".format(prefix))


@task
def activate(c):
    print("Activating environment {}".format(prefix))
    # c.run("source {}".format(conda))
    local("conda activate {}".format(prefix))
