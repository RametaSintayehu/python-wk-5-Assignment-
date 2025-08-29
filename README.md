# Book, EBook, and EnhancedBook Python Classes

This repository demonstrates the use of Python's Object-Oriented Programming (OOP) principles, including **classes**, **inheritance**, **encapsulation**, and **method overriding**. The code is contained in `class.py` and models a simple book system.

## Features

- **Book Class**:  
  Represents a physical book with attributes like title, author, pages, price, and availability.  
  Includes methods to display info, borrow, and return the book.

- **EBook Subclass**:  
  Inherits from `Book` and adds specific attributes such as file size, format type, and download status.  
  Overrides the `display_info` method and provides an additional `download` method.

- **EnhancedBook Subclass**:  
  Also inherits from `Book` and demonstrates encapsulation using private attributes (edition and discount).  
  Includes getter and setter methods for these attributes, and calculates the final price after discount.

## Usage

```python
# Create a Book object
book1 = Book("1984", "George Orwell", 328, 9.99)
book1.display_info()
book1.borrow_book()
book1.display_info()
book1.return_book()

# Create an EBook object
ebook1 = EBook("Digital Fortress", "Dan Brown", 356, 5.99, 2, "PDF")
ebook1.display_info()
ebook1.download()

# Create an EnhancedBook object
enhanced_book = EnhancedBook("Brave New World", "Aldous Huxley", 311, 8.99)
print("Edition:", enhanced_book.get_edition())
enhanced_book.set_discount(20)
```

## Key OOP Concepts Illustrated

- **Encapsulation**: Private attributes in `EnhancedBook` (`__edition`, `__discount`) are accessed and modified through getter/setter methods.
- **Inheritance**: `EBook` and `EnhancedBook` inherit from `Book`, reusing and extending its functionality.
- **Method Overriding**: `EBook` overrides the `display_info` method to provide additional details.
- **Super Calls**: Subclasses use `super()` to invoke parent class methods.

## Getting Started

1. Clone the repository.
2. Run `class.py` using Python 3.x.
3. Modify or extend the classes as needed for your own experiments with OOP.

## License

This project is licensed under the MIT License.
