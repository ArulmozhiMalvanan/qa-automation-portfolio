import threading
import multiprocessing
import time

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
    time.sleep(2)

def test_dashboard():
    print("Dasshboard test")
    time.sleep(2)
start = time.time()
test_login()
test_dashboard()
end = time.time()
print("Time:", end - start)

t1 = threading.Thread(target=test_login)
t2 = threading.Thread(target=test_dashboard)
start = time.time()
t1.start()
t2.start()
end = time.time()
print("Time:", end - start)

#Multiprocessing


# def task():
#     print("Running task")

# p1 = multiprocessing.Process(target=task)
# p2 = multiprocessing.Process(target=task)

# p1.start()
# p2.start()

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
if __name__ == "__main__":
    p1 = multiprocessing.Process(target=test_login)
    p2 = multiprocessing.Process(target=test_dashboard)

    start = time.time()

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    end = time.time()
    print(end-start)
    
