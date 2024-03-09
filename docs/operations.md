# Operations

### Functions in JSONexus

JSONexus provides various functions to manipulate and query data in the database.

### 1. Insert

Insert a new document into a collection.

```python

 db.insert('users', {'name': 'Alice', 'age': 30, 'email': 'alice@example.com'})
    
```

### 2. Find

Find documents that match a specified query.

```python

result = db.find('users', {'age': {'_op': '$eq', '_value': 35}})
    
```

### 3. Update

Update documents that match a specified query.

```python

db.update('users', {"age": {'_op': '$eq', '_value': 23}}, {"job": "Junior DEV"}

```

### 4. Delete

Delete documents that match a specified query.

```python

  db.delete('users', {'name': {'_op': '$eq', '_value': "Alice"}})
  
```

### 5. Count

Count the number of documents in a collection.

```python

 count = db.count('users')
    
```

### 6. Get Collection

Get all documents in a collection.

```python

collection = db.get_collection('users')
    
```

### 7. Get Document

Get a single document from a collection.

```python

  document = db.get_document('users', '6b72a5d2-6f95-4e49-a152-e24e4415fc0e')
    
```

### 8. Drop Collection

Drop a collection from the database.

```python

 db.drop_collection('users')
    
```

###

### 9. Insert Many

Insert multiple documents into a collection.

```python
db.insert_many('users', [
    {'name': 'Alice', 'age': 30, 'email': 'alice@example.com'},
    {'name': 'Bob', 'age': 25, 'email': 'bob@example.com'},
    {'name': 'Charlie', 'age': 35, 'email': 'charlie@example.com'}
])
```

### 10. Additional Resources

Refer to the [documentation](./) for detailed usage instructions, API reference, and examples.
