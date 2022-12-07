#################################
# нумерация всех строк файла
# и поиск по слову word
# расположенного по пути path
################################

path = "/home/user/test/test.txt"
word = "русский"


with open(path, mode='r', encoding='mac_cyrillic') as my_file:
	for number, line in enumerate(my_file):
		if word in line:
			print(str(number) + '\t' + line.strip())
