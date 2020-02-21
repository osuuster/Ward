
class Device:
    """Description of all device functionality"""
    def __init__(self,  sensor):
        self.sensor = sensor

    def state(self):
        if self.sensor:
            return 'triggered'
        else:
            return 'not triggered'