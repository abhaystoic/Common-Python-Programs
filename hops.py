def main():
	arr = [2, 0, 1, 0]
	new_arr = arr
	while len(new_arr) > 0:
		hops = new_arr[0]
		if hops == 0 and len(new_arr) > 1:
			print 'unreachable'
			break
		elif new_arr == [0]:
			print 'reachable'
			break
		new_arr = new_arr[hops:]


if __name__ == '__main__':
	main()