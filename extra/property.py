class UserAccount:
    def __init__(self, username, password):
        self.username = username
        self._password = password

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, new_password):
        if len(new_password) < 6:
            raise ValueError("Password too short")
        self._password = new_password

    @password.deleter
    def password(self):
        raise AttributeError("Can't delete attribute")


if __name__ == "__main__":
    user = UserAccount("eric", "eric123")
    print(user.password)
    user.password = "ericeric"
    print(user.password)
    user.password = "eric"
    print(user.password)
