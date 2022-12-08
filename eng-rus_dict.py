words={}

while True:
	s = input("Введите слово по-английски: ")
	if s in words:
		print("Слово", s, "переводится как", words[s])
	else:
		print("Введите перевод слова ", s)
		words[s] = input()
