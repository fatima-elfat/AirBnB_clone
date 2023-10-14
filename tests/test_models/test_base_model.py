#!/usr/bin/python3
"""
Unittest for BaseModel.
"""
from time import sleep
import unittest
import os
from models.base_model import BaseModel

class TestBaseModelClass(unittest.TestCase):
    '''Testing BaseModel Class

    '''

    @classmethod
    def setUp(cls):
        cls.my_model = BaseModel()
        cls.my_model.name = "My First Model"
        cls.my_model.my_number = 89

    @classmethod
    def tearDown(cls):
        del cls.my_model

    def test_docstrings(self):
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_init(self):
        self.assertTrue(isinstance(self.my_model, BaseModel))
        self.assertEqual(self.my_model.created_at, self.my_model.updated_at)

    def test_save(self):
        sleep(0.08)
        self.my_model.save()
        self.assertNotEqual(self.my_model.created_at, self.my_model.updated_at)

    def test_save_with_arg(self):
        self.my_model = BaseModel()
        with self.assertRaises(TypeError):
            self.my_model.save(None)

    def test_save_updates_file(self):
        self.my_model.save()
        id = "BaseModel." + self.my_model.id
        with open("file.json", "r") as f:
            self.assertIn(id, f.read())

    def test_to_dict_check(self):
        self.assertNotEqual(self.my_model.to_dict(), self.my_model.__dict__)

    def test_to_dict(self):
        my_model_dict = self.my_model.to_dict()
        self.assertIsInstance(my_model_dict['created_at'], str)
        self.assertIsInstance(my_model_dict['updated_at'], str)
        self.assertEqual(self.my_model.__class__.__name__, 'BaseModel')

    def test_to_dict_strs(self):
        mdict = self.my_model.to_dict()
        self.assertEqual(str, type(mdict["created_at"]))
        self.assertEqual(str, type(mdict["updated_at"]))

    def test_to_dict_added_attr(self):
        self.assertIn("name", self.my_model.to_dict())
        self.assertIn("my_number", self.my_model.to_dict())

    def test_to_dict_arg(self):
        with self.assertRaises(TypeError):
            self.my_model.to_dict(None)

    def test_id_unique(self):
        my_model_ = BaseModel()
        self.assertNotEqual(self.my_model.id, my_model_.id)

    def test_diff_models_created_at(self):
        sleep(0.08)
        my_model_ = BaseModel()
        self.assertLess(self.my_model.created_at, my_model_.created_at)

    def test_diff_models_updated_at(self):
        sleep(0.08)
        my_model_ = BaseModel()
        self.assertLess(self.my_model.updated_at, my_model_.updated_at)


if __name__ == "__main__":
    unittest.main()