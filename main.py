from datetime import datetime

year = input("Enter Year\n")
#must be between 1900 - 2020
yeari, yearv = None, None
try:
	yeari = int(year)
except:
	pass
if yeari is not None:

	if yeari < 1900:
		print("Year must be greater than 1900")
	elif yeari > 2020:
		print("Year must be lesser than 2020")
		#print("Valid Year")
	else:
		yearv = 1
		print("A Valid Year")
else:
	print("Year "+year+" is invalid")

month = input("Enter Month\n")
#must be between 01 - 12
monthi, monthv = None, None
try:
	monthi = int(month)
except:
	pass
if monthi is not None:

	if monthi < 1:
		print("Month must be greater than 01")
	elif monthi > 12:
		print("Month must be lesser than 12")
	else:
		monthv = 1
		print("A Valid Month")
else:
	print("Month "+month+" is invalid")

date = input("Enter Date\n")
#must be between 01 - 31
datei, datev = None, None
try:
	datei = int(date)
except:
	pass
if datei is not None:

	if datei < 1:
		print("Date must be greater than 01")
	elif datei == 31:
		if monthi == 2:
			if(yeari % 4 == 0):
				print("Leap year will have only 29 days")
			else:
				print("Non Leap year will have only 28 days")
		elif monthi == 4 or monthi == 6 or monthi == 9 or monthi == 11:
			print("Date must be lesser than 31 as per calendar")
		else:
			datev = 1
			print("A Valid Date")
	elif datei > 31 :
		print("Date must be lesser than 31")
	else:
		datev = 1
		print("A Valid Date")
else:
	print("Date "+date+" is invalid")

#Time section starts here
hour = input("Enter Hour\n")
#must be between 01 - 24
houri, hourv = None, None
try:
	houri = int(hour)
except:
	pass
if houri is not None:

	if houri < 1:
		print("Hour must be greater than 01")
	elif houri > 24:
		print("Hour must be lesser than 24")
	else:
		hourv = 1
		print("A Valid Hour")
else:
	print("Hour "+hour+" is invalid")

minutes = input("Enter Minutes\n")
#must be between 01 - 60
minutesi, minutesv = None, None
try:
	minutesi = int(minutes)
except:
	pass
if minutesi is not None:

	if minutesi < 1:
		print("Minute must be greater than 01")
	elif minutesi > 60:
		print("Minute must be lesser than 60")
	else:
		minutesv = 1
		print("A Valid Minute")
else:
	print("Minute "+minutes+" is invalid")

seconds = input("Enter Seconds\n")
#must be between 01 - 60
secondsi, secondsv = None, None
try:
	secondsi = int(seconds)
except:
	pass
if secondsi is not None:

	if secondsi < 1:
		print("Seconds must be greater than 01")
	elif secondsi > 60:
		print("Seconds must be lesser than 60")
	else:
		secondsv = 1
		print("A Valid Second")
else:
	print("Second "+seconds+" is invalid")

if(yearv == 1 and monthv ==1 and datev == 1 and hourv ==1 and minutesv ==1 and secondsv ==1):
    timestamp = datetime(yeari, monthi, datei, houri, minutesi, secondsi)
    print("Timestamp from User is ", timestamp)
else:
    print("Entered Datetime details are invalid...")