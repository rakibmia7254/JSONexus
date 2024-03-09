# Data Modeling in JSONexus

JSONexus allows you to model your data flexibly using JSON documents, providing a schema-less approach to database design.

### 1. Document-based Modeling

JSONexus follows a document-based data model, where each record is represented as a JSON document. This approach allows for flexible schema design and easy scalability.

### 2. Example

Suppose we have a collection of users with the following attributes:

```json

        {
            users: [
                {
                    name: "Alice",
                    age: 30,
                    email: "alice@example.com",
                    "_id": "6b72a5d2-6f95-4e49-a152-e24e4415fc0e"
                },
                {
                    name: "Bob",
                    age: 25,
                    email: "bob@example.com",
                    "_id": "e24e4415fc0e-6f95-4e49-a152-e24e4415fc"
                },
                {
                    name: "Charlie",
                    age: 35,
                    email: "charlie@example.com",
                    "_id": "f85fb55f-10a8-409f-bdd1-ffdc850c67be"
                }
            ]
        }
    
```

This JSON document represents a user with a name, age, and email. You can store and query such documents in JSONexus without defining a fixed schema.

### 3. Additional Resources

Refer to the [documentation](./) for detailed information on data modeling, including best practices and examples.
