#!/usr/bin/env python3

'''A Python module that provides statistics about nginx logs'''

from pymongo import MongoClient


if __name__ == '__main__':
    '''Prints statistics about the nginx logs collection'''

    # Connect to the MongoDB server running on localhost
    con = MongoClient('mongodb://localhost:27017')

    # Access the 'nginx' collection within the 'logs' database
    collection = con.logs.nginx

    # Print the total number of logs in the collection
    print(f'{collection.estimated_document_count()} logs')

    # Define a list of HTTP methods to analyze
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    print('Methods:')

    # Iterate through the methods and print the count of logs for each method
    for req in methods:
        print('\tMethod {}: {}'.format(req,
              collection.count_documents({'method': req})))

    # Print the count of logs with 'GET' method and path '/status'
    print('{} status check'.format(collection.count_documents(
          {'method': 'GET', 'path': '/status'})))
