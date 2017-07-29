import hashlib

class User:
    def __init__(self, username, password):
        '''creates a new user object using given username & password. The
        password is then encrypted before storage.'''
        self.username = username
        self.password = password
        self.is_logged_in = False

    def _encrypt_pw(self, password):
        '''encrypt the password with the username and return theh sha digest.'''
        hash_string = (self.username + password)
        hash_string = hash_string.encode('utf8')
        return hashlib.sha256(hash_string).hexdigest()

    def check_password(self, password):
        'Returns True only if password is valid for this user'

        encrypted = self._encrypt_pw(password)
        return encrypted == self.password

class AuthException(Exception):
    def __init__(self, username, user = None):
        super().__init__(username, user)
        self.username = username
        self.user = user

class UsernameAlreadyExists(AuthException):
    pass

class PasswordTooShort(AuthException):
    pass

class InvalidUsername(AuthException):
    pass

class InvalidPassword(AuthException):
    pass

class PermissionError(Exception):
    'Extends Exception, not AuthException, because it doesnt require a username/pass'
    pass


class NotLoggedInError(AuthException):
    pass

class NotPermittedError(AuthException):
    pass
class Authenticator:
    def __init__(self):
        'Construct an authenticator to manage the users loggin in/out.'
        self.users = {}

    def add_user(self, username, password):
        if username in self.users:
            raise UsernameAlreadyExists(username)
        if len(password) < 6:
            raise PasswordTooShort(username)
        self.users[username] = User(username, password)

    def login(self, username, password):
        try:
            user = self.users[username]
        except KeyError:                   #that is, if the name isn't in users
            raise InvalidUsername(username)

        if not user.check_password(password):
            raise InvalidPassword(username, user)

        user.is_logged_in = True
        return True

    def is_logged_in(self, username):
        if username in self.users:
            return self.users[username].is_logged_in
        return False

class Authorizer:
    def __init__(self, authenticator):
        self.authenticator = authenticator
        self.permissions = {}

    def add_permission(self, perm_name):
        'Create a new permission that users can be added to'
        try:
            perm_set = self.permissions[perm_name]
        except KeyError:
            self.permissions[perm_name] = set()
        else:
            raise PermissionError('Permission exists')

    def permit_user(self, perm_name, username):
        'Grants permission to user'
        try:
            perm_set = self.permissions[perm.name]
        except KeyError:
            raise PermissionError('Permission does not exist')
        else:
            if username not in self.authenticator.users:
                raise InvalidUsername(username)
            perm_set.add(username)

    def check_permission(self, perm_name, username):
        if not self.authenticator.is_logged_in(username):
            raise NotLoggedInError(username)
        try:
            perm_set = self.permissions[perm_name]
        except KeyError:
            raise PermissionError('Permission does not exist.')
        else:
            if username not in perm_set:
                raise NotPermittedError(username)
            else:
                return True




authenticator = Authenticator()

authorizer = Authorizer(authenticator)
