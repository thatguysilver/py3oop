#This is the silly class written with decorators.

class Silly:

    @property
    def silly(self):
        'This is a silly property'
        print('you are getting silly')
        return self._silly

    @silly.setter
    def silly(self, value):
        print(f'you are making silly {value}')
        self._silly = value

    @silly.deleter
    def silly(self):
        print('Whoa, you killed silly!')
        del self._silly
