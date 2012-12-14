to_sort = [10,20,1]
low = 0
high = len(to_sort)

def mergesort(low,high):
	if (high-low) <= 1:
		return 
	split = (low+high) / 2
	mergesort(low,split)
	mergesort(split,high)
	scratch = []
	scratch.extend(to_sort[low:split]) #Python reads from low to split-1
	m1 = 0
	m2 = split
	i = low
	while i < m2 and m2 < high:
		if scratch[m1] <= to_sort[m2]:
			to_sort[i] = scratch[m1]
			i += 1
			m1 += 1
		else:
			to_sort[i] = to_sort[m2]
			i += 1
			m2 += 1
	while i<m2:
		to_sort[i] = scratch[m1]	
		i += 1
		m1 += 1

if __name__ == '__main__':
	print "Unsorted Input array: %s" % str(to_sort)
	mergesort(low,high)
	print "Sorted Output array: %s" % str(to_sort)

	

