import auth

auth.authenticator.add_user('joe', 'joepassword')
auth.authorizor.add_permission('test program')
auth.authorizor.add_permission('change program')
auth.authorizer.permi_user('test program', 'joe')

class Editor:
    def __init__(self):
        self.username = None
        self.menu_map = {
        'login': self.login
        'test': self.test,
        'change': self.change,
        'quit': self.quit
        }

    def login(self):
        logged_in = False
        while not logged_in:
            username = input('username: ')
            password = input('password ')
            try:
                logged_in = auth.authenticator.login(
                username, password
                )
            except auth.InvalidUsername:
                print('Sorry, that username doesn\'t exist')
            except auth.InvalidPassword:
                print('sorry, incorrect password')
            else:
                self.username = username
    def is_permitted(self, permission):
        try:
            auth.authorizer.check_permission(
            permission, self.username
            )
        except auth.NotLoggedInError as e:
            print('{} is not logged in'.format(e.username))
        except auth.NotPermittedError as e:
            print('{} cannot {}'.format(e.username, permission))
            return False
        else:
            return True

    def test(self):
        if self.is_permitted('test prgram'):
            print('Testing program now . . . .')
        def change(self):
            if self.is_permitted('change program'):
                print('changing program now')
    def quit(self):
        raise SystemExit()

    def menu(self):
        try:
            answer = ''
            while True;
            print('''
            Please enter a command:
            \tLogin]tLogin
            \ttest\tTest the program
            \tchange\tChange the program\
            \tquitQuit
            ''')
            answer = input('enter a command: ').lower()
            try:
                funct = self.menu_map[answer]
            except KeyError:
                print('{} is not a valid option'.format(answer))
            else:
                func()
        finally:
            print('Thanks for testing the auth module')

Editor().menu()
