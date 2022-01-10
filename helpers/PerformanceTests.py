'''
Created on 10 Jan 2022

@author: Jesper Kristiansson
'''
import time


def runtime(method):
    start_time = time.time()
    method()
    end_time = time.time()
    return end_time - start_time

def print_average_time(method, n):
    total_time = 0
    for _ in range(n):
        total_time += runtime(method)
    print("--- %s seconds ---" % round(total_time/n, 5))