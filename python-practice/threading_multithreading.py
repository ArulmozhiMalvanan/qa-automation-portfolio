import threading
import multiprocessing

def task1():
    print("Task1 running")
def task2():
    print("task 2 running")

t1 = threading.Thread(target=task1)
t2 = threading.Thread(target = task2)

t1.start()
t2.start()

#real automation
def test_login():
    print("login test")

def test_dashboard():
    print("Dasshboard test")

t1 = threading.Thread(target=test_login)
t2 = threading.Thread(target=test_dashboard)

t1.start()
t2.start()

#Multiprocessing


def task():
    print("Running task")

p1 = multiprocessing.Process(target=task)
p2 = multiprocessing.Process(target=task)

p1.start()
p2.start()

#Interview questions
"""
1. Diffrence between thread and multiprocessing?
Threading runs tasks in same process with shared memory,while multiprocessing
runs tasks in seperate process with independent memory, allowing true parllel executtion.

2.why multi processing is better for parellel execution?
True CPU parlleleism
No Global intpretor lock

3.where is this used in automation?
Thread --> UI, I/O bounds, Light weight,shared memory
Multiprocessing -> CI/CD pipeline, testcase parllel run.

"""

