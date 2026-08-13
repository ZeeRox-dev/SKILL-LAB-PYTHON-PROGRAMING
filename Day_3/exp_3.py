# Store information about three students using a nested dictionary
students = {
    "student1": {
        "name": "Rahul",
        "age": 20,
        "marks": 85
    },
    "student2": {
        "name": "Amit",
        "age": 21,
        "marks": 90
    },
    "student3": {
        "name": "Priya",
        "age": 19,
        "marks": 95
    }
}

# Print all three students
print("=== All Students ===")
print(students)
print()

# Print Rahul's marks
print("=== Rahul's Marks ===")
print(students["student1"]["marks"])
print()

# Print Priya's age
print("=== Priya's Age ===")
print(students["student3"]["age"])
print()

# Print each student's name and marks using a loop
print("=== Student Names and Marks ===")
for student_id, student_info in students.items():
    print(f"{student_info['name']}: {student_info['marks']}")
print()

# Add a new student
students["student4"] = {
    "name": "Sneha",
    "age": 22,
    "marks": 88
}
print("=== After Adding New Student ===")
for student_id, student_info in students.items():
    print(f"{student_id}: {student_info}")
print()

# Modify one student's marks
students["student2"]["marks"] = 92
print("=== After Modifying Amit's Marks ===")
print(f"Amit's new marks: {students['student2']['marks']}")
print()

# Remove one student
del students["student1"]
print("=== After Removing Student1 (Rahul) ===")
for student_id, student_info in students.items():
    print(f"{student_id}: {student_info['name']}")
print()

# Check whether "student2" exists
print("=== Check if student2 Exists ===")
if "student2" in students:
    print("student2 exists in the dictionary")
else:
    print("student2 does not exist in the dictionary")
print()

# Print the number of students using len()
print("=== Number of Students ===")
print(f"Total students: {len(students)}")