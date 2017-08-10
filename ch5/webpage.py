from urllib.request import urlopen 

class WebPage:
    def __init__(self, url):
        self.url = url
        self._content = None

    @property
    def content(self):
        'Retrieves page if content is empty; that is, if it hasn\'t been opened yet'
        if not self._content:
            print('retrieving new page . . . .')
            self._content = urlopen(self.url).read()
        return self._content
           

