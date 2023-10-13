<<<<<<< HEAD
#!/usr/bin/python3i
"""Provides unittests for models/engine/file_storage.py.

Unittest classes:
    TestFileStorageInstantiation
    TestFileStorageMethods
=======
#!/usr/bin/python3
"""Defines unittests for models/engine/file_storage.py.

Unittest classes:
    TestFileStorage_instantiation
    TestFileStorage_methods
>>>>>>> 2cbaad26e3e537e611d90c4d8dcc81a4d57d3495
"""
import os
import json
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


<<<<<<< HEAD
class TestFileStorageInstantiation(unittest.TestCase):
    """Represents unittests for testing instantiation of the FileStorage class."""

    def testFileStorageInstantiationNoArgs(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def testFileStorageInstantiationWith_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def testFileStorageFilePathIsPrivateStr(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def testFileStorageObjectsIsPrivateDict(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def testStorageInitializes(self):
        self.assertEqual(type(models.storage), FileStorage)


class TestFileStorageMethods(unittest.TestCase):
    """Provides unittests for testing methods of the FileStorage class."""
=======
class TestFileStorage_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the FileStorage class."""

    def test_FileStorage_instantiation_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_instantiation_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_FileStorage_file_path_is_private_str(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def testFileStorage_objects_is_private_dict(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage_initializes(self):
        self.assertEqual(type(models.storage), FileStorage)


class TestFileStorage_methods(unittest.TestCase):
    """Unittests for testing methods of the FileStorage class."""
>>>>>>> 2cbaad26e3e537e611d90c4d8dcc81a4d57d3495

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

<<<<<<< HEAD
    def testAll(self):
        self.assertEqual(dict, type(models.storage.all()))

    def testAllWithArg(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def testNew(self):
        bm = BaseModel()
        usr = User()
=======
    def test_all(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_all_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new(self):
        bm = BaseModel()
        us = User()
>>>>>>> 2cbaad26e3e537e611d90c4d8dcc81a4d57d3495
        st = State()
        pl = Place()
        cy = City()
        am = Amenity()
<<<<<<< HEAD
        rev = Review()
        models.storage.new(bm)
        models.storage.new(usr)
=======
        rv = Review()
        models.storage.new(bm)
        models.storage.new(us)
>>>>>>> 2cbaad26e3e537e611d90c4d8dcc81a4d57d3495
        models.storage.new(st)
        models.storage.new(pl)
        models.storage.new(cy)
        models.storage.new(am)
<<<<<<< HEAD
        models.storage.new(rev)
        self.assertIn("BaseModel." + bm.id, models.storage.all().keys())
        self.assertIn(bm, models.storage.all().values())
        self.assertIn("User." + usr.id, models.storage.all().keys())
        self.assertIn(usr, models.storage.all().values())
=======
        models.storage.new(rv)
        self.assertIn("BaseModel." + bm.id, models.storage.all().keys())
        self.assertIn(bm, models.storage.all().values())
        self.assertIn("User." + us.id, models.storage.all().keys())
        self.assertIn(us, models.storage.all().values())
>>>>>>> 2cbaad26e3e537e611d90c4d8dcc81a4d57d3495
        self.assertIn("State." + st.id, models.storage.all().keys())
        self.assertIn(st, models.storage.all().values())
        self.assertIn("Place." + pl.id, models.storage.all().keys())
        self.assertIn(pl, models.storage.all().values())
        self.assertIn("City." + cy.id, models.storage.all().keys())
        self.assertIn(cy, models.storage.all().values())
        self.assertIn("Amenity." + am.id, models.storage.all().keys())
        self.assertIn(am, models.storage.all().values())
<<<<<<< HEAD
        self.assertIn("Review." + rev.id, models.storage.all().keys())
        self.assertIn(rev, models.storage.all().values())

    def testNewWithArgs(self):
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def testSave(self):
        bm = BaseModel()
        usr = User()
=======
        self.assertIn("Review." + rv.id, models.storage.all().keys())
        self.assertIn(rv, models.storage.all().values())

    def test_new_with_args(self):
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_save(self):
        bm = BaseModel()
        us = User()
>>>>>>> 2cbaad26e3e537e611d90c4d8dcc81a4d57d3495
        st = State()
        pl = Place()
        cy = City()
        am = Amenity()
<<<<<<< HEAD
        rev = Review()
        models.storage.new(bm)
        models.storage.new(usr)
=======
        rv = Review()
        models.storage.new(bm)
        models.storage.new(us)
>>>>>>> 2cbaad26e3e537e611d90c4d8dcc81a4d57d3495
        models.storage.new(st)
        models.storage.new(pl)
        models.storage.new(cy)
        models.storage.new(am)
<<<<<<< HEAD
        models.storage.new(rev)
=======
        models.storage.new(rv)
>>>>>>> 2cbaad26e3e537e611d90c4d8dcc81a4d57d3495
        models.storage.save()
        save_text = ""
        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + bm.id, save_text)
<<<<<<< HEAD
            self.assertIn("User." + usr.id, save_text)
=======
            self.assertIn("User." + us.id, save_text)
>>>>>>> 2cbaad26e3e537e611d90c4d8dcc81a4d57d3495
            self.assertIn("State." + st.id, save_text)
            self.assertIn("Place." + pl.id, save_text)
            self.assertIn("City." + cy.id, save_text)
            self.assertIn("Amenity." + am.id, save_text)
<<<<<<< HEAD
            self.assertIn("Review." + rev.id, save_text)

    def testSaveWithArg(self):
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def testReload(self):
        bm = BaseModel()
        usr = User()
=======
            self.assertIn("Review." + rv.id, save_text)

    def test_save_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload(self):
        bm = BaseModel()
        us = User()
>>>>>>> 2cbaad26e3e537e611d90c4d8dcc81a4d57d3495
        st = State()
        pl = Place()
        cy = City()
        am = Amenity()
<<<<<<< HEAD
        rev = Review()
        models.storage.new(bm)
        models.storage.new(usr)
=======
        rv = Review()
        models.storage.new(bm)
        models.storage.new(us)
>>>>>>> 2cbaad26e3e537e611d90c4d8dcc81a4d57d3495
        models.storage.new(st)
        models.storage.new(pl)
        models.storage.new(cy)
        models.storage.new(am)
<<<<<<< HEAD
        models.storage.new(rev)
=======
        models.storage.new(rv)
>>>>>>> 2cbaad26e3e537e611d90c4d8dcc81a4d57d3495
        models.storage.save()
        models.storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + bm.id, objs)
<<<<<<< HEAD
        self.assertIn("User." + usr.id, objs)
=======
        self.assertIn("User." + us.id, objs)
>>>>>>> 2cbaad26e3e537e611d90c4d8dcc81a4d57d3495
        self.assertIn("State." + st.id, objs)
        self.assertIn("Place." + pl.id, objs)
        self.assertIn("City." + cy.id, objs)
        self.assertIn("Amenity." + am.id, objs)
<<<<<<< HEAD
        self.assertIn("Review." + rev.id, objs)

    def testReloadWithArg(self):
=======
        self.assertIn("Review." + rv.id, objs)

    def test_reload_with_arg(self):
>>>>>>> 2cbaad26e3e537e611d90c4d8dcc81a4d57d3495
        with self.assertRaises(TypeError):
            models.storage.reload(None)


if __name__ == "__main__":
    unittest.main()
