'''
Shell sort is improved from insertion sort to minimize running time
'''
import random
import time

def shell_sort(li):
    N = len(li)
    gap = int(N / 3)
    while gap > 0:
        for i in range(gap, N):
            j = i
            tmp = li[i]
            while j - gap >= 0 and li[j] < li[j - gap]:
                li[j] = li[j - gap]
                j -= gap
            li[j] = tmp
        gap = int(gap / 3)



li = [random.randint(0, 10000) for i in range(1000)]
print(li)
start = time.time()
shell_sort(li)
print(li)
end = time.time()
print(end - start)