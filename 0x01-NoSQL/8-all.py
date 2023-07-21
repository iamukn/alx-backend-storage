#!/usr/bin/env python3
""" Python function that lists all documents in a collection"""


import pymongo


def list_all(mongo_collection):
    """List all collection"""
    if not mongo_collection:
        return []
    docs = mongo_collection.find()
    return [i for i in docs]
