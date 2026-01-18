# Assignment 1; Technical Training 16-01-2026; CS3K

# SETS QUESTIONS.

# Write a program to find all unique characters in a string using a set.
s = input()
u = set(s)
for i in u:
    print(i)
"""
# Given two lists of students (cricket and football), find students who play both sports (intersection).
c = input().split()
f = input().split()
i = set(c) & set(f)
print(list(i))

# Given two lists of students, find students who play only cricket (difference).
c = input().split()
f = input().split()
d = set(c) - set(f)
print(list(d))

# Take a sentence as input and print all unique words using a set.
s = input()
w = set(s.split())
for i in w:
    print(i)

# Write a program to check if two sets are equal (ignoring order)
s1 = set(input().split())
s2 = set(input().split())
print(s1 == s2)

# Create two sets and check if they have at least one element in common (hint: use intersection)
s1 = set(input().split())
s2 = set(input().split())
print(len(s1 & s2) > 0)

# write a program to find the number of unique elements in a list using a set.
l = input().split()
u = set(l)
print(len(u))

# ---
# DICTIONARY MANIPULATION.
# create a dictionary of 5 countries and their capitals.
d = {
    "India": "New Delhi",
    "USA": "Washington",
    "UK": "London",
    "France": "Paris",
    "Japan": "Tokyo",
}
print(d)
# Access India.
print(d["India"])
# Add a new key- value pair "japan" : "Tokyo" to the dictionary.
d["Japan"] = "Tokyo"
print(d)
# Update the capital of "USA" from "Washington" to "New York"
d["USA"] = "New York"
print(d)
# Delete the key France using del.
del d["France"]
print(d)

# Create a dictionary of students and marks. Use .keys() to print all student names.
d = {"Aman": 85, "Riya": 92, "Karan": 78, "Neha": 88, "Sonal": 90}
print(d.keys())
# use .values() to print all marks.
print(d.values())
# Use .items() to print all marks.
print(d.items())
# Use .get() to access the value of "Rahul" safely (if not found, return "Not Found.")
print(d.get("Rahul", "Not Found."))
# Use .update() to add multiple key-value pairs in one step.
d.update({"Neha": 88, "Sonal": 90})
print(d)

# Use .pop(key) to remove "Germany" from the dictionary.
d = {
    "India": "New Delhi",
    "USA": "Washington",
    "Germany": "Berlin",
    "UK": "London",
    "France": "Paris",
}
d.pop("Germany")
print(d)

# Try popping a non-existing key using .pop() with a default value.
d = {"India": "New Delhi", "USA": "Washington", "UK": "London", "France": "Paris"}
print(d.pop("Germany", "Not Found"))

# Use .clear() to remove all elements from the dictionary.
d = {
    "India": "New Delhi",
    "USA": "Washington",
    "UK": "London",
    "France": "Paris",
    "Japan": "Tokyo",
}
d.clear()
print(d)

# Create a dictionary, make a copy using .copy() and update the copy without affecting the original.
d = {"Aman": 85, "Riya": 92, "Karan": 78}
c = d.copy()
c["Neha"] = 88
print("Original:", d)
print("Copy:", c)

# Count the frequency of words in a sentence using a dictionary.
s = input()
f = {}
for w in s.split():
    f[w] = f.get(w, 0) + 1
print(f)

# Store product name as keys and prices as values. Print products costing more than 100.
d = {"Milk": 90, "Eggs": 150, "Bread": 50, "Cheese": 200, "Butter": 120}
for k, v in d.items():
    if v > 100:
        print(k)

# Write a program to check if "Apple" exists as a key in a dictionary.
d = {"Banana": 50, "Apple": 100, "Mango": 150}
print("Apple" in d)

# Find the key with the maximum value in a dictionary of student marks.
d = {"Aman": 85, "Riya": 92, "Karan": 78, "Neha": 88, "Sonal": 90}
m = max(d, key=d.get)
print(m)

# Convert two lists into a dictionary (e.g. ["name", "age", "city"] and ["Amit", 25, "Delhi"])
k = ["name", "age", "city"]
v = ["Amit", 25, "Delhi"]
d = dict(zip(k, v))
print(d)

# Swap keys and values in a dictionary.
d = {"Aman": 85, "Riya": 92, "Karan": 78}
s = {v: k for k, v in d.items()}
print(s)

# ---
# LISTS AND DICTIONARIES

students = {
    # Create a dictionary with two keys "names" and "ages", storing 3 students.
    "names": ["Amit", "Neha", "Rahul"],
    "ages": [20, 22, 19],
}

# Print the first student's name and age.
print(students["names"][0], students["ages"][0])

# Add a new student "Priya", 21 to both lists.
students["names"].append("Priya")
students["ages"].append(21)

# Update "Rahul's" age to 20.
i = students["names"].index("Rahul")
students["ages"][i] = 20

# Remove "Neha" and her age from both lists.
i = students["names"].index("Neha")
students["names"].pop(i)
students["ages"].pop(i)

# Find the student with the maximum age.
i = students["ages"].index(max(students["ages"]))
print(students["names"][i])

# Print all students older than 20.
for i in range(len(students["ages"])):
    if students["ages"][i] > 20:
        print(students["names"][i])

# Convert the dictionary of lists into list of dictionaries.
l = [
    {"name": students["names"][i], "age": students["ages"][i]}
    for i in range(len(students["names"]))
]
print(l)

# Convert the dictionary of lists into a Pandas DataFrame (if pandas is available.)
import pandas as pd  # Used stackflow for understanding.

df = pd.DataFrame(students)
print(df)

# Sort students by age using the dictionary of lists.
z = sorted(zip(students["ages"], students["names"]))
students["ages"], students["names"] = zip(*z)
print(students)
"""
