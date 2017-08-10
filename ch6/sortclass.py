# How to implement sorting logic for a list that
# must sort a class in python.

class WeirdSortee:
    def __init__(self, string, number, sort_num):
        '''Inits around a string key, a number value, and whether or not it sorts
        based on the number.'''
        self.string = string
        self.number = number
        self.sort_num = sort_num

    def __lt__(self, object):
        'determines the behavior when we use the < operator wth this object.'
        if self.sort_num:
            return self.number < object.number
        return self.string < object.string

    def __repr__(self):
        'Determines how object is represented. Alternative to printing location'
        return f'{self.string}:{self.number}'
