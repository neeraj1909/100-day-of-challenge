def heapify(arr, n, i):
    l = 2*i + 1
    r = 2*i + 2
    largest = i

    if l < n and arr[l] > arr[i]:
        largest = l

    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        heapify(arr, n, largest)


def heapsort(arr):
    n = len(arr)

    #build a max-heap
    for i in range(n // 2, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements    
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

if __name__ == '__main__':
    arr = [ 12, 11, 13, 5, 6, 7]
    heapsort(arr)
    print ("Sorted array is")
    for i in range(len(arr)):
        print ("%d" %arr[i]),