import csv
import matplotlib.pyplot as plt 
import numpy as np


categories = []
russia =[]

with open('data/OlympicsWinter.csv') as csvfile:
	reader = csv.reader(csvfile)
	line_count = 0

	for row in reader:
		if line_count is 0:
			categories.append(row)
			line_count += 1
		elif row[4] == "RUS":
			russia.append([int(row[0]), row[5], row[6], row[7]])
		
gold_2002 = []
gold_2014 = []

for medal in russia:
	if medal[0] == 2002 and medal[3] == "Gold":
		gold_2002.append(medal)

	
	if medal[0] == 2014 and medal[3] == "Gold":
		gold_2014.append(medal)


l = len(gold_2002)
f = len(gold_2014)


print('Number of men in RUSSIA' , len(gold_2002))
print('Number of women in RUSSIA', len(gold_2014))



print('processed', line_count, 'rows of data')

x = np.arange(2)
medals = [l,f]

fig, ax = plt.subplots()
plt.bar(x, medals)
plt.xticks(x, ('2002','2014'))
plt.title("Russian gold medals in 2002 and 2014 ratio")

plt.show()


