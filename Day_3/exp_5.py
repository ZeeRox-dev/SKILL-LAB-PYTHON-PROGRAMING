print("=" * 50)
print("EXERCISE 1: Number List Processing")
print("=" * 50)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Original list: {numbers}")
print(f"Squares: {[num**2 for num in numbers]}")
print(f"Even numbers: {[num for num in numbers if num % 2 == 0]}")
print(f"Signs: {['Positive' if num >= 0 else 'Negative' for num in numbers]}")

print("\n" + "=" * 50)
print("EXERCISE 2: Student Marks")
print("=" * 50)

marks = [45, 67, 89, 34, 78, 56, 91, 48, 62, 73]
print(f"Original marks: {marks}")
print(f"Marks >= 50: {[mark for mark in marks if mark >= 50]}")
print(f"Marks with grace (+5): {[mark + 5 for mark in marks]}")
print(f"Results: {['Pass' if mark >= 50 else 'Fail' for mark in marks]}")

print("\n" + "=" * 50)
print("EXERCISE 3: Dictionary of Squares")
print("=" * 50)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
square_dict = {num: num**2 for num in numbers}
print(f"Square dictionary: {square_dict}")
even_squares = {num: num**2 for num in numbers if (num**2) % 2 == 0}
print(f"Even squares dictionary: {even_squares}")

print("\n" + "=" * 50)
print("EXERCISE 4: Product Prices")
print("=" * 50)

products = {
    "Notebook": 45, "Pen": 15, "Laptop": 45000,
    "Mouse": 350, "Keyboard": 1200, "Headphones": 800,
    "USB Drive": 500, "Monitor": 15000, "Desk Lamp": 400,
    "Charger": 250
}
print(f"Original products: {products}")
print(f"Products > ₹500: { {k: v for k, v in products.items() if v > 500} }")
print(f"With 10% discount: { {k: v*0.9 for k, v in products.items()} }")
print(f"Products ≤ ₹500: {[k for k, v in products.items() if v <= 500]}")