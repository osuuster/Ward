class User:
    """User info"""

    def __init__(self, first, last, device):
        self.first = first.lower()
        self.last = last.lower()
        self.device = device.lower()

    def fullname(self):
        return ('{} {}'.format(self.first, self.last).title())


new_user = User("Oliver", 'Suuster', 'door')
print(new_user.fullname())
