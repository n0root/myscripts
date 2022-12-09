import json

###################################################
# открывает json файл из директории file_before
# по ключу key_for_change заменяет значения 
# на те что в файле file_with_new_values
# сохраняет результат в файл file_after 
##################################################

#file_before = 'file.json'
file_before = input("Введите json файл: ")

#file_with_new_values = 'values.txt'
file_with_new_values = input("Введите txt файл: ")

#key_for_change = 'id'
key_for_change = input("Введите ключ: ")

# ------ OPEN 3 FILES ---------
# open file1 for change
file_before_pointer = open(file_before, mode='r', encoding='utf_8')

# open file2 with values for change
file_with_new_values_pointer = open(file_with_new_values, mode='r', encoding='utf_8')

# save in file3
file_after = 'file_after.json'
file_after_pointer = open(file_after, mode='w', encoding='utf_8')
# ------------------------------

# json to dict
json_data = json.load(file_before_pointer)

list1 = [] # for json
list2 = [] # for txt

# in list2 add lines from txt file
for line in file_with_new_values_pointer:
	list2.append(line.strip())

keys = json_data[1].keys()

if key_for_change in keys:
        if len(list2) == len(json_data):

                # in list1 add keys from json
                i=0
                while i < len(json_data):
                        list1.append(json_data[i][key_for_change])
                        i+=1

                for index, item in enumerate(list1):
                        list1[index] = list2[index]
		# change
                for index, user in enumerate(json_data):
                        user[key_for_change] = list1[index]
                
                # dict to json
                json.dump(json_data, file_after_pointer, ensure_ascii=False)

                print("\nУспешно заменено!")
                print(f"Результат сохранен в файле: {file_after}.")
        else:
                print("Количество ключей и новых значений не равны.")
                print("Присваивание не выполнено.")
else:
	print("Такого ключа нет")

# ------ CLOSE 3 FILES ---------
file_after_pointer.close()
file_before_pointer.close()
file_with_new_values_pointer.close()
# ------------------------------

