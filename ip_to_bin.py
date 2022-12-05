################################
# Перевод IP адреса
# в двоичное представление
################################

print("\n\t\t~~~ IP to BIN ~~~\n")

try:

	print("Введите ip адрес (например: 193.233.44.12)\n")
	a = input()
	list1 = []

	i=0
	while i<=3:
			part = a.split('.')[i]
			i = i + 1
			list1.append(part)

	list2 = [128,64,32,16,8,4,2,1]

	bin_list = []

	for item1 in list1:
	
		table = list2.copy()	
		for index,item2 in enumerate(table):
			if int(item1) - int(item2) >= 0:
			
				item1 = int(item1) - int(item2)
				table[index]=1
			else:
				table[index]=0

		bin_list.append(str(''.join((map(str, table)))))

	result = '.'.join(bin_list)	
	print(result)

except:
	print("Некорректный ввод")
