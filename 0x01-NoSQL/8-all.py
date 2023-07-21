#!/usr/bin/python3
""" Python function that lists all documents in a collection"""


def list_all(mongo_collection):
    """List all collection"""
    if not mongo_collection:
        return []
    docs = mongo_collection.find()
    return [i for i in docs]
