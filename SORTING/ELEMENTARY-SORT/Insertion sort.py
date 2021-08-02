import random
import time

def insertion_sort(li):
    for i in range(1, len(li)):
        j = i -1
        tmp = li[i]
        while li[j] > tmp and j >= 0:
            li[j + 1] = li[j]
            j -= 1
        li[j + 1] = tmp


li = [random.randint(0, 10000) for i in range(1000)]
print(li)
start = time.time()
insertion_sort(li)
print(li)
end = time.time()
print(end - start)
