# Hint:  use Google to find python function

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'   

####b)  
date_start = '12312013'  
date_stop = '05282015'  

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  


import datetime
import dateutil.parser

def diff_dates(date1, date2):
	#mdate1 = datetime.datetime.strptime(date1, "%m-%d-%Y").date()
	#rdate1 = datetime.datetime.strptime(date2, "%m-%d-%Y").date()
	mdate1 = dateutil.parser.parse(date1)
	mdate2 = dateutil.parser.parse(date2)
	delta =  abs((mdate1 - mdate2).days)
	print(delta)

diff_dates('01-02-2013', '07-28-2015')
diff_dates('15-Jan-1994', '14-Jul-2015')


def date_diffs_s(date1, date2):
	date_format = "%m%d%Y"
	mdate1 = datetime.datetime.strptime(date1, "%m%d%Y")
	mdate2 = datetime.datetime.strptime(date2, "%m%d%Y")
	delta =  abs((mdate1 - mdate2).days)
	print (delta)

date_diffs_s('12312013', '05282015')
