class User:
    """User info"""

    def __init__(self, email, first, last, device):
        self.email = email
        self.first = first.lower()
        self.last = last.lower()
        self.device = device.lower()

    def fullname(self):
        return ('{} {}'.format(self.first, self.last).title())
