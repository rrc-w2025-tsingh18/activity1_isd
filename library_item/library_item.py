""""
Description: A class to manage LibraryItem objects.
"""
__author__ = "Taranpreet Singh"
__version__ = "1.0.0"
__credits__ = ""

from genre.genre import Genre


class LibraryItem:
    """
    Represents a single library item.
    """

    def __init__(self, title: str, author: str, genre: Genre):
        """
        Initialize a LibraryItem object.

        Args:
            title (str): The title of the item.
            author (str): The author of the item.
            genre (Genre): The genre of the item.
        """
        title = title.strip()
        if not title:
            raise ValueError("Title cannot be blank.")

        if not author:
            raise ValueError("Author cannot be blank.")

        if not isinstance(genre, Genre):
            raise ValueError("Invalid Genre.")

        self.__title = title
        self.__author = author
        self.__genre = genre

    @property
    def title(self) -> str:
        """
        Get the title of the library item.
        """
        return self.__title

    @property
    def author(self) -> str:
        """
        Get the author of the library item.
        """
        return self.__author

    @property
    def genre(self) -> Genre:
        """
        Get the genre of the library item.
        """
        return self.__genre

