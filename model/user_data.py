class User(object):

    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password

    @classmethod
    def Admin(cls):
        return cls(username="mkazantsev", password="119074")