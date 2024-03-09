---
description: >-
  JSONexus is a lightweight and flexible database solution designed for modern
  applications. It provides a simple and intuitive way to store, query, and
  manipulate data using JSON documents.
---

# Getting Started

### 1. Installation

Follow the[ installation guide](./#id-1.-installation) to install JSONexus in your Python environment.

### 2. Import JSONexus

In your Python code, import JSONexus to start using it:

```python
from jsonexus import JSONexus
```

### 3. Create a Database

Create a new instance of JSONexus database by providing the name of the JSON file to store the database:

```python
db = JSONexus('example_db.json')
```

### 4. Perform Database Operations

Perform CRUD (Create, Read, Update, Delete) operations using JSON-based data:

* **Insert:** Add a new record to the database.
* **Find:** Find records in the database that match the specified query.
* **Delete:** Delete records from the database that match the specified query.
* **Update:** Update records in the database that match the specified query.

