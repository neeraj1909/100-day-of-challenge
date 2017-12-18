def binary_search(arr, start, end, item):
    mid = (start + end) // 2 
    if start <= end:
        if item == arr[mid]:
            return True
        elif item < arr[mid]:
            return binary_search(arr, start, mid - 1, item)
        else:
            return binary_search(arr, mid + 1, end, item)
    return False


if __name__ == '__main__':
    num_array = []
    num = input("How many elements you want in array: ")
    for i in range(int(num)):
        n = input("num: ")
        num_array.append(n)
    x = int(input("Enter the element you want to search in the array: "))

    if binary_search(num_array, 0, len(num_array) - 1, x):
        print("Element %s is present in the given array" % x)
    else:
        print("Element %s is not present in the given array" % x)