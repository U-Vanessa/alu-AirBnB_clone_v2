import uuid
import datetime


class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()


    def __str__(self):
        return f"[Person] {self.id} {self.__dict__}"
    

    def save(self):
        self.updated_at = datetime.datetime.now()

    
    def to_dict(self):
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = "BaseModel"
        my_dict["created_at"] = datetime.datetime.isoformat(my_dict["created_at"])
        my_dict["updated_at"] = datetime.datetime.isoformat(my_dict["updated_at"])
        print(my_dict)





