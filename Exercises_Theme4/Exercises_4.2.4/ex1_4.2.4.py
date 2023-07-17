# Implement a solution using Thread, that starts 2 threads, puts the 1st thread on 3s waiting and the 2nd thread on 2s
# waiting and indicates the threads enforcement order
from time import sleep
from threading import Thread

def task(waiting_time, task_name):
    print(f'Starting Thread {task_name}')
    sleep(waiting_time)
    print(f'Finishing Thread {task_name}')

t1 = Thread(target=task, args=(3, 'A'))
t2 = Thread(target=task, args=(2, 'B'))
t1.start()
t2.start()
t1.join()
t2.join()
print("The execution was completed!")
