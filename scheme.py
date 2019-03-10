class User:
    def __init__(self, login, password, session=None):
        self.username = login
        self.password = password
        self.session = session

    def __eq__(self, other):
        if self.username == other.username and self.password == other.password:
            return True
        else:
            return False

    def __repr__(self):
        return 'User: ' + self.username