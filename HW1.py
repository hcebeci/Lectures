n = [100,1000,10000,100000,1000000]
import random
import timeit
def uns_iterative1(n):
    time = []
    for i in range(10):
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
                time = time + stop - start
            index += 1
        stop = timeit.default_timer()
        time = time + stop - start
    return time/10
avr_time_uns_iterative1 = sum(uns_iterative1(100) for i in range(10)) / 10

time5 = []
for sayi in range(n):
    for i in range(10):
        def var_generator(n):
            list = []
            rint = []
            rint.append(random.randint(0,n-1))
            for i in range(n):
                list.append(random.randint(10,n*10))
            return sorted(list), rint

        temp = var_generator(n[sayi])
        arr = temp[0]
        x = temp[1]
        
        start = timeit.default_timer()
        def s_iterative_binary(n):
            low = 0
            high = len(arr) - 1
            mid = 0
            while low <= high:
                mid = (high + low) // 2
                if arr[mid] < x[0]:
                    low = mid + 1
                elif arr[mid] > x[0]:
                    high = mid - 1
                else:
                    mid
            return -1
        stop = timeit.default_timer()
        time5[n] = time5[n] + (stop - start)/10

time6 = []
for sayi in range(n):
    for i in range(10):
        def var_generator(n): ### fonksiyonu tanimlamisim ama aslinda fonksiyonu calistirmam lazim. parantez icine gelen sayiyla
            list = []
            rint = []
            rint.append(random.randint(0,n-1))
            for i in range(n):
                list.append(random.randint(10,n*10))
            return sorted(list), rint

        temp = var_generator(n[sayi])
        arr = temp[0]
        x = temp[1]
        
        start = timeit.default_timer()
        def binary_search_recursive(arr,x):
            if len(arr) == 0:
                return -1;

            midindex = len(arr) // 2
            if (arr[midindex] == x):
                return midindex
            elif arr[midindex] > x:
                return binary_search_recursive(arr[:midindex], x)
            else: #arr[midindex] < x:
                retindex = binary_search_recursive(arr[midindex + 1:], x)
                if retindex == -1:
                    return -1
                else:
                    return midindex + 1 + retindex  
        stop = timeit.default_timer()
        time6[n] = time6[n] + (stop - start)/10
    

        
