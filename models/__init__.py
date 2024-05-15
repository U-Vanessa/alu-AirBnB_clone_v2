from engine.file_storage import FileStorage

# Create a unique FileStorage instance
storage = FileStorage()

print(storage)
# Call reload() method to load data from JSON file
storage.reload()