

# Library Management System - Task 1
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
    
    def display_details(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nISBN: {self.isbn}"

class BorrowableBook(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, author, isbn)
        self.borrower_name = None
        self.borrow_date = None
    
    def borrow(self, borrower_name, borrow_date):
        self.borrower_name = borrower_name
        self.borrow_date = borrow_date
    
    def display_details(self):
        details = super().display_details()
        if self.borrower_name:
            details += f"\nBorrowed by: {self.borrower_name}\nBorrow Date: {self.borrow_date}"
        return details

class DigitalLibrary(Book):
    def __init__(self, title, author, isbn, ebook_link):
        super().__init__(title, author, isbn)
        self.ebook_link = ebook_link
    
    def display_details(self):
        return f"{super().display_details()}\nE-book Link: {self.ebook_link}"


# Fitness Tracker - Task 2
class StepCounter:
    def __init__(self):
        self.daily_steps = 0
    
    def record_steps(self, steps):
        if steps < 0:
            raise ValueError("Steps cannot be negative")
        self.daily_steps = steps
        return self.daily_steps

class CalorieTracker:
    def __init__(self):
        self.calories_intake = 0
        self.calories_burnt = 0
    
    def record_calories(self, intake, burnt):
        if intake < 0 or burnt < 0:
            raise ValueError("Calories cannot be negative")
        self.calories_intake = intake
        self.calories_burnt = burnt
        return self.calories_intake - self.calories_burnt

class FitnessTracker(StepCounter, CalorieTracker):
    def __init__(self):
        StepCounter.__init__(self)
        CalorieTracker.__init__(self)
    
    def calculate_net_calories(self):
        steps_calories = self.daily_steps * 0.04  # Assuming 0.04 calories per step
        total_burnt = self.calories_burnt + steps_calories
        return self.calories_intake - total_burnt

    def daily_summary(self):
        net_calories = self.calculate_net_calories()
        return {
            "steps": self.daily_steps,
            "calories_intake": self.calories_intake,
            "calories_burnt": self.calories_burnt,
            "net_calories": net_calories
        }


# Real Estate Management - Task 3
class Property:
    def __init__(self, address, price, size):
        self.address = address
        self.price = price
        self.size = size
    
    def display_info(self):
        return f"Address: {self.address}\nPrice: ${self.price:,.2f}\nSize: {self.size} sq ft"

class House(Property):
    def __init__(self, address, price, size, bedrooms):
        super().__init__(address, price, size)
        self.bedrooms = bedrooms
    
    def display_info(self):
        return f"{super().display_info()}\nBedrooms: {self.bedrooms}"

class CommercialSpace(Property):
    def __init__(self, address, price, size, business_type):
        super().__init__(address, price, size)
        self.business_type = business_type
    
    def display_info(self):
        return f"{super().display_info()}\nBusiness Type: {self.business_type}"


# Shopping Cart - Task 4
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def calculate_total(self):
        return self.price * self.quantity
    
    def display_info(self):
        return f"{self.name} - ${self.price:.2f} x {self.quantity}"

class DiscountedProduct(Product):
    def __init__(self, name, price, quantity, discount_percentage):
        super().__init__(name, price, quantity)
        self.discount_percentage = discount_percentage
    
    def calculate_total(self):
        original_total = super().calculate_total()
        discount = original_total * (self.discount_percentage / 100)
        return original_total - discount
    
    def display_info(self):
        return f"{super().display_info()} (Discount: {self.discount_percentage}%)"


# Main Program
def main():
    # Initialize collections
    library_books = []
    fitness_tracker = FitnessTracker()
    properties = []
    shopping_cart = []
    
    while True:
        print("\nMain Menu:")
        print("1. Library Management")
        print("2. Fitness Tracker")
        print("3. Real Estate Management")
        print("4. Shopping Cart")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            # Library Management Menu
            print("\nLibrary Management:")
            print("1. Add Book")
            print("2. Borrow Book")
            print("3. View Books")
            lib_choice = input("Enter choice (1-3): ")
            
            if lib_choice == "1":
                title = input("Enter title: ")
                author = input("Enter author: ")
                isbn = input("Enter ISBN: ")
                book_type = input("Enter type (physical/digital): ")
                
                if book_type.lower() == "physical":
                    library_books.append(BorrowableBook(title, author, isbn))
                else:
                    ebook_link = input("Enter e-book link: ")
                    library_books.append(DigitalLibrary(title, author, isbn, ebook_link))
            
            elif lib_choice == "2":
                # Implement borrowing functionality
                pass
            
            elif lib_choice == "3":
                for book in library_books:
                    print("\n" + book.display_details())
        
        elif choice == "2":
            # Fitness Tracker Menu
            try:
                steps = int(input("Enter steps taken: "))
                intake = float(input("Enter calories consumed: "))
                burnt = float(input("Enter calories burnt: "))
                
                fitness_tracker.record_steps(steps)
                fitness_tracker.record_calories(intake, burnt)
                
                summary = fitness_tracker.daily_summary()
                print("\nDaily Summary:")
                for key, value in summary.items():
                    print(f"{key.replace('_', ' ').title()}: {value}")
            
            except ValueError as e:
                print(f"Error: {e}")
        
        elif choice == "3":
            # Real Estate Management Menu
            print("\nReal Estate Management:")
            print("1. Add Property")
            print("2. View Properties")
            prop_choice = input("Enter choice (1-2): ")
            
            if prop_choice == "1":
                address = input("Enter address: ")
                price = float(input("Enter price: "))
                size = float(input("Enter size (sq ft): "))
                prop_type = input("Enter type (house/commercial): ")
                
                if prop_type.lower() == "house":
                    bedrooms = int(input("Enter number of bedrooms: "))
                    properties.append(House(address, price, size, bedrooms))
                else:
                    business_type = input("Enter business type: ")
                    properties.append(CommercialSpace(address, price, size, business_type))
            
            elif prop_choice == "2":
                for prop in properties:
                    print("\n" + prop.display_info())
        
        elif choice == "4":
            # Shopping Cart Menu
            print("\nShopping Cart:")
            print("1. Add Product")
            print("2. View Cart")
            print("3. Remove Product")
            cart_choice = input("Enter choice (1-3): ")
            
            if cart_choice == "1":
                name = input("Enter product name: ")
                price = float(input("Enter price: "))
                quantity = int(input("Enter quantity: "))
                has_discount = input("Has discount? (yes/no): ").lower() == "yes"
                
                if has_discount:
                    discount = float(input("Enter discount percentage: "))
                    shopping_cart.append(DiscountedProduct(name, price, quantity, discount))
                else:
                    shopping_cart.append(Product(name, price, quantity))
            
            elif cart_choice == "2":
                total = 0
                print("\nCart Contents:")
                for item in shopping_cart:
                    print(item.display_info())
                    total += item.calculate_total()
                print(f"\nTotal Amount: ${total:.2f}")
            
            elif cart_choice == "3":
                name = input("Enter product name to remove: ")
                shopping_cart = [item for item in shopping_cart if item.name != name]
        
        elif choice == "5":
            print("Thank you for using the system!")
            break

if __name__ == "__main__":
    main()