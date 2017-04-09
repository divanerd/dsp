import csv
from collections import Counter
import re
import itertools
import numpy

#print (row['name'], row['degree'], row['title'], row['email'])

#get emails
with open('faculty.csv') as csv_file:
	reader = csv.DictReader(csv_file)
	res = []
	for row in reader:
		res.append(row['email'])
	print (res)


#get titles and counts
with open('faculty.csv') as csv_file:
	reader = csv.DictReader(csv_file)
	res = []
	for row in reader:
		j = re.sub('is', 'of', row['title'])
		res.append(j)
	counts = Counter(res)
	print(counts)



#get distinct email 
with open('faculty.csv') as csv_file:
	reader = csv.DictReader(csv_file)
	regex = '@(\w*.){0,2}\w*.\w*'
	res=[]
	for row in reader:
		res.append(re.compile(regex, 0).search(row['email']).group())
	uniques = numpy.unique(res)
	print(uniques)

	



#get degrees and counts
#strip away period
#get all degrees in cases where more than one
with open('faculty.csv') as csv_file:
	reader = csv.DictReader(csv_file)
	degrees = []
	clean_list = []
	for row in reader:
		if ' ' in row['degree']:
			i = (row['degree'].split())
			#i.tolist()
			degrees.append(i)
			for i in degrees:
				for j in i:
					j = re.sub('[.]', '', j)
					if j not in clean_list:
						clean_list.append(j)
					else:
						pass

	count_unique_degrees = Counter(clean_list)
	
print(count_unique_degrees)
		

##review pandas and python data structures
