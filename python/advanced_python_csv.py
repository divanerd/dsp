import csv
from collections import Counter
import re

#write emails files to csv
with open('faculty.csv') as csv_file:
	reader = csv.DictReader(csv_file)
	with open('faculty_emails.csv', 'w') as f:
		for row in reader:
			f.write(row['email'])
			f.write('\n')
			print(row['email'])
		f.close
