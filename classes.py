class Item:
    def __init__(self, id, color, plain, formal):
        self.id = id
        self.color = color
        self.plain = plain
        self.formal = formal


class Top(Item):
    def __init__(self, id, color, pain, formal, sleeve, neck):
        Item.__init__(self, id, color, pain, formal)
        self.sleeve = sleeve
        self.neck = neck


class Pants(Item):
    """
        Type: 1 is jeans, 2 is training, 3 is tights
    """

    def __init__(self, id, color, pain, formal, length, type):
        Item.__init__(self, id, color, pain, formal)
        self.length = length
        self.type = type


class Shoes(Item):
    """
        Type: 1 is sports, 2 is sneackers, 3 is fancy
    """

    def __init__(self, id, color, pain, formal, type):
        Item.__init__(self, id, color, pain, formal)
        self.type = type

