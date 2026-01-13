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

    Attributes:
        item_id (int): The unique id of the library item.
        title (str): The title of the library item.
        author (str): The author of the library item.
        genre (Genre): The Genre of the library item.
        is_borrowed (bool): Indicates if the item is borrowed.
    """

    def __init__(
        self,
        item_id: int,
        title: str,
        author: str,
        genre: Genre,
        is_borrowed: bool
    ):
        """
        Initialize a LibraryItem instance.

        Args:
            item_id (int): The unique id of the library item.
            title (str): The title of the library item.
            author (str): The author of the library item.
            genre (Genre): The Genre of the library item.
            is_borrowed (bool): Indicates if the item is borrowed.

        Raises:
            ValueError: If item_id is not numeric.
            ValueError: If title is blank.
            ValueError: If author is blank.
            ValueError: If genre is invalid.
            ValueError: If is_borrowed is not boolean.
        """
        if not isinstance(item_id, int):
            raise ValueError("Item Id must be numeric.")

        title = title.strip()
        if not title:
            raise ValueError("Title cannot be blank.")

        if not author:
            raise ValueError("Author cannot be blank.")

        if not isinstance(genre, Genre):
            raise ValueError("Invalid Genre.")

        if not isinstance(is_borrowed, bool):
            raise ValueError("Is Borrowed must be a boolean value.")

        self.__item_id = item_id
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__is_borrowed = is_borrowed

    @property
    def item_id(self) -> int:
        """
        Get the item id.

        Returns:
            int: The item id.
        """
        return self.__item_id

    @property
    def title(self) -> str:
        """
        Get the title of the library item.

        Returns:
            str: The title of the library item.
        """
        return self.__title

    @property
    def author(self) -> str:
        """
        Get the author of the library item.

        Returns:
            str: The author of the library item.
        """
        return self.__author

    @property
    def genre(self) -> Genre:
        """
        Get the genre of the library item.

        Returns:
            Genre: The Genre of the library item.
        """
        return self.__genre

    @property
    def is_borrowed(self) -> bool:
        """
        Get the borrowed status of the library item.

        Returns:
            bool: True if borrowed, otherwise False.
        """
        return self.__is_borrowed