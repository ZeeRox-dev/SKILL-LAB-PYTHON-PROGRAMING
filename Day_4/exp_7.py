class Student:
    def __init__(self, name, roll_number, marks):
        """Constructor to initialize student attributes"""
        self.name = name
        self.roll_number = roll_number
        self.marks = marks
    
    def display_details(self):
        """Method to display student details"""
        print(f"Student Details:")
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")
        print(f"Marks: {self.marks}")
        print("-" * 30)

# Creating two student objects
student1 = Student("Alice Johnson", "CS101", 85.5)
student2 = Student("Bob Smith", "CS102", 92.0)

# Displaying student details
print("Exercise 1: Student Class")
print("=" * 30)
student1.display_details()
student2.display_details()
print()

class Employee:
    # Class variable
    company = "ABC Technologies"
    
    def __init__(self, name, employee_id, salary):
        """Constructor to initialize instance variables"""
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
    
    def display_details(self):
        """Method to display employee details"""
        print(f"Employee Details:")
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Salary: ${self.salary:,.2f}")
        print(f"Company: {self.company}")  # Accessing class variable
        print("-" * 30)

print("Exercise 2: Class and Instance Variables")
print("=" * 30)

# Creating three employee objects
employee1 = Employee("John Doe", "E001", 50000)
employee2 = Employee("Jane Smith", "E002", 60000)
employee3 = Employee("Mike Wilson", "E003", 55000)

# Displaying employee details
print("Initial Company Name:")
employee1.display_details()
employee2.display_details()
employee3.display_details()

# Changing the company name using class variable
print("After changing company name to 'XYZ Corporation':")
Employee.company = "XYZ Corporation"

# Observe the effect on all objects
employee1.display_details()
employee2.display_details()
employee3.display_details()

# You can also change it for a specific instance only
employee2.company = "Special Assignment Corp"
print("After changing employee2's company individually:")
employee1.display_details()
employee2.display_details()
employee3.display_details()
print()

class Rectangle:
    def __init__(self, length, width):
        """Constructor to initialize rectangle dimensions"""
        self.length = length
        self.width = width
    
    def calculate_area(self):
        """Calculate and return the area of the rectangle"""
        return self.length * self.width
    
    def calculate_perimeter(self):
        """Calculate and return the perimeter of the rectangle"""
        return 2 * (self.length + self.width)
    
    def display_details(self):
        """Display rectangle details including area and perimeter"""
        area = self.calculate_area()
        perimeter = self.calculate_perimeter()
        print(f"Rectangle Details:")
        print(f"Length: {self.length} units")
        print(f"Width: {self.width} units")
        print(f"Area: {area} square units")
        print(f"Perimeter: {perimeter} units")
        print("-" * 30)

print("Exercise 3: Using self")
print("=" * 30)

# Creating two rectangle objects
rectangle1 = Rectangle(5, 3)
rectangle2 = Rectangle(7.5, 4.2)

# Displaying rectangle details
rectangle1.display_details()
rectangle2.display_details()

# Directly accessing area and perimeter
print("Direct access to calculations:")
print(f"Rectangle1 Area: {rectangle1.calculate_area()}")
print(f"Rectangle1 Perimeter: {rectangle1.calculate_perimeter()}")
print(f"Rectangle2 Area: {rectangle2.calculate_area()}")
print(f"Rectangle2 Perimeter: {rectangle2.calculate_perimeter()}")
print()

class BankAccount:
    def __init__(self, account_holder_name, initial_balance):
        """Constructor to initialize bank account"""
        self.account_holder_name = account_holder_name
        self.balance = initial_balance
        print(f"Account created for {self.account_holder_name} with initial balance ${self.balance:,.2f}")
    
    def deposit(self, amount):
        """Method to deposit money into the account"""
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:,.2f} into {self.account_holder_name}'s account")
            print(f"New balance: ${self.balance:,.2f}")
        else:
            print("Invalid deposit amount. Please enter a positive amount.")
        print("-" * 40)
    
    def withdraw(self, amount):
        """Method to withdraw money from the account"""
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew ${amount:,.2f} from {self.account_holder_name}'s account")
                print(f"New balance: ${self.balance:,.2f}")
            else:
                print(f"Insufficient funds! Cannot withdraw ${amount:,.2f}")
                print(f"Current balance: ${self.balance:,.2f}")
        else:
            print("Invalid withdrawal amount. Please enter a positive amount.")
        print("-" * 40)
    
    def display_balance(self):
        """Method to display current balance"""
        print(f"Account Holder: {self.account_holder_name}")
        print(f"Current Balance: ${self.balance:,.2f}")
        print("-" * 40)

print("Exercise 4: Constructor and Object Creation")
print("=" * 30)

# Creating two bank account objects
account1 = BankAccount("Alice Johnson", 1000)
account2 = BankAccount("Bob Smith", 500)

print("\nInitial balances:")
account1.display_balance()
account2.display_balance()

# Demonstrating independent balance maintenance
print("\nTransactions on Account 1:")
account1.deposit(500)
account1.withdraw(200)
account1.display_balance()

print("\nTransactions on Account 2:")
account2.deposit(1000)
account2.withdraw(750)
account2.display_balance()

# Demonstrating that balances are maintained independently
print("\nFinal balances showing independence:")
account1.display_balance()
account2.display_balance()