JSONexus
========

JSONexus is a lightweight and flexible database solution designed for modern applications. It provides a simple and intuitive way to store, query, and manipulate data using JSON documents.

Key Features
------------

*   Document-based storage
*   Flexible schema-less design
*   Powerful query capabilities
*   Easy integration with various platforms

Installation
------------

You can install JSONexus using pip:

    pip install jsonexus

Getting Started
---------------

Check out the [documentation](https://jsonexus.gitbook.io/jsonexus/) for detailed usage instructions, API reference, and examples.

Usage
-----

### Local Storage

```python
    from jsonexus import JSONexus
    
    # Create a local database
    db = JSONexus('data/db.json')
    
    # Insert a document
    db.insert('users', {'
    name': 'Alice', 
    'age': 30, 'email': 'alice@example.com'
    })
    
    # Find documents
    result = db.find('users', {"age": {'_op': '$gte', '_value': 25}})
    
    # Update a document
    db.update('users', {"name": {'_op': '$eq', '_value': 'Alice'}, {'age': 35})
    
    # Delete a document
    db.delete('users', {"name": {'_op': '$eq', '_value': 'Alice'}})
    
    # Count documents
    count = db.count('users')
```
        

Documentation
-------------

The documentation for JSONexus can be found in the [Documentation](https://jsonexus.gitbook.io/jsonexus/) directory. It includes detailed usage instructions, API reference, and examples.

About
-----

JSONexus is an open-source project hosted on GitHub. You can contribute to the project, report issues, and request features on the GitHub repository

License
-------

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

# New Features

- **deleteby_id**: Allows users to delete an item from a collection by its unique identifier.
- **updateby_id**: Enables users to update an item in a collection based on its unique identifier.
- **insert_no_duplicate**: Adds functionality to insert items into a collection without duplicates.
- **check_duplicate**: Provides a method for checking whether a duplicate item exists in a collection.

  # Update
  I replaced json with orjson for faster operation
  
  So, compared to Orjson:
  Old JSONexus is approximately `17.70` times slower.
  SQLite is approximately `5.366` times slower.
