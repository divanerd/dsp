import csv
from collections import Counter
import re

#write emails files to csv
with open('faculty.csv') as csv_file:
	reader = csv.DictReader(csv_file)
	regex = re.compile(r'''@\(\w*.\){0,2}\w*.\w*\)''')
	#regex = re.compile()
	res=[]
	with open('faculty_emails.csv', 'w') as f:
		for row in reader:
			f.write(row['email'])
			f.write('\n')
			print(row['email'])
		f.close
