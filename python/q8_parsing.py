# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.


import csv
with open ('football.csv') as csv_file:
	reader = csv.DictReader(csv_file)
	team_diffs = {}
	for row in reader:
		team_diffs[row['Team']] = abs(int(row['Goals']) - int(row['Goals Allowed']))
		#print (row['Team'], row['Goals'], row['Goals Allowed'])
	return min_diff = min(team_diffs.items(), key=lambda k: k[1])
	# print (min_diff)

#answer: ('Aston_Villa', 1)
