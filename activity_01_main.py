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
    # in an exception is handled. When exceptions are 'caught', display the exception
    # message to the console.

    # 1. Code a statement which creates an instance of the LibraryItem class with valid inputs.
    # Use your own unique valid values for the inputs to the class.
    try:
        library_item = LibraryItem(
            "The Hobbit",
            "J.R.R. Tolkien",
            Genre.FANTASY
        )
    except ValueError as error:
        print(error)

    # 2. Using the instance defined above, and the class Accessors, print
    # each of the attributes of the LibraryItem instance.
    try:
        print(library_item.title)
        print(library_item.author)
        print(library_item.genre)
    except ValueError as error:
        print(error)

    # 3. Code a statement which creates an instance of the LibraryItem class with one or more invalid inputs.
    # Use your own unique valid values for the inputs to the class.
    try:
        LibraryItem("", "Unknown Author", Genre.FICTION)
    except ValueError as error:
        print(error)


if __name__ == "__main__":
    main()