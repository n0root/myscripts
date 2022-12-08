#####################################
# нумерация всех строк файла
# и поиск по слову word
# расположенного по пути path
# и вывод количества повторений word
######################################

path = "/home/user/myscripts/test.txt"
word = input("Введите слово для поиска: ")
n=0
print("\n")

with open(path, mode='r', encoding='mac_cyrillic') as my_file:
	for number, line in enumerate(my_file):
		if word in line:
			print(f"{str(number)}\t{line.strip()}")
			n+=1
	

	print(f"\n\nСловo \"{word}\" встречалось в файле {n} раз.")
	
