# Implement a solution using Thread, that starts a thread execution, puts the thread in 2s wait and shows the thread
# execution start/end
from time import sleep
from threading import Thread

def task(waiting_time, message):
    print(f'Starting the task: {message}')
    sleep(waiting_time)
    print(f'Finishing the task: {message}')


thread = Thread(target=task, args=(2, 'Thread in execution'))
thread.start()
print('\nWaiting for thread execution')
thread.join()
print('The execution was completed!')
