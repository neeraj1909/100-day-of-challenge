def linear_search(arr, item):
	position = 0
	for i in range(len(arr)):
		if arr[i] == item:
			return True
	return False		

    
if __name__ == '__main__':
    num_array = []
    num = input("How many elements you want in array: ")
    for i in range(int(num)):
    	n = input("num: ")
    	num_array.append(n)
    x = int(input("Enter the element you want to search in the array: "))

    if linear_search(num_array, x):
    	print("Element %s is present in the given array" % x)
    else:
        print("Element %s is not present in the given array" % x)	