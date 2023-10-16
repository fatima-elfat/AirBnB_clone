#!/usr/bin/python3
"""
the unittests for FileStorage.
"""

from models.engine.file_storage import FileStorage
import unittest
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User
import os
import models


class TestFileStorage(unittest.TestCase):
    "represent unittest for FileStorage"

    @classmethod
    def setUp(self):
        """
        set up method.
        """
        try:
            os.rename("file.json", "test_file.json")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        """
        tear down method.
        """
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("test_file.json", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_all(self):
        """
        test the function all.
        """
        self.assertIsNotNone(models.storage.all())
        self.assertEqual(dict, type(models.storage.all()))
        self.assertIs(
            models.storage.all(),
            models.storage._FileStorage__objects
            )

    def test_new(self):
        """
        test the function new.
        """
        st = models.storage
        a, b, c = Amenity(),  BaseModel(), City()
        p, r, s = Place(), Review(), State()
        u = User()
        st.new(a)
        self.assertIn("Amenity." + a.id, models.storage.all().keys())
        self.assertIn(a, models.storage.all().values())
        st.new(b)
        self.assertIn("BaseModel." + b.id, models.storage.all().keys())
        self.assertIn(b, models.storage.all().values())
        st.new(c)
        self.assertIn("City." + c.id, models.storage.all().keys())
        self.assertIn(c, models.storage.all().values())
        st.new(p)
        self.assertIn("Place." + p.id, models.storage.all().keys())
        self.assertIn(p, models.storage.all().values())
        st.new(r)
        self.assertIn("Review." + r.id, models.storage.all().keys())
        self.assertIn(r, models.storage.all().values())
        st.new(s)
        self.assertIn("State." + s.id, models.storage.all().keys())
        self.assertIn(s, models.storage.all().values())
        st.new(u)
        self.assertIn("User." + u.id, models.storage.all().keys())
        self.assertIn(u, models.storage.all().values())

    def test_save(self):
        """
        test the function save.
        """
        st = models.storage
        a, b, c = Amenity(),  BaseModel(), City()
        p, r, s = Place(), Review(), State()
        u = User()
        st.new(a)
        st.new(b)
        st.new(c)
        st.new(p)
        st.new(r)
        st.new(s)
        st.new(u)
        st.save()
        with open("file.json", "r") as f:
            text_ = f.read()
            self.assertIn("Amenity." + a.id, text_)
            self.assertIn("BaseModel." + b.id, text_)
            self.assertIn("City." + c.id, text_)
            self.assertIn("Place." + p.id, text_)
            self.assertIn("Review." + r.id, text_)
            self.assertIn("State." + s.id, text_)
            self.assertIn("User." + u.id, text_)

    def test_reload(self):
        """
        test the function reload.
        """
        st = models.storage
        a, b, c = Amenity(),  BaseModel(), City()
        p, r, s = Place(), Review(), State()
        u = User()
        st.new(a)
        st.new(b)
        st.new(c)
        st.new(p)
        st.new(r)
        st.new(s)
        st.new(u)
        st.save()
        st.reload()
        fs = FileStorage._FileStorage__objects
        self.assertIn("Amenity." + a.id, fs)
        self.assertIn("BaseModel." + b.id, fs)
        self.assertIn("City." + c.id, fs)
        self.assertIn("Place." + p.id, fs)
        self.assertIn("Review." + r.id, fs)
        self.assertIn("State." + s.id, fs)
        self.assertIn("User." + u.id, fs)

    def test_all_(self):
        """
        test the function all without args.
        """
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new_(self):
        """
        test the function new without args.
        """
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_save_(self):
        """
        test the function save without args.
        """
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload_(self):
        """
        test the function reload without args.
        """
        with self.assertRaises(TypeError):
            models.storage.reload(None)

    def test_init(self):
        """
        test the init.
        """
        self.assertEqual(type(models.storage), FileStorage)


if __name__ == "__main__":
    unittest.main()
