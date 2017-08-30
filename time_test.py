import datetime
import threading

#Check Today's date
today = datetime.date(2017, 2, 24) #datetime.date.today()


#-------------- Start Special Dates --------------

#Christmas dates
christmas_start = datetime.date(today.year, 12, 15)
christmas_end = datetime.date(today.year, 12, 30)

#St Istvan dates
st_istvan_day = datetime.date(today.year, 8, 20)

#Adri's Nameday
adri_nameday = datetime.date(today.year, 9, 8)

#Farkas Birthday
farkas_birthday = datetime.date(today.year, 9, 29)

#Farkas Nameday
farkas_nameday = datetime.date(today.year, 10, 31)

#Adri's Birth day
adri_birthday = datetime.date(today.year, 2, 24)

#-------------- End Special Dates --------------


#------------ Start Checking if There is a Certain Special Day ------------
def printit():
	threading.Timer(1.0, printit).start() #Checkin the dates every x second
	if christmas_start <= today <= christmas_end:
		print('Yeah! Its Christmas!')
	elif st_istvan_day == today:
		print ('It is St Istvan day! Happy Birthday Hungary!')
	elif adri_nameday == today:
		print ('It is Adri"s name day! Happy name day!')
	elif farkas_nameday == today:
		print ('It is Farkas name day! Happy name day!')
	elif adri_birthday == today:
		print ("It is Adri's Birth day! Happy Birth day Adri!")
	elif farkas_birthday == today:
		print ('It is Farkas Birth day! Happy Birth day Farkas!')
	else:
		print('Its not a special day :(')
printit()
#------------ End Checking if There is a Certain Special Day ------------