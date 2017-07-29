from notebook import Notebook, Note

class Menu:
    'Displays a CLI menu'
    def __init__(self):
        self.notebook = Notebook()
        self.choices = {
                '1': self.show_notes,
                '2': self.search_notes,
                '3': self.add_note,
                '4': self.modify_note,
                '5': self.quit
                }
    def display_menu(self):
        print('''

        1. Show all notes
        2. Search all notes
        3. Add a note
        4. Modify a note
        5. Quit
        ''')

    def run(self):
        'Displays menu, takes input'
        while True:
            self.display_menu()
            choice = input('Enter an option: ')
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print(f'{choice} is not a valid choice')

    def show_notes(self, notes = None):
        if not notes:
            notes = self.notebook.notes
        for note in notes:
            print(f'{note.id}, {note.tags}, {note.memo}')

    def search_notes(self):
        filter = input('Search for: ')
        notes = self.notebook.search(filter)
        self.show_notes(notes)

    def add_note(self):
        memo = input('Enter a memo: ')
        self.notebook.new_note(memo)
        print('Your note has been added')

    def modify_note(self):
        id = input('enter a note id: ')
        memo = input('enter a memo: ')
        tags = input('Enter tags: ')
        if memo:
            self.notebook.modify_memo(id, memo)
        if tags:
            self.notebook.modify_tags(id, tags)
    
    def quit(self):
        print('Fuck off')
        sys.exit(0)

if __name__ == '__main__':
    Menu().run()
