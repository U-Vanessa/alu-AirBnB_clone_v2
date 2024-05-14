import json
from models.base_model import BaseModel


class FileStorage:
    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        return self.__objects
    

    def new(self, obj):
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    
    def save(self):
        new_dict = {}

        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()

        try:
            with open(self.__file_path, 'w') as file:
                json.dump(new_dict, file, indent=2)
        except FileNotFoundError:
            pass

    
    def reload(self, BaseModelClass):  # Pass BaseModel class as parameter
        try:
            with open(self.__file_path, 'r') as file:
                obj_dict = json.load(file)

                for key, value in obj_dict.items():
                    class_name = value['__class__']
                    cls = eval(class_name) if class_name in globals() else BaseModelClass
                    self.__objects[key] = cls(**value)

        except FileNotFoundError:
            pass
