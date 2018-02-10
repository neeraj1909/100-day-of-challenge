from math import sqrt

def jump_search(arr, x, n):
    #arr is a array of elements
    #x is the element to be searched and n is total no.of elements in the array

    step = sqrt(n) #comparison will be minimum when n = m**2
    
    prev = 0
    
    #for finding the block
    while arr[int(min(step,n))-1] < x:
        prev = step
        step = step + sqrt(n)
        if prev > n:
            return -1

    #for finding the element
    while arr[int(prev)] < x:
        prev = prev + 1

        if prev == min(step, n):
            return -1

    if arr[int(prev)] == x:
        return prev
    return -1
  

if __name__ == '__main__':
    arr = [ 0, 1, 1, 2, 3, 5, 8, 13, 21,
       34, 55, 89, 144, 233, 377, 610 ]
    x = 55  
    index = jump_search(arr, x, len(arr))

    print("number, x is at index: %.0f" % index)