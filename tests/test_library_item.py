"""
Description: Unit tests for the LibraryItem class.
Usage:
    python -m unittest tests/test_library_item.py
"""

__author__ = "Taranpreet Singh"
__version__ = "1.0.0"

import unittest
from library_item.library_item import LibraryItem
from genre.genre import Genre


class TestLibraryItem(unittest.TestCase):
    """
    Test cases for the LibraryItem class.
    """

    def test_valid_library_item_creation(self):
        item = LibraryItem("Harry Potter", "J.K. Rowling", Genre.FANTASY)
        self.assertEqual(item.title, "Harry Potter")
        self.assertEqual(item.author, "J.K. Rowling")
        self.assertEqual(item.genre, Genre.FANTASY)

    def test_blank_title_raises_exception(self):
        with self.assertRaises(ValueError) as context:
            LibraryItem("   ", "J.K. Rowling", Genre.FANTASY)
        self.assertEqual(str(context.exception), "Title cannot be blank.")

    def test_blank_author_raises_exception(self):
        with self.assertRaises(ValueError) as context:
            LibraryItem("Harry Potter", "", Genre.FANTASY)
        self.assertEqual(str(context.exception), "Author cannot be blank.")

    def test_invalid_genre_raises_exception(self):
        with self.assertRaises(ValueError) as context:
            LibraryItem("Harry Potter", "J.K. Rowling", "Fantasy")
        self.assertEqual(str(context.exception), "Invalid Genre.")

    def test_title_accessor(self):
        item = LibraryItem("1984", "George Orwell", Genre.FICTION)
        self.assertEqual(item.title, "1984")

    def test_author_accessor(self):
        item = LibraryItem("1984", "George Orwell", Genre.FICTION)
        self.assertEqual(item.author, "George Orwell")

    def test_genre_accessor(self):
        item = LibraryItem("1984", "George Orwell", Genre.FICTION)
        self.assertEqual(item.genre, Genre.FICTION)


if __name__ == "__main__":
    unittest.main()