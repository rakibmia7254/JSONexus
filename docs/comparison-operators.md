# Comparison Operators

JSONexus supports various comparison operators to perform advanced searches in the database. Here's a comparison between SQL queries and JSONexus queries:

### 1. Comparison Operators

* **$eq**: Matches values that are equal to a specified value.
* **$gt**: Matches values that are greater than a specified value.
* **$gte**: Matches values that are greater than or equal to a specified value.
* **$lt**: Matches values that are less than a specified value.
* **$lte**: Matches values that are less than or equal to a specified value.
* **$ne**: Matches all values that are not equal to a specified value.

### 2. Example

Suppose we have a collection of users with the following documents:

```json
[
    {'name': 'Alice', 'age': 30, 'email': 'alice@example.com'},
    {'name': 'Bob', 'age': 25, 'email': 'bob@example.com'},
    {'name': 'Charlie', 'age': 35, 'email': 'charlie@example.com'}
]
```

To find users older than 25, you can use the `$gt` operator as follows:

```python

 result = db.find('users', {"age": {'_op': '$gte', '_value': 25}})
    
```

This query will return documents for Alice and Charlie since their ages are greater than 25.

### 3. Comparison with SQL Queries

Here's how you would achieve the same result in SQL:

```sql

[SQL] SELECT * FROM users WHERE age > 25;
[JSONexus] db.find('users', {"age": {'_op': '$gt', '_value': 25}})

[SQL] SELECT * FROM users WHERE age >= 25;
[JSONexus] db.find('users', {"age": {'_op': '$gte', '_value': 25}})

[SQL] SELECT * FROM users WHERE age < 25;
[JSONexus] db.find('users', {"age": {'_op': '$lt', '_value': 25}})

[SQL] SELECT * FROM users WHERE age <= 25;
[JSONexus] db.find('users', {"age": {'_op': '$lte', '_value': 25}})

[SQL] SELECT * FROM users WHERE age != 25;
[JSONexus] db.find('users', {"age": {'_op': '$ne', '_value': 25}})

[SQL] SELECT * FROM users WHERE age = 25;
[JSONexus] db.find('users', {"age": {'_op': '$eq', '_value': 25}})
```

Both JSONexus queries and SQL queries provide ways to filter data based on certain conditions, but JSONexus queries use a JSON-like syntax, while SQL queries use a more structured SQL syntax.
