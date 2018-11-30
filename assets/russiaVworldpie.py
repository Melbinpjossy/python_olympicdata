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
			russia.append([int(row[0]), row[5], row[6], row[7]]) # multidimensional array
		else:
			world.append([int(row[0]), row[5], row[6], row[7]])
		line_count += 1

print('total medals for canada', len(russia))
print('total medals for everyone else', len(world))

print('processed', line_count, 'rows of data')


total = len(russia) + len(world)
russia_percentage = int(len(russia) / total * 100)
world_percentage = int(len(world) / total * 100)

print(russia_percentage, world_percentage)

label = "Russia" , "World"
sizes = [russia_percentage, world_percentage]
colors = ['yellow', 'green']
explode = (0.1, 0.1)

plt.pie(sizes, explode=explode, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')

plt.legend(label, loc=1)
plt.title("Medal Wins - Historical Medals Counts")
plt.xlabel("Russian World Medals")
plt.show()

print('Russia won', len(russia))
print("World won", len(world))
