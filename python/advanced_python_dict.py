import csv
from collections import Counter
import re
import itertools


#6
with open('faculty.csv') as csv_file:
	reader = csv.DictReader(csv_file)
 	faculty_dict = {}
 	for row in reader:
 		faculty_dict[row['name'].rsplit(None, 1) [-1]] = [str(row['degree']), str(row['title']), str(row['email'])]
# print(faculty_dict)

top_three = dict(itertools.islice(faculty_dict.items(), 3))
print(top_three)


#7/8
with open('faculty.csv') as csv_file:
	reader = csv.DictReader(csv_file)
	faculty_dict = {}
	for row in reader:
		faculty_dict[row['name'].rsplit(None, 1) [-1], row['name'].rsplit(None, 1) [0] ] = [str(row['degree']), str(row['title']), str(row['email'])]

top_three = dict(itertools.islice(faculty_dict.items(), 3))
print(top_three)

