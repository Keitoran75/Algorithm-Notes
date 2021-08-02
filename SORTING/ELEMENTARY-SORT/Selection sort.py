'''
* Find the smallest item in the array and exchange it with the first entry
* Find the next smallest item and exchange ut with second entry
'''

import random
import time
# version A
def selection_sort_simple(li):
    li_new = []
    for i in range(len(li)):
        min_val = min(li)
        li_new.append(min_val)
        li.remove(min_val)
    return li_new

# version B
def selection_sort(li):
    for i in range(len(li) - 1):
        min_loc = i
        for j in range(i + 1, len(li)):
            if  li[j] < li[min_loc]:
                min_loc = j
        li[i], li[min_loc] = li[min_loc], li[i]


# validation
li = [random.randint(0, 10000) for i in range(1000)]
print(li)
start = time.time()
li_new = selection_sort_simple(li)
print(li_new)
end = time.time()
print(end-start)