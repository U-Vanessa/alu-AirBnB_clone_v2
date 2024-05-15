import uuid
import datetime

class BaseModel:
    def __init__(self, *args, **kwargs):
        """ Defines common attributes:
            id: string - UUID assigned at instance creation.
            created_at: datetime - set to current datetime at instance creation.
            updated_at: datetime - set to current datetime at instance creation, updated on object change. """
        
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        setattr(self, key, datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                    else: 
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            from models import storage  # Local import to avoid circular import
            storage.new(self)

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        from models import storage  # Local import to avoid circular import
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """ Return a dictionary representing the class instance. """
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = datetime.datetime.isoformat(my_dict["created_at"])
        my_dict["updated_at"] = datetime.datetime.isoformat(my_dict["updated_at"])
        return my_dict

# Example usage for testing:
if __name__ == "__main__":
    import os
    import sys

    # Add the project root to PYTHONPATH
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if project_root not in sys.path:
        sys.path.append(project_root)

    from models.base_model import BaseModel
    p = BaseModel()
    print(p)
