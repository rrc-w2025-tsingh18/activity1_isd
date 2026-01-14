"""
Description: Unit tests for the LibraryItem class.
Usage:
    python -m unittest tests/test_library_item.py
"""

__author__ = "Taranpreet Singh"
__version__ = "1.1.0"

import unittest
from library_item.library_item import LibraryItem
from genre.genre import Genre


class TestLibraryItem(unittest.TestCase):
    """
    Unit tests for the LibraryItem class.
    """

    def test_init_valid_inputs_sets_attributes(self):
        # Arrange
        item_id = 101
        title = "The Hobbit"
        author = "J.R.R. Tolkien"
        genre = Genre.FANTASY
        is_borrowed = False

        # Act
        library_item = LibraryItem(item_id, title, author, genre, is_borrowed)

        # Assert (name mangling)
        self.assertEqual(library_item._LibraryItem__item_id, item_id)
        self.assertEqual(library_item._LibraryItem__title, title)
        self.assertEqual(library_item._LibraryItem__author, author)
        self.assertEqual(library_item._LibraryItem__genre, genre)
        self.assertEqual(library_item._LibraryItem__is_borrowed, is_borrowed)

    def test_init_item_id_not_numeric_raises_exception(self):
        with self.assertRaises(ValueError) as context:
            LibraryItem("ABC", "The Hobbit", "J.R.R. Tolkien", Genre.FANTASY, False)
        self.assertEqual(str(context.exception), "Item Id must be numeric.")

    def test_init_blank_title_raises_exception(self):
        with self.assertRaises(ValueError) as context:
            LibraryItem(101, "   ", "J.R.R. Tolkien", Genre.FANTASY, False)
        self.assertEqual(str(context.exception), "Title cannot be blank.")

    def test_init_blank_author_raises_exception(self):
        with self.assertRaises(ValueError) as context:
            LibraryItem(101, "The Hobbit", "", Genre.FANTASY, False)
        self.assertEqual(str(context.exception), "Author cannot be blank.")

    def test_init_invalid_genre_raises_exception(self):
        with self.assertRaises(ValueError) as context:
            LibraryItem(101, "The Hobbit", "J.R.R. Tolkien", "Fantasy", False)
        self.assertEqual(str(context.exception), "Invalid Genre.")

    def test_init_is_borrowed_not_boolean_raises_exception(self):
        with self.assertRaises(ValueError) as context:
            LibraryItem(101, "The Hobbit", "J.R.R. Tolkien", Genre.FANTASY, "yes")
        self.assertEqual(
            str(context.exception),
            "Is Borrowed must be a boolean value."
        )

    def test_item_id_valid_item_returns_item_id(self):
        library_item = LibraryItem(201, "1984", "George Orwell", Genre.FICTION, False)
        self.assertEqual(library_item.item_id, 201)

    def test_title_valid_item_returns_title(self):
        library_item = LibraryItem(202, "1984", "George Orwell", Genre.FICTION, False)
        self.assertEqual(library_item.title, "1984")

    def test_author_valid_item_returns_author(self):
        library_item = LibraryItem(203, "1984", "George Orwell", Genre.FICTION, False)
        self.assertEqual(library_item.author, "George Orwell")

    def test_genre_valid_item_returns_genre(self):
        library_item = LibraryItem(204, "1984", "George Orwell", Genre.FICTION, False)
        self.assertEqual(library_item.genre, Genre.FICTION)

    def test_is_borrowed_true_input_returns_true(self):
        library_item = LibraryItem(205, "1984", "George Orwell", Genre.FICTION, True)
        self.assertTrue(library_item.is_borrowed)


if __name__ == "__main__":
    unittest.main()