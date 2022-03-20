n = [1000,10000,100000,1000000, 10000000]
'''
import random
set = {}
rint = {}

for k in range(len(n)):
    temp = []
    for j in range(10):
        temp.append(random.randint(0,n[k]-1))
    rint[x] = temp

for x in range(len(n)):
    for i in range(1,11):
        list = []
        for l in range(n[x]):
            list.append(random.randint(10,n[x]*10))
        set[(x*10)+i] = list

sorted_set = {}
for x in range(len(set)):
    sorted_set[x] = sorted(set[x])
'''
import random
import timeit
def var_generator(n):
    list = []
    rint = []
    rint.append(random.randint(0,n-1))
    for i in range(n):
        list.append(random.randint(10,n*10))
    return list, rint

def uns_iterative1(n):
    start = timeit.default_timer()
    def var_generator(n):
        list = []
        rint = []
        rint.append(random.randint(0,n-1))
        for i in range(n):
            list.append(random.randint(10,n*10))
        return list, rint
    temp = (var_generator(n))
    arr = temp[0]
    x = temp[1]
    index = 0
    for y in arr:
        if y == x:
            stop = timeit.default_timer()
            return (stop - start)
        index += 1
    stop = timeit.default_timer()
    return (stop - start);
avr_time_uns_iterative1 = sum(uns_iterative1(100) for i in range(10)) / 10

def s_iterative_binary(n):
    start = timeit.default_timer()
    def var_generator(n):
        list = []
        rint = []
        rint.append(random.randint(0,n-1))
        for i in range(n):
            list.append(random.randint(10,n*10))
        return list, rint
    temp = (var_generator(n))
    arr = temp[0]
    x = temp[1]    
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

print(s_iterative_binary(100))


def s_recursive_binary(arr,x):
