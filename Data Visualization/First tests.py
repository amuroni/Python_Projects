import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]  # define input values as x axis values
squares = [1, 4, 9, 16, 25]  # dataset as y axis values

#plt.plot(input_values, squares, linewidth=5)  # plot the x,y data in a chart + line thickness
plt.scatter(2, 4, s=290)  # plot a single point in the chart + size of the dot

# set chart title and label axes
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=11)
plt.ylabel("Square of Value", fontsize=11)

# set size of ticks for labels
plt.tick_params(axis="both", which="major", labelsize=11)

plt.show()  # shows the data

"******************"

x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

plt.scatter(x_values, y_values, s=150)
plt.show()  # shows only single points in the chart, scattered
