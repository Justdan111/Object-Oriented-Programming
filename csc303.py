# Task 1: Multilevel Inheritance – Library Management System

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def display_details(self):
        print(f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}")

class BorrowableBook(Book):
    def __init__(self, title, author, isbn, borrower_name="", borrow_date=""):
        super().__init__(title, author, isbn)
        self.borrower_name = borrower_name
        self.borrow_date = borrow_date

    def borrow(self, borrower_name, borrow_date):
        self.borrower_name = borrower_name
        self.borrow_date = borrow_date
        print(f"Borrowed by {self.borrower_name} on {self.borrow_date}")

class DigitalLibrary(BorrowableBook):
    def __init__(self, title, author, isbn, borrower_name="", borrow_date="", e_book_link=""):
        super().__init__(title, author, isbn, borrower_name, borrow_date)
        self.e_book_link = e_book_link

    def display_details(self):
        super().display_details()
        print(f"e-Book Link: {self.e_book_link}")

# Task 2: Multiple Inheritance – Fitness Tracker

class StepCounter:
    def record_steps(self, steps):
        self.steps = steps
        print(f"Steps recorded: {self.steps}")

class CalorieTracker:
    def record_calories(self, intake, burnt):
        self.intake = intake
        self.burnt = burnt
        print(f"Calories intake: {self.intake}, Burnt: {self.burnt}")

class FitnessTracker(StepCounter, CalorieTracker):
    def calculate_net_balance(self):
        try:
            net = self.intake - self.burnt
            print(f"Net Calorie Balance: {net}")
        except AttributeError:
            print("Please record steps and calories first.")

# Task 3: Method Overriding – Real Estate Management System

class Property:
    def __init__(self, address, price, size):
        self.address = address
        self.price = price
        self.size = size

    def display_info(self):
        print(f"Address: {self.address}, Price: {self.price}, Size: {self.size}")

class House(Property):
    def __init__(self, address, price, size, number_of_bedrooms):
        super().__init__(address, price, size)
        self.number_of_bedrooms = number_of_bedrooms

    def display_info(self):
        super().display_info()
        print(f"Bedrooms: {self.number_of_bedrooms}")

class CommercialSpace(Property):
    def __init__(self, address, price, size, business_type):
        super().__init__(address, price, size)
        self.business_type = business_type

    def display_info(self):
        super().display_info()
        print(f"Business Type: {self.business_type}")

# Task 4: Using super() – Online Shopping Cart

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

class DiscountedProduct(Product):
    def __init__(self, name, price, quantity, discount_percentage):
        super().__init__(name, price, quantity)
        self.discount_percentage = discount_percentage

    def calculate_total_price(self):
        total = super().calculate_total_price()
        discount = total * (self.discount_percentage / 100)
        return total - discount

# Main Program
if __name__ == "__main__":
    # Example usage for Task 1
    book1 = Book("Python Programming", "John Doe", "1234567890")
    book1.display_details()

    borrowable_book = BorrowableBook("Learning Java", "Jane Smith", "0987654321")
    borrowable_book.borrow("Alice", "2023-10-01")

    digital_book = DigitalLibrary("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565", e_book_link="http://example.com/greatgatsby")
    digital_book.display_details()

    # Example usage for Task 2
    fitness_tracker = FitnessTracker()
    fitness_tracker.record_steps(5000)
    fitness_tracker.record_calories(2500, 1500)
    fitness_tracker.calculate_net_balance()

    # Example usage for Task 3
    house = House("123 Main St", 500000, 2000, 4)
    house.display_info()

    commercial = CommercialSpace("456 Business Ave", 1000000, 5000, "Retail")
    commercial.display_info()

    # Example usage for Task 4
    product = Product("Shirt", 20, 2)
    print(f"Total Price: {product.calculate_total_price()}")

    discounted_product = DiscountedProduct("Shoes", 100, 1, 10)
    print(f"Discounted Total Price: {discounted_product.calculate_total_price()}")