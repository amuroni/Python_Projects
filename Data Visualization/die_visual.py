from die import Die
import pygal
import random
import webbrowser


# two D6 dice
die_1 = Die(random.randint(6, 20))
die_2 = Die(random.randint(6, 20))

# analyze results
results = []
roll = random.randint(10000, 1000000)
for roll_num in range(roll):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# analyze frequency
frequencies = []
max_result = die_1.num_sides + die_2.num_sides  # largest possible result = num_sides of each Die

for value in range(2, max_result+1):  # works for any number of dice face
    frequency = results.count(value)
    frequencies.append(frequency)

# visualize results
hist = pygal.Bar()  # define a bar chart with pygal
labels = []
faces = die_1.num_sides + die_2.num_sides
for face in range(2, faces+1):
    labels.append(face)
hist.title = "Results of rolling two dices with " + str(faces) + " faces for " + str(roll) + " times."
hist.x_labels = labels
hist.x_title = "Result"
hist.y_title = "Frequency"
hist.add("D" + str(die_1.num_sides) + " & D" + str(die_2.num_sides), frequencies)  # calling directly num_sides
hist.render_to_file('die_visual.svg')  # render to svg file

# automatically open the svg with the default windows browser - in my case firefox
svg = "C:\\Users\\muron\\IdeaProjects\\Python_Projects\\Data Visualization\\die_visual.svg"
browser = webbrowser.get("Windows-default")
browser.open(svg)
