import string, random


print("***Генератор надежного пароля***\n")

size = int(input('Количество символов: '))

generate_pass = ''.join([random.choice( 
                        string.ascii_uppercase + string.digits + string.punctuation) 
                        for n in range(size)]) 


print('\n', generate_pass, sep="")
