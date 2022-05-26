class Band:
    def __init__(self, name, members= []):
        self.name = name
        self.members = members

    def __str__(self):
        return f"The band {self.name}"

    def __repr__(self):
        return f"Band instance. name={self.name}, members={self.members}"


class Musician:
    pass

class Guitarist:
    def __init__(self, name):
        self.name = name


    def __str__(self):
        return f'My name is {self.name} and I play guitar'

    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"

    @staticmethod
    def get_instrument():
        return 'guitar'

    @staticmethod
    def play_solo():
        return "face melting guitar solo"

class Bassist:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'My name is {self.name} and I play bass'

    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"

    @staticmethod
    def get_instrument():
        return 'bass'

    @staticmethod
    def play_solo():
        return "bom bom buh bom"


class Drummer:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'My name is {self.name} and I play drums'

    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"

    @staticmethod
    def get_instrument():
        return 'drums'

    @staticmethod
    def play_solo():
        return "rattle boom crash"



# Band Tests
# A Band instance should have a name attribute which is a string.
# A Band instance should have a members attribute which is a list of instances that inherit from Musician base (or super) class.
# A Band instance should have a play_solos method that asks each member musician to play a solo, in the order they were added to band.
# A Band instance should have appropriate __str__ and __repr__ methods.
# A Band should have a class method to_list which returns a list of previously created Band instances
# Musician Subclass Tests
# Each kind of Musician instance should have appropriate __str__ and __repr__ methods.
# Each kind of Musician instance should have a get_instrument method that returns string.
# Each kind of Musician instance should have a play_solo method that returns string.