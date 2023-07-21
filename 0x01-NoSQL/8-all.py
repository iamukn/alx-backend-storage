#!/usr/bin/python3
""" Python function that lists all documents in a collection"""


def list_all(mongo_collection):
    """List all collection"""

    return mongo_collection.find()
