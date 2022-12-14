import json, random, string

###################################################
# открывает json файл из директории file_before
# по ключу key_for_change 
# заменяет значение на рандомные
# сохраняет результат в файл file_after 
##################################################

file_before = 'file.json'
#file_before = input("Введите имя/путь файла: ")

key_for_change = 'id'
#key_for_change = input("Введите ключ: ")


# ------ OPEN 2 FILES ----------

# open json-file
file_before_pointer = open(file_before, mode='r', encoding='utf_8')

# save in file
file_after = 'file_after.json'
file_after_pointer = open(file_after, mode='w', encoding='utf_8')

# -----------------------------

# json to dict
json_data = json.load(file_before_pointer)

# get keys
keys = json_data[1].keys()


# ----- random values  -----

# random int
rand_from = 0 # от
rand_to = 255 # до

# random str
size = 5
generate_str = ''.join([random.choice(
                        string.ascii_uppercase + string.digits + string.punctuation)
                        for n in range(size)])
# ------------------------------

if key_for_change in keys:
	
	# change value
	for user in json_data:
		user[key_for_change] = random.randint(rand_from,rand_to)
		# user[key_for_change] = generate_str

	# dict to json
	json.dump(json_data, file_after_pointer, ensure_ascii=False)
	
	print("\nЗначения заменены!!")
	print(f"Результат сохранен в файле: {file_after}")

else:
        choice = input("Такого ключа нет.")

# ------ CLOSE 2 FILES ---------
file_after_pointer.close()
file_before_pointer.close()
# ------------------------------

