import optparse
to_sort = [-1,-2,-4,10,22,0,11,13]

def bubble(to_sort):
	for i in range(len(to_sort)-1,0,-1):
		for j in range(0,i):
			if to_sort[j] > to_sort[j+1]:
				to_sort[j] , to_sort [j+1] = to_sort[j+1] , to_sort[j]
	print "Sorted Output array: %s" % str(to_sort)

if __name__ == '__main__':
	print "Unsorted input array: %s" % str(to_sort)
	bubble(to_sort)


