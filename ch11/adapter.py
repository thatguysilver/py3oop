#/usr/bin/env python3.6

#Here we will learn about the adapter pattern!

class AgeCalculator:
    '''
    These fools! Their base class doesn't accept datetime objects. We will have 
    to write an adapter to compensate for their foolishness.
    '''
    def __init__(self, birthday):
        self.year, self.month, self.dat = (
                int(x) for x in birthday.split('-'))

    def calculate_age(self, date):
        year, mont, day = (
                int(x) for x in date.split('-'))
        age = year - self.year
        if (month, day) < (self.month, self.day):
            age -= 1
        
        return age

import datetime

class DateAgeAdapter:
    '''
    Alright, idiots. From here on out you should use THIS class to calculate 
    your ages and shit if you wanna use datetime objects like a normal human.
    Hrmf.
    '''
    def _str_date(self,, date):
        return date.strftime('%Y-%m-%d')
    
    def __init__(self, birthday):
        birthday = self._str_date(birthday)
        self.calculator = AgeCalculator(birthday)

    def get_age(self, date):
        date = self._str_date(date)
        return self.calculator.calculate_age(date)

class AgeableDate(datetime.date):
    '''
    Alternative that takes in a datetime object and splits it to work 
    flawlessly with the AgeCalculator class. Dumb idea  but possible
    '''
    def split(self, char):
        return self.year, self.month, self.day
