import datetime
import time
import threading
from urllib.request import urlopen
import ssl
import json

# This restores the same behavior as before.
context = ssl._create_unverified_context()

#Check Today's date
today = datetime.date(2017, 2, 24) #datetime.date.today()
sunset_api_url = 'https://api.sunrise-sunset.org/json?lat=36.7201600&lng=-4.4203400&date=today'

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
#printit()
#------------ End Checking if There is a Certain Special Day ------------

def load_api():
	response = urlopen(sunset_api_url, context=context).read().decode('utf8')
	obj = json.loads(response)
	success = True
	sunrise_time = time.strptime(str(obj['results']['sunrise']), '%I:%M:%S %p')
	sunset_time = time.strptime(str(obj['results']['sunset']), '%I:%M:%S %p')
	current_time = time.strptime(time.strftime('%I:%M:%S %p',time.localtime()),'%I:%M:%S %p')
	
	print('The sun will rise at: ' + time.strftime('%I:%M:%S %p',sunrise_time))
	print('The sun will set at: ' + time.strftime('%I:%M:%S %p',sunset_time))
	print('Currently it is: ' + time.strftime('%I:%M:%S %p',time.localtime()))
	
	if sunrise_time <= current_time <= sunset_time:
		print("It's daylight")
	else:
		print("It's night time")

load_api()