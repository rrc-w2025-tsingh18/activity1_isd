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
    Unit tests for the LibraryItem class.
    """

    def test_init_valid_inputs_attributes_set_correctly(self):
        # Arrange
        title = "Harry Potter"
        author = "J.K. Rowling"
        genre = Genre.FANTASY

        # Act
        library_item = LibraryItem(title, author, genre)

        # Assert (using name mangling)
        self.assertEqual(library_item._LibraryItem__title, title)
        self.assertEqual(library_item._LibraryItem__author, author)
        self.assertEqual(library_item._LibraryItem__genre, genre)

    def test_init_blank_title_raises_exception(self):
        # Arrange / Act / Assert
        with self.assertRaises(ValueError) as context:
            LibraryItem("   ", "J.K. Rowling", Genre.FANTASY)

        self.assertEqual(str(context.exception), "Title cannot be blank.")

    def test_init_blank_author_raises_exception(self):
        # Arrange / Act / Assert
        with self.assertRaises(ValueError) as context:
            LibraryItem("Harry Potter", "", Genre.FANTASY)

        self.assertEqual(str(context.exception), "Author cannot be blank.")

    def test_init_invalid_genre_raises_exception(self):
        # Arrange / Act / Assert
        with self.assertRaises(ValueError) as context:
            LibraryItem("Harry Potter", "J.K. Rowling", "Fantasy")

        self.assertEqual(str(context.exception), "Invalid Genre.")

    def test_title_accessor_returns_title(self):
        # Arrange
        library_item = LibraryItem("1984", "George Orwell", Genre.FICTION)

        # Act
        result = library_item.title

        # Assert
        self.assertEqual(result, "1984")

    def test_author_accessor_returns_author(self):
        # Arrange
        library_item = LibraryItem("1984", "George Orwell", Genre.FICTION)

        # Act
        result = library_item.author

        # Assert
        self.assertEqual(result, "George Orwell")

    def test_genre_accessor_returns_genre(self):
        # Arrange
        library_item = LibraryItem("1984", "George Orwell", Genre.FICTION)

        # Act
        result = library_item.genre

        # Assert
        self.assertEqual(result, Genre.FICTION)


if __name__ == "__main__":
    unittest.main()