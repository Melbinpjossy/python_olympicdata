import csv
import matplotlib.pyplot as plt 
import numpy as np


categories = []
russia = []
world = []

with open('data/OlympicsWinter.csv') as csvfile:
	reader = csv.reader(csvfile)
	line_count = 0

	for row in reader:
		if line_count is 0:
			categories.append(row)
			line_count += 1
		elif row[4] == "RUS":
			russia.append([int(row[0]), row[2], row[5], row[6], row[7]])
		else:
			world.append([int(row[0]), row[2], row[5], row[6], row[7]])
		line_count += 1

print('total medals for RUS:', len(russia))
print('total medals for everyone else:', len(world))

print('processed', line_count, 'rows of data')

Skiing = []
Skating = []

for medal in russia:
	if medal[1] == "Skiing":
		Skiing.append(medal)

	if medal[1] == "Skating":
		Skating.append(medal)

print('processed', line_count, 'rows of data')
print('Number of participates in Skiing = ', len(Skiing))
print('Number of participates in Skating = ', len(Skating))

e = len(Skiing)
w = len(Skating)

print('processed', line_count, 'rows of data')

x = np.arange(2)
medals = [e,w]

fig, ax = plt.subplots()
plt.bar(x, medals)
plt.xticks(x, ('Skiing', 'Skating'))
plt.title("Skating and Skiing Medal ratio")

plt.show()


