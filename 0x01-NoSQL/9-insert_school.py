#!/usr/bin/env python3
""" Module for using PyMongo """


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document into the specified collection
    based on the provided keyword arguments (kwargs).

    Parameters:
        mongo_collection (pymongo.collection.Collection): The MongoDB collection to insert the document into.
        **kwargs: Keyword arguments representing the fields and values for the new document.

    Returns:
        The ObjectId of the newly inserted document.
    """
    inserted_document = mongo_collection.insert_one(kwargs)
    inserted_id = inserted_document.inserted_id

    return inserted_id
