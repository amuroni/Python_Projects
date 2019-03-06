from random import choice


class RandomWalk:
    def __init__(self, num_points=5000):
        self.num_points = num_points
        self.x_values = [0]  # starting x value
        self.y_values = [0]  # starting y value

    def fill_walk(self):
        while len(self.x_values) < self.num_points:
            x_direction = choice([1, -1])  # decide x direction ( 1 = right, -1 = left)
            x_distance = choice([0, 1, 2, 3, 4])  # and distance
            x_step = x_direction * x_distance  # length of y step
            y_direction = choice([1, -1])  # same for y, direction
            y_distance = choice([0, 1, 2, 3, 4])  # and distance
            y_step = y_direction * y_distance  # length of y step
            if x_step == 0 and y_step == 0:
                continue
            next_x = self.x_values[-1] + x_step  # next x value
            next_y = self.y_values[-1] + y_step  # next y value
            self.x_values.append(next_x)
            self.y_values.append(next_y)
