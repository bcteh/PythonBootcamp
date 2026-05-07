#sets are unordered collection of items, they are mutable and do not allow duplicate values
"""
fruits1={"apple","orange","durian","kiwi"}
fruits2={"grape","durian","kiwi"}

#    print(next(iter(fruits1)))
#    print(fruits1)

#    fruits1.add("banana")
#    print(fruits1)

#    fruits1.update(fruits2)
#    print(fruits1)


#sets intersection
intersection=fruits1.intersection(fruits2)
print(intersection)
union1=fruits1.union(fruits2)
print(union1)
difference1=fruits1.difference(fruits2)
print(difference1)
difference2=fruits2.difference(fruits1)
print(difference2)
print()
print()
"""
# Create a set to store unique student names as tuples of (student_name, subject, grade)
grades = {("Alice", "Math", 85),
  ("Bob", "Science", 92),
  ("Alice", "Science", 78),
  ("Charlie", "Math", 90),
  ("Bob", "Math", 88),
  ("Alice", "English", 95)}
 
#student_names = set() #same as student_names = {} but this is more clear that it is a set
#uses sets to find unique subjects and students
""""
for student, subject, grade in grades:
    student_names.add(student)
print("Name of Students:")
print(student_names)    
#uses sets to find unique subjects and students
subjects = set()
for student, subject, grade in grades:
    subjects.add(subject)
print("List of Subjects:")
print(subjects)
"""
#another way to find unique students and subjects using set comprehension
name2 = set()
subjects2 = set()
for name, subject, grade in grades:
    name2.add(name)
    subjects2.add(subject)
print("Unique students (method 2):", name2)
print("Unique subjects (method 2):", subjects2)