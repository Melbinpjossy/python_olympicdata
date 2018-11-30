import csv
import matplotlib.pyplot as plt

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
			russia.append([int(row[0]), row[5], row[6], row[7]])
		else:
			world.append([int(row[0]), row[5], row[6], row[7]])
		line_count += 1

print('total medals for RUS:', len(russia))
print('total medals for everyone else:', len(world))

print('processed', line_count, 'rows of data')

gold_2002 = []
gold_2014 = []

for medal in russia:
	if medal[0] == 2006 and medal[3] == "Gold":
		gold_2002.append(medal)

	
	if medal[0] == 2014 and medal[3] == "Gold":
		gold_2014.append(medal)

print('Number of gold medals in 2006 = ', len(gold_2002))
print('Number of gold medals in 2014 = ', len(gold_2014))

total = len(gold_2002) + len(gold_2014)
# percent
rustf_percentage = int(len(gold_2002) / total * 100)
rust_percentage = int(len(gold_2014) / total * 100)

print(rustf_percentage, rust_percentage)

label = "2002", "2014"
sizes = [rustf_percentage, rust_percentage]
colors = ['yellowgreen', 'lightcoral']
explode = (0.1, 0.1)

plt.pie(sizes, explode=explode, colors=colors, autopct='%1.1f%%' ,shadow=True, startangle=140)
plt.axis('equal')

plt.legend(label, loc=1)
plt.title("Medal Wins - Historic Medals Counts")
plt.xlabel("Russian gold medals in 2002 and 2014 ratio")
plt.show()

print('Russia won', len(gold_2002), 'gold medals in 2002')
print('Russia won', len(gold_2014), 'gold medals in 2014')

