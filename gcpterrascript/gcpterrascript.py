"""Main module."""
import json
import terrascript
import terrascript.provider
import terrascript.resource
import gcpterrascript.utils
import os

TF_FILES = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'files')
print(TF_FILES)

class Gcptf:
    """ terraform for gcp """
    def __init__(self, credentials, project, region="us-central1"):
        self.region = region
        self.credentials = credentials
        self.project = project
        self.provider = "google"
        config = terrascript.Terrascript()
        config += terrascript.provider.google(**self.__dict__)
        self.config = config
    
    
    def write_terraform(self, filename):
        with open(filename, "w") as fopen:
            json.dump(self.config, fopen, indent=2, sort_keys=False)


class 