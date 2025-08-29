# Constructor-initializes the object with unique values
class Book:
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        self.is_available = True

    # Method - What the book can do
    def display_info(self):
        print(f"Title: {self.title}") 
        print(f"Author: {self.author}")
        print(f"pages: {self.pages}") 
        print(f"price: {self.price}")
        print(f"Available: {'Yes' if self.is_available else 'No'}")

    # Another method
    def borrow_book(self):
        if self.is_available:
            self.is_available = False
            print(f"'{self.title}' has been borrowed!")
        else:
            print(f"Sorry, '{self.title}' is currently unavailable.")

    def return_book(self):
        self.is_available = True
        print(f"'{self.title}' has been returned!")

#Testing the base class
# creating an object of the Book class
book1 = Book("1984", "George Orwell", 328, 9.99)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 281, 7.99)
#Use the methods 
book1.display_info()  
book1.borrow_book() 
book1.display_info()
book1.return_book()
#Add Inheritance(creating a subclass)  
# Subclass - inherits from the Book class  
class EBook(Book):
    def __init__(self, title, author, pages, price, file_size, format_type):
        # Call the constructor of the parent class
        super().__init__(title, author, pages, price)  
        # Add new attributes specific to EBook
        self.file_size = file_size 
        self.format_type = format_type
        self.is_downloaded = False

    # Overriding the display_info method to include file size
    def display_info(self):
        super().display_info()  # Call the parent class method
        print(f"File Size: {self.file_size} MB") 
        print(f"Format: {self.format_type}")
        print(f"Downloaded: {'Yes' if self.is_downloaded else 'No'}") 

    # Add new method specific to EBook
    def download(self):
        self.is_downloaded = True
        print(f"'{self.title}' has been downloaded!")
        print(f"{self.format_type} format!")

#Testing the Inheritance
# creating an object of the EBook class 
ebook1 = EBook("Digital Fortress", "Dan Brown", 356, 5.99, 2, "PDF") 
#Teting the Inheritance methods 
ebook1.display_info() 
ebook1.download() 
#Add Encapsulation 
class EnhancedBook(Book): 
    def __init__(self, title, author, pages, price): 
        super().__init__(title, author, pages, price) 
        self.__edition = 1  # Private attribute 
        self.__discount=0 # Private attribute

    # Getter methods to access private attributes
    def get_edition(self): 
        return self.__edition 
    # Setter method  
    def set_discount(self, discount): 
        if 0 <= discount <= 50: 
            self.__discount = discount
        else: 
            print("Discount must be between 0 and 50 percent.") 
            #Method using private attributes
            def get_final_price(self): 
                discount_amount = self.price * (self.__discount / 100) 
                return self.price * (1 - self.__discount / 100) 
            def display_info(self): 
                super().display_info() 
                print(f"Edition: {self.__edition}")  
                print(f"Discount: {self.__discount}%") 
                print(f"Final Price: ${self.get_final_price():.2f}") 
