class LibraryItem:
    def __init__(self, title, item_id):
        self.title = title
        self.item_id = item_id

    def display_info(self):
        print(f"Title: {self.title}, Item ID: {self.item_id}")

class Book(LibraryItem):
    def __init__(self, title, item_id, author):
        super().__init__(title, item_id)
        self.author = author

    def show_book_details(self):
        self.display_info()
        print(f"Author: {self.author}")

class Magazine(LibraryItem):
    def __init__(self, title, item_id, issue):
        super().__init__(title, item_id)
        self.issue = issue

    def show_magazine_details(self):
        self.display_info()
        print(f"Issue: {self.issue}")

class DVD(LibraryItem):
    def __init__(self, title, item_id, duration):
        super().__init__(title, item_id)
        self.duration = duration

    def show_dvd_details(self):
        self.display_info()
        print(f"Duration: {self.duration} minutes")

# Create instances of each child class
book = Book("The Great Gatsby", "B123", "F. Scott Fitzgerald")
magazine = Magazine("National Geographic", "M456", "March 2024")
dvd = DVD("Inception", "D789", 148)

# Accessing methods from the parent and each child class
book.show_book_details()
print()
magazine.show_magazine_details()
print()
dvd.show_dvd_details()
