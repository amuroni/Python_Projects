from die import Die
import pygal

die = Die()

# analyze results
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)
# print(results)  # check if the Die class works

# analyze frequency
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)
# print(frequencies)  # analyze the frequency of each number rolled

# visualize the results
hist = pygal.Bar()  # define a bar chart
hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Result"
hist.y_title = "Frequency"
hist.add('D6', frequencies)  # add set of values to the chart
hist.render_to_file('die_visual.svg')  # render to svg file
