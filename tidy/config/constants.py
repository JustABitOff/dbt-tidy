from os import environ
from pathlib import Path


TIDY_CONFIG_PATH = Path(environ.get("TIDY_CONFIG_PATH", "tidy.yaml"))
