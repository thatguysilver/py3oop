from collections import namedtuple

Stock = namedtuple('Stock', 'symbol current high low')
stock = Stock('FB', 75.00, high = 75.03, low = 74.90)

'''
What's going on here? Basically, a namedtuple allows us to create an object with
attributes. To create one, you follow the above format; the second argument to
the namedtuple() fn is a space-separated string of things that will be attributes
of that object.
'''
