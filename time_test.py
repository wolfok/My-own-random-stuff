import datetime

today = datetime.date.today()
today_test = datetime.date(2017, 12, 17)
margin = datetime.timedelta(days = 3)

if datetime.date(today.year, 12, 15) <= today <= datetime.date(today.year, 12, 30):
	print('Yeah! Its Christmas!')
else:
	print('Its not Christmas :(')