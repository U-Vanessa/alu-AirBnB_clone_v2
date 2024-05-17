In this project, we will develop the console component of an AirBnB clone. Our primary goal is to create a command interpreter to manage AirBnB objects. The project involves several key steps:

# BaseModel Implementation:

Develop a parent class, BaseModel, responsible for the initialization, serialization, and deserialization of instances.
Establish a straightforward flow for serialization and deserialization:
Instance ↔ Dictionary ↔ JSON string ↔ File

## Class Creation:

Design all classes required for AirBnB (e.g., User, State, City, Place), ensuring they inherit from BaseModel.

### Storage Engine:

Implement the initial storage engine, focusing on file storage.

### Unit Testing:

Create comprehensive unittests to validate the functionality of all classes and the storage engine.
Command Interpreter Capabilities
Our command interpreter will provide the following functionalities:

### Object Creation:

Create new instances of objects (e.g., User, Place).

### Object Retrieval:

Retrieve objects from various storage sources (e.g., files, databases).

### Object Operations:

Perform operations on objects such as counting and computing statistics.

### Attribute Updates:

Update attributes of existing objects.

### Object Destruction:

Delete objects.
