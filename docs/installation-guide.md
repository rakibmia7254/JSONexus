# Installation Guide

### Requirements

Before installing JSONexus, make sure you have the following prerequisites:

* Python 3.x installed on your system.
* Pip package manager installed.

### Installation Steps

#### 1. Create a Virtual Environment (Optional)

It's recommended to create a virtual environment to isolate the dependencies of JSONexus. Run the following command in your terminal to create a virtual environment named `jsonexus-env`:

```bash
python3 -m venv jsonexus-env
```

Activate the virtual environment:

* **On Windows:** `jsonexus-env\Scripts\activate`
* **On macOS and Linux:** `source jsonexus-env/bin/activate`

#### 2. Install JSONexus

Once the virtual environment is activated, you can install JSONexus using pip. Run the following command:

```bash
pip install jsonexus
```

#### 3. Verify Installation

After installation, you can verify that JSONexus is installed correctly by importing it in a Python script:

```python
from jsonexus import JSONexus
```

If no errors occur, JSONexus is successfully installed on your system.

#### 4. Start Using JSONexus

You're now ready to start using JSONexus for working with JSON-based databases in your Python projects. Refer to the [documentation](./) for usage instructions and API reference.

### Additional Resources

* [JSONexus Documentation](./): Detailed documentation on using JSONexus.
