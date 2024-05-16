import unittest
from library import Library


class LibraryTest(unittest.TestCase):

    def setUp(self):
        self.library = Library()

    # --- ADD TEST ---
    def test_add_book_existing_title(self):
        # Black-box testing
        """Tests if adding a book with an existing title increments the count."""
        self.library.add_book("The Hitchhiker's Guide to the Galaxy")
        self.library.add_book("The Hitchhiker's Guide to the Galaxy", count=2)

        # Assert that the book count is incremented
        # assert self.library.books["The Hitchhiker's Guide to the Galaxy"]["count"] == 3
        self.assertEqual(self.library.books["The Hitchhiker's Guide to the Galaxy"]["count"], 3)

    def test_add_book_new_title(self):
        """Tests if adding a book with a new title creates a new entry."""
        self.library.add_book("Ender's Game")

        # Assert that the book entry exists and has the correct count
        assert "Ender's Game" in self.library.books
        assert self.library.books["Ender's Game"]["count"] == 1

    # --- BORROW TEST ---
    def test_borrow_book_available(self):
        """Tests if borrowing a book with available copies succeeds."""
        self.library.add_book("Dune", count=2)

        # Assert successful borrow
        # assert self.library.borrow_book("Dune") is True
        self.assertTrue(self.library.borrow_book("Dune"), True)

        # Assert borrowed count is incremented
        assert self.library.books["Dune"]["borrowed"] == 1

    def test_borrow_book_unavailable(self):
        """Tests if borrowing a book with no available copies fails."""
        self.library.add_book("The Martian")

        # Assert borrow fails
        assert self.library.borrow_book("The Martian") is False

        # Assert borrowed count remains unchanged
        assert self.library.books["The Martian"]["borrowed"] == 0

    # --- RETURN TEST ---
    def test_return_book_borrowed(self):
        """Tests if returning a borrowed book succeeds."""
        self.library.add_book("The Lord of the Rings")
        self.library.borrow_book("The Lord of the Rings")

        # Assert successful return
        assert self.library.return_book("The Lord of the Rings") is True

        # Assert borrowed count is decremented
        assert self.library.books["The Lord of the Rings"]["borrowed"] == 0

    def test_return_book_not_borrowed(self):
        """Tests if returning a non-borrowed book fails."""
        self.library.add_book("A Confederacy of Dunces")

        # Assert return fails
        assert self.library.return_book("A Confederacy of Dunces") is False

        # Assert borrowed count remains unchanged
        assert self.library.books["A Confederacy of Dunces"]["borrowed"] == 0

    # --- CHECK AVAILABILITY TEST ---
    def test_check_availability_available(self):
        """Tests if checking availability returns True for available books."""
        self.library.add_book("Pride and Prejudice", count=3)

        # Assert availability check returns True
        assert self.library.check_availability("Pride and Prejudice") is True

    def test_check_availability_unavailable(self):
        """Tests if checking availability returns False for unavailable books."""
        self.library.add_book("To Kill a Mockingbird")
        self.library.borrow_book("To Kill a Mockingbird")

        # Assert availability check returns False
        assert self.library.check_availability("To Kill a Mockingbird") is False


if __name__ == '__main__':
    unittest.main()