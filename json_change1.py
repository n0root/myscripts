import json

###################################
# открывает json файл из директории file_before
# по ключу key_for_change 
# заменяет значение на new_value
# сохраняет результат в файл file_after 
###################################

#file_before = 'file.json'
file_before = input("Введите имя/путь файла: ")
key_for_change = input("Введите ключ: ")
new_value = input("Введите новое значение: ")

# open json-file
file_before_pointer = open(file_before, mode='r', encoding='utf_8')

# change value
json_data = json.load(file_before_pointer)

for user in json_data:
        user[key_for_change] = new_value

# save in file
file_after = 'file_after.json'
file_after_pointer = open(file_after, mode='w', encoding='utf_8')

json.dump(json_data, file_after_pointer, ensure_ascii=False)
file_after_pointer.close()
file_before_pointer.close()


print("\nУспех!")
print(f"Результат сохранен в файле: {file_after}")
