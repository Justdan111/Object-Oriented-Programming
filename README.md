# Object-Oriented Programming Assignment

## Author
NGULUBE EMMANUEL DAN



## Overview
This project implements four different object-oriented programming systems in Python, demonstrating various OOP concepts including inheritance (single, multilevel, multiple), method overriding, and the use of the super() function. The systems include a Library Management System, Fitness Tracker, Real Estate Management System, and Online Shopping Cart.

## Features

### 1. Library Management System
- Multilevel inheritance implementation
- Classes: Book (base), BorrowableBook (intermediate), DigitalLibrary (derived)
- Functionality:
  - Add new physical and digital books
  - Record borrowing details
  - Display comprehensive book information

### 2. Fitness Tracker
- Multiple inheritance implementation
- Classes: StepCounter, CalorieTracker, FitnessTracker
- Features:
  - Record daily steps
  - Track calorie intake and burned calories
  - Calculate net calorie balance
  - Exception handling for invalid inputs

### 3. Real Estate Management System
- Method overriding demonstration
- Classes: Property (base), House and CommercialSpace (derived)
- Capabilities:
  - Add different types of properties
  - Display property-specific details
  - Interactive property management

### 4. Online Shopping Cart
- Super() function implementation
- Classes: Product (base), DiscountedProduct (derived)
- Features:
  - Add products with or without discounts
  - Calculate total prices with discounts
  - Remove products from cart

## Installation and Setup
1. Ensure Python 3.x is installed on your system
2. Download the `main.py` file
3. No additional dependencies are required

## Usage
1. Run the program using Python:
   ```bash
   python main.py
   ```
2. Follow the interactive menu to navigate between different systems
3. Choose options within each system to perform various operations
4. Input data as prompted
5. View results and summaries

## Program Structure
- Each task is implemented as separate classes
- Main menu provides access to all systems
- Input validation and error handling implemented throughout
- Clear separation of concerns between different functionalities

## Personal Reflection on OOP Concepts
Through this assignment, I've gained a deeper understanding of Object-Oriented Programming concepts and their practical applications. Here are key insights:

1. Inheritance has proven to be a powerful tool for code reuse and establishing relationships between classes. The Library Management System particularly demonstrated how multilevel inheritance can model real-world hierarchical relationships effectively.

2. Multiple inheritance, as implemented in the Fitness Tracker, showed how different functionalities can be combined while maintaining clean code organization. However, it also highlighted the importance of careful design to avoid potential conflicts.

3. Method overriding, demonstrated in the Real Estate Management System, illustrated how derived classes can maintain their uniqueness while adhering to a common interface. This showcased the flexibility of polymorphism in OOP.

4. The super() function, used in the Shopping Cart system, demonstrated elegant handling of parent class methods and attributes, making it easier to extend functionality while maintaining existing features.

These concepts together show how OOP principles can create maintainable, scalable, and well-organized code structures that mirror real-world relationships and interactions.

## Error Handling
- Input validation for numerical values
- Exception handling for invalid inputs
- Clear error messages for user feedback

## Limitations and Future Improvements
1. Data persistence could be added to store information between sessions
2. Additional features like search functionality could be implemented
3. User interface could be enhanced with a GUI
4. More sophisticated validation and error handling could be added
5. Reporting and analytics features could be incorporated



