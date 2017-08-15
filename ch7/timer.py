# a timer used to demonstrate how fns can be passed around and used whenever.

import datetime
import time

class TimedEvent:
    'Stores variables endtime and callback.'
    def __init__(self, endtime, callback):
        self.endtime = endtime
        self.callback = callback

    def ready(self):
        'Returns True if the given endtime isn\'t in the future.'
        return self.endtime <= datetime.datetime.now()

class Timer:
    '''Stores a list of upcoming events; call_after() 
    allows us to append a new item to the list.'''
    def __init__(self):
        self.events = []

    def call_after(self, delay, callback):
        end_time = datetime.datetime.now() + \
                datetime.timedelta(seconds = delay)

        self.events.append(TimedEvent(end_time, callback))

    def run(self):
        
        while True:
            ready_events = (e for e in self.events if e.ready())
            for event in ready_events:
                event.callback(self)
                self.events.remove(event)
            time.sleep(0.5)
