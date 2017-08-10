class Document:
    def __init__(self):
        self.characters = []
        self.cursor = Cursor(self)
        self.filename = ''

    def insert(self, character):
        'checks if character is a Character or String, then inserts it'
        if not hasattr(character, 'character'):
            character = Character(character)
        self.characters.insert(self.cursor.position, character)
        self.cursor.forward()

    def delete(self):
        del self.characers[self.cursor.position]

    def save(self):
        f = open(self.filename, 'w')
        f.write(''.join(self.characters))
        f.close()
   
    @property
    def string(self):
        'returns the entire contensts of the file so far without saving'
        return ''.join((str(c) for c in self.characters))

class Cursor:
    def __init__(self, document):
        self.document = document
        self.position = 0

    def forward(self):
        self.position += 1

    def back(self):
        self.position -= 1

    def home(self):
        while self.document.characters[
                self.position - 1].character != '\n': 
            self.position -= 1
            if self.position == 0:
                break

    def end(self):
        while self.position < len(self.document.characters) \
        and self.document.characters[
        self.position] != '\n':
            self.position += 1

class Character:
    def __init__(self, character, bold = False, 
            italic = False, underline = False):
        assert len(character) == 1
        self.character = character
        self.bold = bold
        self.italic = italic
        self.underline = underline

    def __str__(self):
        'Assigns special characters to represent altered text if it\'s altered.'
        bold = '*' if self.bold else ''
        italic = '/' if self.italic else ''
        underline = '_' if self.underline else ''
        return bold + italic + underline + self.character

    

