class Book:
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages
        
    def __str__(self):
        return f"'{self.title}' by {self.author}"
     
    def __eq__(self, other):
        # return True if self.title == other.title  and self.author == other.author else False
        return self.title == other.title  and self.author == other.author
    
    def __lt__(self, other):
        return self.num_pages < other.num_pages
        
    def __gt__(self, other):
        return self.num_pages > other.num_pages
    
    def __add__(self, other):
        return f"{self.num_pages + other.num_pages} pages"
    
    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == 'num_pages':
            return self.num_pages
        else:
            return f"{key} key was not found"
    
        
book1 = Book("The Hobbit", "J.R.R", 200)
book2 = Book("Kafka on the Shore", "Haruki Murakami", 600)
book3 = Book("The KiteRunner", "Khaled Hosseini", 800)
book4 = Book("The Hobbit", "J.R.R", 200)


print(book1)    #__str__(self)
print(book1 == book4) # __eq__(self, other)
print(book2 < book3) # __gt__(self, other)
print(book3 > book4) # __lt__(self, other)
print(book1 + book2) # add__(self, other)
print(book1['author']) # __getItem__(self, key)