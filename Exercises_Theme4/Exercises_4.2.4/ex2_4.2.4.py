# Implement a solution using Thread, that starts 2 threads, (the 1st one must calculate the cube of a number, the 2nd
# one must calculate the square of a number), puts the 1st thread on 3s waiting and the 2nd thread on 2s waiting and
# indicates the threads enforcement order
from time import sleep
from threading import Thread

def function_cube(waiting_time, number):
    print(f'Cube: {number ** 3}')
    sleep(waiting_time)
    print(f'Finishing task function_cube')

def function_square(waiting_time, number):
    print(f'Square: {number ** 2}')
    sleep(waiting_time)
    print(f'Finishing task function_square')

t1 = Thread(target=function_square, args=(3, 5))
t2 = Thread(target=function_cube, args=(2, 5))
t1.start()
t2.start()
t1.join()
t2.join()
print("The execution was completed!")
