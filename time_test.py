import datetime
import time
import threading
from urllib.request import urlopen
import ssl
import json
#---------- Import files ------------
import suncalc

# This restores the same behavior as before.
context = ssl._create_unverified_context()

#Check Today's date
today =  datetime.date.today() #datetime.date(2017, 2, 24)
# sunset_api_url = 'https://api.sunrise-sunset.org/json?lat=47.4979&lng=19.0402&date=today'

#Getting Sunset and Sunrise y geographical location
location_lat = 47.4979
location_long = 19.0402
sunTime = suncalc.getTimes(today + datetime.timedelta(days=1), location_lat, location_long)
sunRIseTime = suncalc.getSunrise(today + datetime.timedelta(days=1), location_lat, location_long)
print('Mit kap a progi?:' + str(today))
print('Mikor kel fel a nap?:' + str(sunRIseTime))

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
	threading.Timer(5.0, printit).start() #Checkin the dates every x second
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

	def checkSunStatus():
		sunrise_time = time.strptime(str(sunTime['sunrise']), '%Y-%m-%d %H:%M:%S')
		sunset_time = time.strptime(str(sunTime['night']), '%Y-%m-%d %H:%M:%S')
		current_time = time.strptime(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()),'%Y-%m-%d %H:%M:%S')
	
		print('The sun will rise at: ' + time.strftime('%Y-%m-%d %H:%M:%S',sunrise_time))
		print('The sun will set at: ' + time.strftime('%Y-%m-%d %H:%M:%S',sunset_time))
		print('Currently it is: ' + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
	
		if sunrise_time <= current_time <= sunset_time:
			print("It's daylight")
		else:
			print("It's night time")

	checkSunStatus()

	
	print('Ez most műkszik?: ' + str(sunTime))
printit()
#------------ End Checking if There is a Certain Special Day ------------

