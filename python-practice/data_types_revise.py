"""
OOP helps in reusbale, maintainable and scalable automation frameworks by organizing code into classes like page objects,base classes and utilities.
It reduces duplication and improves readbility.
"""
error_elements = ["Invalid username", "password requires", "Account locked"]
errors = []
for e in error_elements:
    errors.append(e)
print(errors)

users = ["admin", "test", "admin", "guest"]

unique_users = list(set(users))
print(unique_users)

results = ["pass", "fail", "pass", "fail", "pass"]
pass_count = results.count("pass")
fail_count = results.count("fail")

print(f"pass fail count", pass_count,fail_count)

response = {
    "status": "success",
    "user" : "admin"
}
if "status" in response and response["status"] == "success":
    print('API passed')

elements = ["home", "login", "Dasboard"]
texts = [el.lower() for el in elements]
print(texts)

failures = ["TC1", "TC2", "TC1", "TC3"]
# seen = set()
# duplicate = set()
# for el in failures:
#     if el in seen:
#         duplicate.add(el)
#     else:
#         seen.add(el)
# print(duplicate)

duplicate = []
for el in failures:
    if failures.count(el) >1 and el not in duplicate:
        duplicate.append(el)
print(duplicate)

config = {
    "url": "https://test.com",
    "timeout": 10
}

if "url" in config:
    print("valid config")

# Practice
#Task 1: UI Cleanup Scenario
elements = ["Home", "Login", "Login", "Dashboard"]
# unique_elements = set(elements)
# print(unique_elements)
# for el in unique_elements:
#     print(el.lower())
for i in elements:
    if not elements.count(i) > 1:
        print(i)

#Task 2: Failure Analyzer (Advanced)
results = ["pass", "fail", "fail", "pass", "fail"]  
pass_count = results.count("pass")
fail_count = results.count("fail")
Failure_precentage =(fail_count / len(results)) * 100
print(f"Pass",pass_count)
print(f"Fail", fail_count)
print(f"Failure percentage", Failure_precentage,"%")

#Task 3: API Validation (Real Scenario)
response = {
    "status": "success",
    "code": 200,
    "data": ["user1", "user2"]
}
print(response["status"] == "success")
print(response["code"] == 200)

print(len(response["data"]))
for el in response["data"]:
    print(el.count(el))

#Task 5: Data Transformation (Important)
names = ["Nish", "Rahul", "Aman"]
print([el.upper() for el in names])