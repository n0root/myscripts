import datetime
from datetime import date


print('1. New Year calculation')
print('2. Calculate age\n')

choice = int(input('Enter the number (1-2) to start the program: '))

if choice == 1:

	# New Year
	today = datetime.date.today()
	future = datetime.date(today.year+1,1,1)
	diff = future - today

	if today == future:
		print (f"\n***Happy New Year!!!***")
	else:
		print (f"\n***There are {diff.days} days left before the New Year!***")


if choice == 2:

	#Age
	year = int(input('\nEnter year of birth: '))
	month = int(input('Enter month of birth: '))
	day = int(input('Enter day of birth: '))

	def age(birthdate):
	    today = date.today()
	    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day)) 
	    return age

	print(f'\nAge: {age(date(year,month,day))} years')


