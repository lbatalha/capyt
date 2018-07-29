import os

name = "capyt"

with open(os.path.join(os.path.dirname(os.path.abspath( __file__ )), "VERSION")) as version_file:
    version = version_file.read().strip()
__version__ = version
