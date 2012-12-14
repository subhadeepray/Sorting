to_sort = [10,20,11,1,1,1,1,4,5,6,1,99,10,34,4,4,4,8,100]
maxval = 100

def countingsort(to_sort,maxval):
	output = [0] * len(to_sort)
	count = [0] * (maxval+1)
	for j in range(0,len(to_sort)):
		count[to_sort[j]] += 1
	for i in range(1,maxval+1):
		count[i] = count[i] + count[i-1]
	for j in range(len(to_sort)-1,-1,-1):
		output[count[to_sort[j]]-1] = to_sort[j]
		count[to_sort[j]] = count[to_sort[j]] - 1
	print "Sorted Output array: %s" % str(output)

if __name__ == '__main__':
	print "Unsorted Input array: %s" % str(to_sort)
	countingsort(to_sort,100)

