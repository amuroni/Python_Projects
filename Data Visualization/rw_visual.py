import matplotlib.pyplot as plt
from random_walk import RandomWalk

rw = RandomWalk(100000)
rw.fill_walk()
plt.scatter(0, 0, c="blue", s=100)
plt.scatter(rw.x_values, rw.y_values, c="green", edgecolors="none", s=1)
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)
plt.show()
