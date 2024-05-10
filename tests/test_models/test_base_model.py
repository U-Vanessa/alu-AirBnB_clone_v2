import unittest
import time
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.model = BaseModel()


    def test_instance(self):
        self.assertIsInstance(self.model, BaseModel)


    def test_uniqueUUID(self):
        model2 = BaseModel()
        self.assertNotEqual(self.model, model2)


    def test_dict(self):
        model_dict = self.model.to_dict()
        self.assertEqual(type(model_dict), dict)
        self.assertIn('__class__', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')

    
    def test_str_representation(self):
        str_repr = str(self.model)
        self.assertIn('[BaseModel]',str_repr)
        self.assertIn('id', str_repr)
        self.assertIn('created_at', str_repr)
        self.assertIn('updated_at', str_repr)


    def test_save_updates_updated_at(self):
        # Create an instance of BaseModel
        model = BaseModel()

        # Get the initial updated_at timestamp
        initial_updated_at = model.updated_at

        # Call the save method
        model.save()

        # Get the updated updated_at timestamp
        updated_updated_at = model.updated_at

        # Assert that updated_at has been updated
        self.assertNotEqual(initial_updated_at, updated_updated_at)

        # Assert that the new updated_at is approximately now
        # We use a small sleep to ensure that time has passed between save and checking
        time.sleep(0.001)
        now = datetime.now()
        self.assertAlmostEqual(updated_updated_at, now, delta=datetime.timedelta(seconds=1))
    


if __name__ == '__main__':
    unittest.main()
