class Book():

    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    # dunder method to represents the objetc
    def __repr__(self):
        return "Title: {}, Author: {}".format(self.title, self.author)

    # dunder method to represent the len method
    def __len__(self):
        return self.pages
    
mybook = Book("Python Rocks", "Jose", 250)
length_book = len(mybook)
print(length_book)