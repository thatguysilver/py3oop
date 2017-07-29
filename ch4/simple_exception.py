#Basic demo of exception raising.

class EvenOnly(list):
    def append(self, integer):
        if not isinstance(integer, int):
            raise TypeError('Only integers can be added!')
        if integer % 2:
            raise ValueError('Only even numbers can be added.')
        super().append(integer)

def funny_division(number):
    try: 
        if number == 13:
            raise ValueError('Unlucky!')
        return 100 / number
    except ValueError:
        print('No, not 13!')
        raise

funny_division(13)
