"""
Python Functions Comprehensive Program
Includes: Basic Functions, Default Arguments, Lambda Functions, and Combined Calculator
"""

# ===== EXERCISE 1: BASIC FUNCTIONS =====
def sum_two_numbers(a, b):
    """Calculate the sum of two numbers."""
    return a + b

def difference_two_numbers(a, b):
    """Calculate the difference between two numbers."""
    return a - b

def product_two_numbers(a, b):
    """Calculate the product of two numbers."""
    return a * b

def division_two_numbers(a, b):
    """Calculate the division of two numbers."""
    if b == 0:
        return "Error: Division by zero is not allowed!"
    return a / b

def exercise_1():
    """Execute Exercise 1: Basic Functions"""
    print("\n" + "="*50)
    print("EXERCISE 1: Basic Functions Calculator")
    print("="*50)
    
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        print(f"\nResults for {num1} and {num2}:")
        print(f"Sum: {sum_two_numbers(num1, num2)}")
        print(f"Difference: {difference_two_numbers(num1, num2)}")
        print(f"Product: {product_two_numbers(num1, num2)}")
        print(f"Division: {division_two_numbers(num1, num2)}")
        
    except ValueError:
        print("Error: Please enter valid numbers!")

# ===== EXERCISE 2: DEFAULT ARGUMENTS =====
def student_details(name, branch="VLSI", year=3):
    """
    Display student details with default arguments.
    """
    print(f"  Name: {name:<20} Branch: {branch:<20} Year: {year}")

def exercise_2():
    """Execute Exercise 2: Default Arguments"""
    print("\n" + "="*50)
    print("EXERCISE 2: Student Details with Default Arguments")
    print("="*50)
    
    print("\nDemonstrating different argument combinations:\n")
    
    print("1. All arguments provided:")
    student_details("Alice Smith", "Computer Science", 4)
    
    print("2. Only name (defaults for branch and year):")
    student_details("Bob Johnson")
    
    print("3. Name and branch (default year):")
    student_details("Charlie Brown", "Electronics")
    
    print("4. Name and year using keyword argument:")
    student_details("Diana Prince", year=2)
    
    print("5. All arguments, different order using keywords:")
    student_details(year=1, name="Eve Wilson", branch="Mechanical")

# ===== EXERCISE 3: LAMBDA FUNCTIONS =====
def exercise_3():
    """Execute Exercise 3: Lambda Functions"""
    print("\n" + "="*50)
    print("EXERCISE 3: Lambda Functions with Lists")
    print("="*50)
    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"\nOriginal list: {numbers}\n")
    
    # Squares using lambda
    squares = list(map(lambda x: x ** 2, numbers))
    print(f"Squares: {squares}")
    
    # Even/Odd using lambda
    even_odd = list(map(lambda x: "Even" if x % 2 == 0 else "Odd", numbers))
    print(f"Even/Odd: {even_odd}")
    
    # Detailed display
    print("\nDetailed classification:")
    for num, status in zip(numbers, even_odd):
        print(f"  {num:2} → {status}")
    
    # Cubes using lambda
    cubes = list(map(lambda x: x ** 3, numbers))
    print(f"\nCubes: {cubes}")

# ===== EXERCISE 4: COMBINED CALCULATOR =====
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b=1):
    """Division with default divisor of 1"""
    if b == 0:
        return "Error: Division by zero!"
    return a / b

def exercise_4():
    """Execute Exercise 4: Combined Calculator"""
    print("\n" + "="*50)
    print("EXERCISE 4: Advanced Calculator with Lambda")
    print("="*50)
    
    print("\nOperations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    try:
        choice = input("\nEnter operation (1-4): ").strip()
        
        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice!")
            return
        
        num1 = float(input("Enter first number: "))
        
        if choice == '4':
            num2_input = input("Enter second number (Enter for default=1): ").strip()
            num2 = float(num2_input) if num2_input else 1
        else:
            num2 = float(input("Enter second number: "))
        
        # Perform operation
        operations = {'1': ('+', add), '2': ('-', subtract), 
                     '3': ('*', multiply), '4': ('/', divide)}
        
        symbol, func = operations[choice]
        result = func(num1, num2)
        
        print(f"\n{num1} {symbol} {num2} = {result}")
        
        # Lambda for square
        if isinstance(result, (int, float)):
            square = (lambda x: x ** 2)(result)
            print(f"Square of result ({result})² = {square}")
        else:
            print(result)
            
    except ValueError:
        print("Error: Please enter valid numbers!")
    except Exception as e:
        print(f"Error: {e}")

# ===== MAIN MENU =====
def main():
    """Main menu to access all exercises"""
    while True:
        print("\n" + "="*50)
        print("PYTHON FUNCTIONS - COMPREHENSIVE PROGRAM")
        print("="*50)
        print("\nSelect an exercise to run:")
        print("1. Basic Functions (Sum, Difference, Product, Division)")
        print("2. Default Arguments (Student Details)")
        print("3. Lambda Functions (Squares, Even/Odd, Cubes)")
        print("4. Combined Calculator with Lambda")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == '1':
            exercise_1()
        elif choice == '2':
            exercise_2()
        elif choice == '3':
            exercise_3()
        elif choice == '4':
            exercise_4()
        elif choice == '5':
            print("\nThank you for using the program. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter 1-5.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()