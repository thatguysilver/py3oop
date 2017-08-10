#The averagelist example in ch5.

class AverageList(list):
    'Gives us the average of the entire list using sum() and len()'
    @property
    def average(self):
        return sum(self) / len(self)
