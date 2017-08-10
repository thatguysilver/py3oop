import collections

def letter_frequency(sentence):
    'creates a dictionary with default int values of 0; counts letters.'
    frequencies = collections.defaultdict(int)
    for letter in sentence:
        frequencies[letter] +=  1
    return frequencies

num_items = 0
def tuple_counter():
    global num_items
    num_items += 1
    return(num_items, [])

d = collections.defaultdict(tuple_counter)
