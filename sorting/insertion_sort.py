def insertion_sort(arr):
    for i in range(len(arr)):
        key = arr[i]
        j = i - 1
        while j >=0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key 
    return arr    


if __name__ == '__main__':
    num_array = []
    num = input("How many elements you want in array: ")
    for i in range(int(num)):
        n = int(input("num: "))
        num_array.append(n)
    print(insertion_sort(num_array))