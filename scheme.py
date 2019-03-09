class User:
    def __init__(self, login, password, session=None):
        self.login = login
        self.password = password
        self.session = session

    def __eq__(self, other):
        if self.login == other.login and self.password == other.password:
            return True
        else:
            return False

    def __repr__(self):
        return self.login