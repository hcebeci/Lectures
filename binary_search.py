# Write a function to find out if an integer value exists in a given list of integers.
# The function is expected to return the index of the integer in the array if it exists. 
# Otherwise the function should return value -1;  

def search_iterative1(arr, x):
    index = 0
    for y in arr:
        if y == x:
            return index
        index += 1
    return -1;
    
def search_iterative2(arr, x):
    for index, y in enumerate(arr):
        if y == x:
            return index
    return -1;


# (n-1)! n -> n!
    
# if arr is sorted in nondecreasing order

def binary_search_iterative(arr, x):
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
   
def binary_search_recursive(arr, x):
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

def binary_search_recursive2(arr, x, low, high):
    if high < low:
        return -1;

    midindex = (high + low) // 2
    if (arr[midindex] == x):
        return midindex
    elif arr[midindex] > x:
        return binary_search_recursive2(arr, x, low, midindex - 1)
    else: #arr[midindex] < x:
        return binary_search_recursive2(arr, x, midindex + 1, high)

arr = [1,3,5,9]
print(binary_search_recursive(arr, 7)) #, binary_search_recursive2(arr, 7, 0, len(arr) - 1))
print(arr)