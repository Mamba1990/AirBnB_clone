#!/usr/bin/python3
<<<<<<< HEAD
"""Represents unittests for models/review.py.

Unittest classes:
    TestReviewInstantiation
    TestReviewSave
    TestReviewToDict
=======
"""Defines unittests for models/review.py.

Unittest classes:
    TestReview_instantiation
    TestReview_save
    TestReview_to_dict
>>>>>>> 2cbaad26e3e537e611d90c4d8dcc81a4d57d3495
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.review import Review


<<<<<<< HEAD
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
=======
class TestReview_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Review class."""

    def test_no_args_instantiates(self):
        self.assertEqual(Review, type(Review()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Review(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Review().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Review().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Review().updated_at))

    def test_place_id_is_public_class_attribute(self):
        rv = Review()
        self.assertEqual(str, type(Review.place_id))
        self.assertIn("place_id", dir(rv))
        self.assertNotIn("place_id", rv.__dict__)

    def test_user_id_is_public_class_attribute(self):
        rv = Review()
        self.assertEqual(str, type(Review.user_id))
        self.assertIn("user_id", dir(rv))
        self.assertNotIn("user_id", rv.__dict__)

    def test_text_is_public_class_attribute(self):
        rv = Review()
        self.assertEqual(str, type(Review.text))
        self.assertIn("text", dir(rv))
        self.assertNotIn("text", rv.__dict__)

    def test_two_reviews_unique_ids(self):
        rv1 = Review()
        rv2 = Review()
        self.assertNotEqual(rv1.id, rv2.id)

    def test_two_reviews_different_created_at(self):
        rv1 = Review()
        sleep(0.05)
        rv2 = Review()
        self.assertLess(rv1.created_at, rv2.created_at)

    def test_two_reviews_different_updated_at(self):
        rv1 = Review()
        sleep(0.05)
        rv2 = Review()
        self.assertLess(rv1.updated_at, rv2.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        rv = Review()
        rv.id = "123456"
        rv.created_at = rv.updated_at = dt
        rvstr = rv.__str__()
>>>>>>> 2cbaad26e3e537e611d90c4d8dcc81a4d57d3495
        self.assertIn("[Review] (123456)", rvstr)
        self.assertIn("'id': '123456'", rvstr)
        self.assertIn("'created_at': " + dt_repr, rvstr)
        self.assertIn("'updated_at': " + dt_repr, rvstr)

<<<<<<< HEAD
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
=======
    def test_args_unused(self):
        rv = Review(None)
        self.assertNotIn(None, rv.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        rv = Review(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(rv.id, "345")
        self.assertEqual(rv.created_at, dt)
        self.assertEqual(rv.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
>>>>>>> 2cbaad26e3e537e611d90c4d8dcc81a4d57d3495
        with self.assertRaises(TypeError):
            Review(id=None, created_at=None, updated_at=None)


<<<<<<< HEAD
class TestReviewSave(unittest.TestCase):
    """Provides unittests for testing save method of the Review class."""
=======
class TestReview_save(unittest.TestCase):
    """Unittests for testing save method of the Review class."""
>>>>>>> 2cbaad26e3e537e611d90c4d8dcc81a4d57d3495

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

<<<<<<< HEAD
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
=======
    def test_one_save(self):
        rv = Review()
        sleep(0.05)
        first_updated_at = rv.updated_at
        rv.save()
        self.assertLess(first_updated_at, rv.updated_at)

    def test_two_saves(self):
        rv = Review()
        sleep(0.05)
        first_updated_at = rv.updated_at
        rv.save()
        second_updated_at = rv.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        rv.save()
        self.assertLess(second_updated_at, rv.updated_at)

    def test_save_with_arg(self):
        rv = Review()
        with self.assertRaises(TypeError):
            rv.save(None)

    def test_save_updates_file(self):
        rv = Review()
        rv.save()
        rvid = "Review." + rv.id
>>>>>>> 2cbaad26e3e537e611d90c4d8dcc81a4d57d3495
        with open("file.json", "r") as f:
            self.assertIn(rvid, f.read())


<<<<<<< HEAD
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
=======
class TestReview_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the Review class."""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(Review().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        rv = Review()
        self.assertIn("id", rv.to_dict())
        self.assertIn("created_at", rv.to_dict())
        self.assertIn("updated_at", rv.to_dict())
        self.assertIn("__class__", rv.to_dict())

    def test_to_dict_contains_added_attributes(self):
        rv = Review()
        rv.middle_name = "Holberton"
        rv.my_number = 98
        self.assertEqual("Holberton", rv.middle_name)
        self.assertIn("my_number", rv.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        rv = Review()
        rv_dict = rv.to_dict()
        self.assertEqual(str, type(rv_dict["id"]))
        self.assertEqual(str, type(rv_dict["created_at"]))
        self.assertEqual(str, type(rv_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        rv = Review()
        rv.id = "123456"
        rv.created_at = rv.updated_at = dt
>>>>>>> 2cbaad26e3e537e611d90c4d8dcc81a4d57d3495
        tdict = {
            'id': '123456',
            '__class__': 'Review',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
<<<<<<< HEAD
        self.assertDictEqual(rev.to_dict(), tdict)

    def testContrastToDictDunderDict(self):
        rev = Review()
        self.assertNotEqual(rev.to_dict(), rev.__dict__)

    def testToDictWithArg(self):
=======
        self.assertDictEqual(rv.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        rv = Review()
        self.assertNotEqual(rv.to_dict(), rv.__dict__)

    def test_to_dict_with_arg(self):
>>>>>>> 2cbaad26e3e537e611d90c4d8dcc81a4d57d3495
        rv = Review()
        with self.assertRaises(TypeError):
            rv.to_dict(None)


if __name__ == "__main__":
    unittest.main()
