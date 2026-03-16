# Data Types in Python
name = "Nisha"
experience = 4
salary = 50000.0
is_ready_to_switch = True

# collections
# List - ordered, mutable, allows duplicates
skills = ["python", "selenium", "pytest","python"]
print(skills[1])

# Tuple - ordered, immutable, allows duplicates
browser = ("chrome", "Firefox")

# Set - unordered, mutable, no duplicates
unique_skills = {"python", "selenium", "python"}
print(unique_skills)

# Dictionary - unordered, mutable, key- value pairs
candidate = {
    "name": "Nisha",
    "experience": 4,
    "skills": ["python", "selenium", "pytest"]
}
print(candidate["skills"])

# Task Create one dictionary for your profile with:
# name, experience, skills, and is_ready_to_switch

my_profile = {
    "name": "Arulmozhi",
    "experience": 4,
    "primary_skills": ["python", "selenium", "pytest"],
    "is_ready_to_switch": True
}
print(my_profile["name"])

# Conditions
score = 85
if score > 70:
    print("ready for next level")
else:
    print("need to practice more")

# Loops
# For loop
for skill in skills:
    print(skill)

# While loop
count = 1
while count <=5:
    print(count)
    count +=1

# Functions
# Functions are very important because automation frameworks use reusable methoda everywhere.
def greet(name):
    print(f"Hello, {name}")
greet("Asha")

# Function with return value
def add(a, b):
    return a + b
print(add(5,3))

#task: 
def login_status(is_logged_in):
    if is_logged_in:
        return "Login sussessful"
    else:
        return "Login failed"
print(login_status(False))

# String
text = "Automation Testing"

print(text.lower())
print(text.upper())
print(text.replace("Testing", "Framework"))
print(text.split())

#task
email = "   testuser@gmail.com   "
print(email.strip())
print(email.lower())
print(email.find("gmail"))

# Exception Handling
try:
    num = int("abc")
    print(num)
except ValueError:
    print("Invalid number")

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")

# File handling
with open("sample.txt", "w") as file:
    file.write("Hello Nish")
with open("sample.txt", "r") as file:
    content = file.read()
    print(content)

# OOP basics
# very important for framework design
class LoginPage:
    def open_page(self):
        print("Opening login page")

page = LoginPage()
page.open_page()

# constructors
class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def display(self):
        print(self.name, self.role)
emp1 = Employee("Nisha", "QA Engineer")
emp1.display()

# practise Questions
"""
1. what is the diffrent between list and tuple?
List and tuple come under collections in python. List is ordered,mutable, duplications allowed.Defined with square brackets[].
Tuple ore ordered immutable, duplications allowed.Defined with parenthesis.

2. what is the diffrent between set and dictionary?
Set is unodered, mutable, no duplicates. Defined with curly braces{}.
Dictionary is unodred, mutable, key value pairs. Defined with curly braces.

3. what is the diffrence between == and =?
= is for assigning value to a variable.
== is for comparing two values.

4. what is the diffrence between function and method?
Function is a block of code that performs a specific task and can be called independently.
Method is a function that is associated with an object and can access the data of that object.

5. what is the diffrence between break and continue?
break is used to exit the loop completely.
continue is used to skip current iteration and move to the next iteration of the loop.

"""

# coding challenge
# 1. print even numbers from 1 to 20
for i in range(1, 21):
    if i % 2 == 0:
        print(i)

# 2. Count number of vowels in a string
str = "Nisha"
count = 0
vowels = ["a","e","i","o","u"]
for i in str:
    if i in vowels:
        count += 1
print(count)

# 3. Reverse string
print(str[::-1])

# 4. Duplicate items in a list
items = [10, 20, 30, 10, 40, 20, 50]
seen = set()
duplicates = set()
for item in items:
    if item in seen:
        duplicates.add(item)
    else:
        seen.add(item)
print(duplicates)

#5. check prime number
def is_prime(num):
    if num <= 1:
        return "Not prime"
    for i in range(2, num):
        if num % i == 0:
            return "Not Prime"
    return "Prime"
print(is_prime(7))
    