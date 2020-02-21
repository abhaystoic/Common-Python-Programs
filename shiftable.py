def shift():
	text1 = 'abcde'
	text2 = 'cdeab'

	for i in xrange(len(text1)):
		text1 = text1[1::] + text1[0]
		if text1 == text2:
			return True
	return False


if __name__ == '__main__':
	if shift():
		print 'Shiftable'
	else:
		print 'Un-Shiftable'
