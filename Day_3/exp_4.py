# # Student Grade and Result System
# print("=" * 50)
# print("STUDENT GRADE AND RESULT SYSTEM")
# print("=" * 50)

# while True:
#     total = 0
#     subjects = []
    
#     print("\nEnter marks for 5 subjects (out of 100):")
    
#     # Accept marks for 5 subjects using for loop
#     for i in range(1, 6):
#         while True:
#             try:
#                 marks = float(input(f"Subject {i}: "))
#                 if 0 <= marks <= 100:
#                     subjects.append(marks)
#                     total += marks
#                     break
#                 else:
#                     print("Please enter marks between 0 and 100!")
#             except ValueError:
#                 print("Invalid input! Please enter a number.")
    
#     # Calculate percentage
#     percentage = total / 5
    
#     # Assign grade using if-elif-else
#     if percentage >= 90:
#         grade = "A+"
#     elif percentage >= 80:
#         grade = "A"
#     elif percentage >= 70:
#         grade = "B"
#     elif percentage >= 60:
#         grade = "C"
#     elif percentage >= 50:
#         grade = "D"
#     else:
#         grade = "F"
    
#     # Display results
#     print("\n" + "=" * 30)
#     print("RESULT")
#     print("=" * 30)
#     print(f"Total Marks: {total:.2f}/500")
#     print(f"Percentage: {percentage:.2f}%")
#     print(f"Grade: {grade}")
    
#     # Ask if user wants to continue
#     choice = input("\nDo you want to calculate for another student? (yes/no): ").lower()
#     if choice != 'yes':
#         print("\nThank you for using the Student Grade System!")
#         break


# # Menu-Driven Calculator
# print("=" * 40)
# print("MENU-DRIVEN CALCULATOR")
# print("=" * 40)

# while True:
#     # Display menu
#     print("\n--- Calculator Menu ---")
#     print("1. Addition")
#     print("2. Subtraction")
#     print("3. Multiplication")
#     print("4. Division")
#     print("5. Exit")
    
#     choice = input("\nEnter your choice (1-5): ")
    
#     # Exit condition
#     if choice == '5':
#         print("Thank you for using the calculator. Goodbye!")
#         break
    
#     # Validate menu choice
#     if choice not in ['1', '2', '3', '4']:
#         print("Invalid choice! Please select 1-5.")
#         continue
    
#     # Get numbers from user
#     try:
#         num1 = float(input("Enter first number: "))
#         num2 = float(input("Enter second number: "))
#     except ValueError:
#         print("Invalid input! Please enter numbers only.")
#         continue
    
#     # Perform operation using match-case
#     match choice:
#         case '1':
#             result = num1 + num2
#             print(f"\n{num1} + {num2} = {result}")
        
#         case '2':
#             result = num1 - num2
#             print(f"\n{num1} - {num2} = {result}")
        
#         case '3':
#             result = num1 * num2
#             print(f"\n{num1} × {num2} = {result}")
        
#         case '4':
#             # Handle division by zero
#             if num2 == 0:
#                 print("\nError: Division by zero is not allowed!")
#             else:
#                 result = num1 / num2
#                 print(f"\n{num1} ÷ {num2} = {result}")
    
#     input("\nPress Enter to continue...")

# Number Analysis Program
print("=" * 40)
print("NUMBER ANALYSIS PROGRAM")
print("=" * 40)
print("Enter 10 integers (or 999 to quit early):")

positive_count = 0
negative_count = 0
zero_count = 0
positive_sum = 0

for i in range(1, 11):
    while True:
        try:
            num = int(input(f"Enter number {i}: "))
            break
        except ValueError:
            print("Invalid input! Please enter an integer.")
    
    # Check for early termination
    if num == 999:
        print("\nEarly termination requested (999 entered).")
        break
    
    # Determine if positive, negative, or zero
    if num > 0:
        positive_count += 1
        positive_sum += num
        print(f"  → {num} is positive")
    elif num < 0:
        negative_count += 1
        print(f"  → {num} is negative (skipping)")
        continue  # Skip negative numbers (won't be added to sum)
    else:
        zero_count += 1
        print(f"  → {num} is zero")

# Display analysis results
print("\n" + "=" * 30)
print("ANALYSIS RESULTS")
print("=" * 30)
print(f"Positive numbers: {positive_count}")
print(f"Negative numbers: {negative_count}")
print(f"Zeros entered: {zero_count}")
print(f"Sum of positive numbers: {positive_sum}")