def binary_search(my_list,item):
	low=0
	high=len(my_list)-1

	while low<=high:
		mid=(low+high)//2
		guess=my_list[mid]

		if guess==item:
			return mid
		if guess>item:
			high=mid-1
		else:
			low=mid+1

	return None

list1=[1,2,44,55,74,95,102]

print(binary_search(list1,44))


a=5//2
print(a)