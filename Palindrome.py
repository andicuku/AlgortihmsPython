sentence = input("Enter sentence \n").lower()


def palindromic(sentence):
	sentence = (''.join(filter(str.isalnum, sentence)))
	if len(sentence) <= 1:
		return True
	while (len(sentence) > 1):
		if sentence[0]==sentence[-1]:
			sentence = sentence[1:-1]
		else:
			return False
	return True




if palindromic(sentence)==True:
	print(True)
else:
	print(False)