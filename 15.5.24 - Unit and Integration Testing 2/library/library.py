
class Library:
    def __init__(self):
        self.books = {}  # books stored as {title: {'count': int, 'borrowed': int}}

    def add_book(self, title, count=1):
        if title in self.books:
            self.books[title]['count'] += count
        else:
            self.books[title] = {'count': count, 'borrowed': 0}

    def borrow_book(self, title):
        if title in self.books and self.books[title]['count'] > self.books[title]['borrowed']:
            self.books[title]['borrowed'] += 1
            return True
        return False

    def return_book(self, title):
        if title in self.books and self.books[title]['borrowed'] > 0:
            self.books[title]['borrowed'] -= 1
            return True
        return False

    def check_availability(self, title):
        if title in self.books and self.books[title]['count'] > self.books[title]['borrowed']:
            return True
        return False
