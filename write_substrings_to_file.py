#################################
# запись подстрок substr
# файла inputfile
# в другой файл outputfile
################################

inputfile  = "/home/user/test/test.txt"
outputfile = "/home/user/test/result.txt" 
substr = "русский"


myfile1 = open(inputfile, mode='r', encoding='mac_cyrillic')
myfile2 = open(outputfile, mode='a', encoding='mac_cyrillic')

for number, line in enumerate(myfile1):
	if substr in line:
		print(str(number) + '\t' + line.strip())
		myfile2.write(line)

myfile1.close()
myfile2.close()
