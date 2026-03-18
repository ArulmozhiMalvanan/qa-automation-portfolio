"""
undertand how python loops actually work(iterators)
Know how to write memory-efficient code(genrators)
use decorators like real frameworks(logging, retry, reporting)
"""
import time
it = iter([1,2,3])
print(next(it))
print(next(it))
print(next(it))
#iter() --> converts objects to iterator
#next() --> gets next value
"""
What is the diffrence between iterable and iterator?
iterable --> can be looped (list,string)
iterator --> object with next()
"""

#Genrators(Memory efficient iteration)
numbers = [1,2,3,4,5,100000]

def num_gen():
    for i in range(1,100000):
        yield i
gen = num_gen()
print(next(gen))
print(next(gen))

def user_geneartor():
    for i in range(1,10):
        yield f"user{i}"
for user in user_geneartor():
    print(user)


# PART 3: Decorators
"""
What is decorator ?
A function that modifies another function
"""

def say_hello():
    print("Hello")

def say_hi():
    print("Hi")

def add_wrapper(func):
    def wrapper():
        print("start")
        func()
        print("end")
    return wrapper

say_hello = add_wrapper(say_hello)

say_hello()

@add_wrapper
def say_hi():
    print("Hi")

say_hi()
#Task G1 (Smallest possible)
def generate():
    yield 1
    yield 2
    yield 3

gen = generate()
print(next(gen))
print(next(gen))
print(next(gen))

#Task G2 (Slight upgrade)
def generate_for():
    for i in range(1,6):
        yield i
for i in generate_for():
    print(i)

#Task G3 (Real-life style)
def login():
    for i in range(1,4):
        yield f"user{i}"
for i in login():
    print(i)

#Task D1 (Smallest possible)
def my_deco(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper
@my_deco
def greet():
    print("Hello")

greet()

# Task D2 (Make it real)
def my_decor(func):
    def wrap():
        print(f"Test Started",func.__name__)
        func()
        print(f"Test Ended",func.__name__)
    return wrap
@my_decor
def test_login():
    print("login running")
              
test_login()

def genrator():
    for i in range(1,11):
        if i % 2 == 0:
            yield i
for i in genrator():
    print(i)

def my_decor(func):
    def wrap(*args, **kwargs):
        print(f"Test Started",func.__name__)
        func(*args, **kwargs)
        print(f"Test Ended",func.__name__)
    return wrap
@my_decor
def test_login(user):
    start = time.time()
    print(f"login running",user)
    end = time.time()
    print("Execution time:", end - start)

test_login("nisha")
              