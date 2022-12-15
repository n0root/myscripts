import json, string, re

###################################################
# открывает json файл из директории file_before
# по ключу key_for_change 
# выводит значения в файл output_file
# изменяем значение по регулярнеым функциям 
##################################################

file_before = 'data.json'
#file_before = input("Введите имя/путь файла: ")

#key_for_change = 'phone'
key_for_change = 'currency'
#key_for_change = input("Введите ключ: ")


# ------ OPEN 2 FILES ----------

# open json-file
file_before_pointer = open(file_before, mode='r', encoding='utf_8')

# save in file
output_file = 'output.txt'
output_file_pointer = open(output_file, mode='w', encoding='utf_8')

# -----------------------------

# ------ поиск в подстроке ----

# найти телефоны начинающиеся со скобок:
# (366) 302-8054

phone_mask = r"\(\d\d\d\) \d+\-\d+"

# найти currency (до точки)
# $29

currency_mask = r"\$\d+"

# -----------------------------


# json to dict
json_data = json.load(file_before_pointer)

# get keys
keys = json_data[1].keys()

if key_for_change in keys:
	
	# change value
	for user in json_data:
		
		#output without mask
		#print(user[key_for_change])

		# change value
		#lines = re.findall(currency_mask, user[key_for_change])
		#non_empty_lines = (line + '\n' for line in lines if not line.isspace())
		
		# save in file
		output_file_pointer.write(user[key_for_change] + '\n')		

		# save in file with mask
		#output_file_pointer.writelines(non_empty_lines)
                
else:
        choice = input("Такого ключа нет.")

# ------ CLOSE 2 FILES ---------
file_before_pointer.close()
output_file_pointer.close()
# ------------------------------

