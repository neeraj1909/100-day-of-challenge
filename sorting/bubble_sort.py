def bubble_sort(arr):
	for i in range(len(arr)):
		for j in range(len(arr) - i - 1):
			if arr[j] > arr[j + 1]:
				(arr[j + 1], arr[j]) = (arr[j], arr[j + 1])
	return arr			

if __name__ == '__main__':
    num_array = []
    num = input("How many elements you want in array: ")
    for i in range(int(num)):
        n = int(input("num: "))
        num_array.append(n)
    print(bubble_sort(num_array))	