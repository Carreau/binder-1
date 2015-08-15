import os

if "BINDER_HOME" not in os.environ:
    raise Exception("BINDER_HOME environment variable must be set")

ROOT = os.environ["BINDER_HOME"]
DOCKER_HUB_USER = "andrewosh"
REGISTRY_NAME = "gcr.io/generic-notebooks"
