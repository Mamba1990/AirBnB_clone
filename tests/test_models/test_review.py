#!/usr/bin/python3
"""Represents unittests for models/review.py.

Unittest classes:
    TestReviewInstantiation
    TestReviewSave
    TestReviewToDict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.review import Review


class TestReviewInstantiation(unittest.TestCase):
    """Provides unittests for testing instantiation of the Review class."""

    def testNoArgsInstantiates(self):
        self.assertEqual(Review, type(Review()))

    def testNewInstanceStoredInObjects(self):
        self.assertIn(Review(), models.storage.all().values())

    def testIdIsPublicStr(self):
        self.assertEqual(str, type(Review().id))

    def testCreatedAtIsPublicDatetime(self):
        self.assertEqual(datetime, type(Review().created_at))

    def testUpdatedAtIsPublicDatetime(self):
        self.assertEqual(datetime, type(Review().updated_at))

    def testPlaceIdIsPublicClassAttribute(self):
        rev = Review()
        self.assertEqual(str, type(Review.place_id))
        self.assertIn("place_id", dir(rev))
        self.assertNotIn("place_id", rev.__dict__)

    def testUserIdIsPublicClassAttribute(self):
        rev = Review()
        self.assertEqual(str, type(Review.user_id))
        self.assertIn("user_id", dir(rev))
        self.assertNotIn("user_id", rev.__dict__)

    def testTextIsPublicClassAttribute(self):
        rev = Review()
        self.assertEqual(str, type(Review.text))
        self.assertIn("text", dir(rev))
        self.assertNotIn("text", rev.__dict__)

    def testTwoReviewsUniqueIds(self):
        rv_1 = Review()
        rv_2 = Review()
        self.assertNotEqual(rv_1.id, rv_2.id)

    def testTwoReviewsDifferentCreatedAt(self):
        rv_1 = Review()
        sleep(0.05)
        rv_2 = Review()
        self.assertLess(rv_1.created_at, rv_2.created_at)

    def testTwoReviewsDifferentUpdatedAt(self):
        rv_1 = Review()
        sleep(0.05)
        rv_2 = Review()
        self.assertLess(rv_1.updated_at, rv_2.updated_at)

    def testStrRepresentation(self):
        dtm = datetime.today()
        dt_repr = repr(dtm)
        rev = Review()
        rev.id = "123456"
        rev.created_at = rev.updated_at = dtm
        rvstr = rev.__str__()

    def testNoArgsInstantiates(self):
        self.assertEqual(Review, type(Review()))

    def testNewInstanceStoredInObjects(self):
        self.assertIn(Review(), models.storage.all().values())

    def testIdIsPublicStr(self):
        self.assertEqual(str, type(Review().id))

    def testCreatedAt_isPublicDatetime(self):
        self.assertEqual(datetime, type(Review().created_at))

    def testUpdatedAtIsPublicDatetime(self):
        self.assertEqual(datetime, type(Review().updated_at))

    def testPlaceIdIs_PubliClassAttribute(self):
        rv = Review()
        self.assertEqual(str, type(Review.place_id))
        self.assertIn("place_id", dir(rv))
        self.assertNotIn("place_id", rv.__dict__)

    def testUserIdIsPublicClassAttribute(self):
        rv = Review()
        self.assertEqual(str, type(Review.user_id))
        self.assertIn("user_id", dir(rv))
        self.assertNotIn("user_id", rv.__dict__)

    def testTextIsPublicClassAttribute(self):
        rv = Review()
        self.assertEqual(str, type(Review.text))
        self.assertIn("text", dir(rv))
        self.assertNotIn("text", rv.__dict__)

    def testTwoReviewsUniqueIds(self):
        rv1 = Review()
        rv2 = Review()
        self.assertNotEqual(rv1.id, rv2.id)

    def testTwoReviewsDifferentCreatedAt(self):
        rv1 = Review()
        sleep(0.05)
        rv2 = Review()
        self.assertLess(rv1.created_at, rv2.created_at)

    def tesTtwoReviewsDifferentUpdatedAt(self):
        rv1 = Review()
        sleep(0.05)
        rv2 = Review()
        self.assertLess(rv1.updated_at, rv2.updated_at)

    def testStrRepresentation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        rv = Review()
        rv.id = "123456"
        rv.created_at = rv.updated_at = dt
        rvstr = rv.__str__()
        self.assertIn("[Review] (123456)", rvstr)
        self.assertIn("'id': '123456'", rvstr)
        self.assertIn("'created_at': " + dt_repr, rvstr)
        self.assertIn("'updated_at': " + dt_repr, rvstr)

    def testArgsUnused(self):
        rev = Review(None)
        self.assertNotIn(None, rev.__dict__.values())

    def testInstantiationWithKwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        rev = Review(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(rev.id, "345")
        self.assertEqual(rev.created_at, dt)
        self.assertEqual(rev.updated_at, dt)

    def testInstantiationWithNoneKwargs(self):
        with self.assertRaises(TypeError):
            Review(id=None, created_at=None, updated_at=None)

    def testArgsUnused(self):
        rv = Review(None)
        self.assertNotIn(None, rv.__dict__.values())

    def testInstantiationWithKwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        rv = Review(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(rv.id, "345")
        self.assertEqual(rv.created_at, dt)
        self.assertEqual(rv.updated_at, dt)

        with self.assertRaises(TypeError):
            Review(id=None, created_at=None, updated_at=None)


class TestReviewSave(unittest.TestCase):
    """Provides unittests for testing save method of the Review class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def testOneSave(self):
        rev = Review()
        sleep(0.05)
        first_updated_at = rev.updated_at
        rev.save()
        self.assertLess(first_updated_at, rev.updated_at)

    def test_two_saves(self):
        rev = Review()
        sleep(0.05)
        first_updated_at = rev.updated_at
        rev.save()
        second_updated_at = rev.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        rev.save()
        self.assertLess(second_updated_at, rev.updated_at)

    def testSaveWithArg(self):
        rev = Review()
        with self.assertRaises(TypeError):
            rev.save(None)

    def testSaveUpdatesFile(self):
        rev = Review()
        rev.save()
        rvid = "Review." + rev.id

    def testOneSave(self):
        rv = Review()
        sleep(0.05)
        first_updated_at = rv.updated_at
        rv.save()
        self.assertLess(first_updated_at, rv.updated_at)

    def testTwoSaves(self):
        rv = Review()
        sleep(0.05)
        first_updated_at = rv.updated_at
        rv.save()
        second_updated_at = rv.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        rv.save()
        self.assertLess(second_updated_at, rv.updated_at)

    def testSaveWithArg(self):
        rv = Review()
        with self.assertRaises(TypeError):
            rv.save(None)

    def testSaveUpdatesFile(self):
        rv = Review()
        rv.save()
        rvid = "Review." + rv.id
        with open("file.json", "r") as f:
            self.assertIn(rvid, f.read())


class TestReviewToDict(unittest.TestCase):
    """Provides unittests for testing to_dict method of the Review class."""

    def testToDictType(self):
        self.assertTrue(dict, type(Review().to_dict()))

    def testToDictContainsCorrectKeys(self):
        rev = Review()
        self.assertIn("id", rev.to_dict())
        self.assertIn("created_at", rev.to_dict())
        self.assertIn("updated_at", rev.to_dict())
        self.assertIn("__class__", rev.to_dict())

    def testToDictContainsAddedAttributes(self):
        rev = Review()
        rev.middle_name = "Holberton"
        rev.my_number = 98
        self.assertEqual("Holberton", rev.middle_name)
        self.assertIn("my_number", rev.to_dict())

    def testToDictDatetimeAttributesAreStrs(self):
        rev = Review()
        rev_dict = rev.to_dict()
        self.assertEqual(str, type(rev_dict["id"]))
        self.assertEqual(str, type(rev_dict["created_at"]))
        self.assertEqual(str, type(rev_dict["updated_at"]))

    def testToDictOutput(self):
        dt = datetime.today()
        rev = Review()
        rev.id = "123456"
        rev.created_at = rev.updated_at = dt


class TestReviewToDict(unittest.TestCase):
    """Provides nittests for testing to_dict method of the Review class."""

    def testToDictType(self):
        self.assertTrue(dict, type(Review().to_dict()))

    def testToDictContainsCorrectKeys(self):
        rv = Review()
        self.assertIn("id", rv.to_dict())
        self.assertIn("created_at", rv.to_dict())
        self.assertIn("updated_at", rv.to_dict())
        self.assertIn("__class__", rv.to_dict())

    def testToDictContainsAddedAttributes(self):
        rv = Review()
        rv.middle_name = "Holberton"
        rv.my_number = 98
        self.assertEqual("Holberton", rv.middle_name)
        self.assertIn("my_number", rv.to_dict())

    def testToDictDatetimeAttributesAareStrs(self):
        rv = Review()
        rv_dict = rv.to_dict()
        self.assertEqual(str, type(rv_dict["id"]))
        self.assertEqual(str, type(rv_dict["created_at"]))
        self.assertEqual(str, type(rv_dict["updated_at"]))

    def testToDictOutput(self):
        dt = datetime.today()
        rv = Review()
        rv.id = "123456"
        rv.created_at = rv.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'Review',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(rv.to_dict(), tdict)

    def testContrastToDictDunderDict(self):
        rev = Review()
        self.assertNotEqual(rev.to_dict(), rev.__dict__)

    def testToDictWithArg(self):
        rev = Review()
        with self.assertRaises(TypeError):
            rev.to_dict(None)


if __name__ == "__main__":
    unittest.main()
