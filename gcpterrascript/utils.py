"""utility file - common function defs
"""
import os
import json 

#TODO allow jwt token 
def get_credentials(env=True):
    """gets gcp credentials right now will default to GOOGLE_APPLICATION_CREDENTIALS

    Args:
        env (bool, optional): placeholder for now. Defaults to True.
    """
    if env:
        return os.environ['GOOGLE_APPLICATION_CREDENTIALS']