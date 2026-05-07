student_records = {
    "student_001": {
        "name": "John",
        "age": 19,
        "major": "Computer Science",
        "grades": [85, 92, 78]
    },
    "student_002": {
        "name": "Sarah",
        "age": 20,
        "major": "Biology",
        "grades": [90, 88, 95]
    }
}
print(student_records["student_001"]["name"])  # Output: John
print(student_records["student_002"]["grades"])  # Output: [90, 88, 95] 
print(student_records["student_001"]["grades"][1])  # Output: 92

# Adding a new student record
student_records["student_003"] = {
    "name": "Mike",       
    "age": 18,
    "major": "Mathematics",
    "grades": [88, 79, 91]
}
# Updating an existing student record
student_records["student_001"]["age"] = 20

# Deleting a student record
# del student_records["student_002"]

print(student_records)