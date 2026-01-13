""""
Description: A client program written to verify correctness of 
the activity classes.
"""
__author__ = "Taranpreet Singh"
__version__ = "1.0.0"
__credits__ = ""


from library_item.library_item import LibraryItem
from genre.genre import Genre


def main():
    """Test the functionality of the methods encapsulated
    in this project.
    """
    # In the statements coded below, ensure that any statement that could result
    # in an exception is handled. When exceptions are 'caught', display the
    # exception message to the console.

    # 1. Create a LibraryItem instance with valid inputs
    try:
        library_item = LibraryItem(
            1001,
            "The Hobbit",
            "J.R.R. Tolkien",
            Genre.FANTASY,
            False
        )
    except ValueError as error:
        print(error)

    # 2. Print each attribute using accessors
    try:
        print(library_item.item_id)
        print(library_item.title)
        print(library_item.author)
        print(library_item.genre)
        print(library_item.is_borrowed)
    except ValueError as error:
        print(error)

    # 3. Create a LibraryItem instance with invalid inputs
    try:
        LibraryItem(
            "ABC",
            "Invalid Book",
            "Unknown Author",
            Genre.FICTION,
            "no"
        )
    except ValueError as error:
        print(error)


if __name__ == "__main__":
    main()