#Used to illustrate why we don't need to use get/set methods in py.

class Color:
    def __init__(self, rgb_value, name):
        self.rgb_value = rgb_value
        self._name = name

    def _set_name(self, name):
        if not name:
            raise Exception('invalid name')
        self._name = name

    def _get_name(self):
        return self._name

    def _del_name(self):
        print('Deleted.')
        del self._name

    name = property(_get_name, _set_name, _del_name, 'Allows us to get, set, del')
    

    #property() supports get, set, del, and documentation functions. Setting a 
    #variable equal to property() basically allows us to return or alter a class
    #attribute.
