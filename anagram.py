def main():
	text = 'aaabxaxba'
	word = 'xba'
	rev_word = word[::-1]
	scan_window = len(word)
	text_len = len(text)

	aux_text = text
	# Check for the word
	for i in xrange(0, text_len - scan_window + 1):
		if aux_text[0:scan_window] == word:
			print i
		aux_text = aux_text[1:]

	# No need to check, if word and reverse of the word are the same.
	if word == rev_word:
		return
	aux_text = text
	# Check for the reverse word
	for i in xrange(0, text_len - scan_window + 1):
		if aux_text[0:scan_window] == rev_word:
			print i
		aux_text = aux_text[1:]


if __name__ == '__main__':
	main()