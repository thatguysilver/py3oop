import datetime

# store the next available id for all new notes
last_id = 0

class Notebook:
    '''Collection of notes that can be altered further.'''

    def __init__(self):
        'Initializes an empty notebook with an empty list.'

        self.notes = []

    def new_note(self, memo, tags = ''):
        'Creates a new note, adds it to list using our Note class'
        self.notes.append(Note(memo, tags))

    def modify_memo(self, note_id, memmo):
        'Find the note with the given id and change its memo to given value'

        for note in self.notes:
            if note.id == note_id:
                note.memo = memo
                break

    def modify_tags(self, note_id, memmo):
        'Find the note with the given id and change its memo to given value'

        for note in self.notes:
            if note.id == note_id:
                note.tags = tags 
                break

    def _find_note(self, note_id):
        '''locates a note with the given id'''
        for note in self.notes:
            if str(note.id) == str(note_id):
                return note
        return None

    def modify_memo(self, note_id, memo):
        'find the note with the given id and alter its memo to given value'
        if note:
            note.memo = memo
            return True
        return False

    def search(self, filter):
        'Finds yo note'
        return [note for note in self.notes if note.match(filter)]


class Note:
    'A note in the notebook.'

    def __init__(self, memo, tags = ''):
        '''Initializes a note with memo and optional space-separated tags.
        The note's creation date and unique id are automatically created.'''

        self.memo = memo

        self.tags = tags
        self.creation_date = datetime.date.today()

        global last_id
        last_id += 1
        self.id = last_id

    def match(self, filter):
        'Determines if this note matches filter text. Returns True if match.'

        return filter.lower() in self.memo.lower() or filter in self.tags

    def date(self):
        print(self.creation_date)

    



