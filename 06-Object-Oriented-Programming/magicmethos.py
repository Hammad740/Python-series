# // https://www.geeksforgeeks.org/dunder-magic-methods-python/

# ** Python Magic methods are the methods starting and ending with double underscores ‘__’. They are defined by built-in classes in Python and commonly used for operator overloading.

# ** They are also called Dunder methods, Dunder here means “Double Under (Underscores)”.


class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __len__(self):
        return self.pages


x = Book("Python Rocks", "Jose", 200)
print(x)
print(len(x))
