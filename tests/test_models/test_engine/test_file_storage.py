#!/usr/bin/python3
"""Provides unittests for models/engine/file_storage.py.

Unittest classes:
    TestFileStorageInstantiation
    TestFileStorageMethods
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


class TestFileStorageInstantiation(unittest.TestCase):
    """Represents unittests for FileStorage class."""

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

    def testAll(self):
        self.assertEqual(dict, type(models.storage.all()))

    def testAllWithArg(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def testNew(self):
        bm = BaseModel()
        usr = User()
        st = State()
        pl = Place()
        cy = City()
        am = Amenity()
        rev = Review()
        models.storage.new(bm)
        models.storage.new(usr)
        models.storage.new(st)
        models.storage.new(pl)
        models.storage.new(cy)
        models.storage.new(am)
        models.storage.new(rev)
        self.assertIn("BaseModel." + bm.id, models.storage.all().keys())
        self.assertIn(bm, models.storage.all().values())
        self.assertIn("User." + usr.id, models.storage.all().keys())
        self.assertIn(usr, models.storage.all().values())
        self.assertIn("State." + st.id, models.storage.all().keys())
        self.assertIn(st, models.storage.all().values())
        self.assertIn("Place." + pl.id, models.storage.all().keys())
        self.assertIn(pl, models.storage.all().values())
        self.assertIn("City." + cy.id, models.storage.all().keys())
        self.assertIn(cy, models.storage.all().values())
        self.assertIn("Amenity." + am.id, models.storage.all().keys())
        self.assertIn(am, models.storage.all().values())
        self.assertIn("Review." + rev.id, models.storage.all().keys())
        self.assertIn(rev, models.storage.all().values())

    def testNewWithArgs(self):
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def testSave(self):
        bm = BaseModel()
        usr = User()
        st = State()
        pl = Place()
        cy = City()
        am = Amenity()
        rev = Review()
        models.storage.new(bm)
        models.storage.new(usr)
        models.storage.new(st)
        models.storage.new(pl)
        models.storage.new(cy)
        models.storage.new(am)
        models.storage.new(rev)
        models.storage.save()
        save_text = ""
        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + bm.id, save_text)
            self.assertIn("User." + usr.id, save_text)
            self.assertIn("State." + st.id, save_text)
            self.assertIn("Place." + pl.id, save_text)
            self.assertIn("City." + cy.id, save_text)
            self.assertIn("Amenity." + am.id, save_text)
            self.assertIn("Review." + rev.id, save_text)

    def testSaveWithArg(self):
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def testReload(self):
        bm = BaseModel()
        usr = User()
        st = State()
        pl = Place()
        cy = City()
        am = Amenity()
        rev = Review()
        models.storage.new(bm)
        models.storage.new(usr)
        models.storage.new(st)
        models.storage.new(pl)
        models.storage.new(cy)
        models.storage.new(am)
        models.storage.new(rev)
        models.storage.save()
        models.storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + bm.id, objs)
        self.assertIn("User." + usr.id, objs)
        self.assertIn("State." + st.id, objs)
        self.assertIn("Place." + pl.id, objs)
        self.assertIn("City." + cy.id, objs)
        self.assertIn("Amenity." + am.id, objs)
        self.assertIn("Review." + rev.id, objs)

    def testReloadWithArg(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)


if __name__ == "__main__":
    unittest.main()
