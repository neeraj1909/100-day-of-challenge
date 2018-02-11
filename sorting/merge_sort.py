def merge_sort(arr, low, high):
	if (low < high):
		mid = (low + high - 1) // 2
		merge_sort(arr, low, mid)
		merge_sort(arr, mid + 1, high)
		merge(arr, low, mid, high)
	return arr	

def merge(arr, low, mid, high):
	h = low
	i = low
	j = mid + 1
	b = []
	while h <= mid and j <= high:
		if arr[h] < arr[j]:
			b[i] = arr[h]
			h = h + 1
		else:
		    b[i] = arr[j]
		    j = j + 1
		i = i + 1 

	if h > mid:
		for i in range(j, high + 1):
			b[i] = arr[i]
	else:
		for i in range(h, mid + 1):
			b[i] = arr[i]

	for i in range(low, high + 1):
		arr[i] = b[i]
	return arr
	

if __name__ == '__main__':
    num_array = []
    num = input("How many elements you want in array: ")
    for i in range(int(num)):
        n = int(input("num: "))
        num_array.append(n)
    print(merge_sort(num_array, 0, len(num_array)))		