def selection_sort(arr):
	for i in range(len(arr)):
		for j in range(i + 1, len(arr)):
			if arr[i] > arr[j]:
				(arr[i], arr[j]) = (arr[j], arr[i])
	return arr			

if __name__ == '__main__':
    num_array = []
    num = input("How many elements you want in array: ")
    for i in range(int(num)):
        n = int(input("num: "))
        num_array.append(n)
    print(selection_sort(num_array))