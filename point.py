import math

class Point:
    'A point in two-dimensional space'

    def __init__(self):
        self.x = 0
        self.y = 0

    def status(self):
        'Displays status of point.'
        print(self.x, self.y)

    def move(self, x, y):
        'Moves point for us.'
        self.x = x
        self.y = y

    def reset(self):
        'Resets point to zero'
        self.move(0, 0)

    def calculate_distance(self, other_point):
        'Calculates distance between this and another point'
        return math.sqrt(
                (self.x - other_point.x)**2 
                + (self.y - other_point.y)**2
                )

        
