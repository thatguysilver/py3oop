class StringJoiner(list):
    def __enter__(self):
        return self
    def __exit__(self, type, value, tb):
        '''type, value and tb (traceback) all tell the intepreter how to 
        return errors.'''
        self.result = ''.join(self)

import random, string
with StringJoiner() as joiner:
    for i in range(15):
        joiner.append(random.choice(string.ascii_letters))

print(joiner.result)
