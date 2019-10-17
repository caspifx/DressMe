from db_actions import *
import random


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


class Relationship:
    def __init__(self, score, dst, src):
        self.score = score
        self.dst = dst
        self.src = src


class Outfit:
    def __init__(self, top, pants, shoes):
        self.top = top
        self.pants = pants
        self.shoes = shoes


def init():
    """

    :return: list of all of the items in closet
    """
    items = get_all_nodes()
    return items


def get_all_tops(items):
    tops = []
    for item in items:
        if isinstance(item, Top):
            tops.append(item)
    return tops


def get_all_pants(items):
    pants = []
    for item in items:
        if isinstance(item, Pants):
            pants.append(item)
    return pants


def get_all_shoes(items):
    shoes = []
    for item in items:
        if isinstance(item, Shoes):
            shoes.append(item)
    return shoes


def pick_random_top(tops):
    index = random.randint(len(tops))
    return tops[index]


def match_pant_to_top(top):
    pants = get_connected_good(top)
    best_score = 0
    for pant in pants:
        rel = pant[1]
        if rel.score > best_score:
            best_score = rel.score
            best_rel = rel
    if best_rel:
        return best_rel
    else:
        return None


def generate_outfit(tops, pants, shoes):
    top = pick_random_top(tops)
    pant = match_pant_to_top(top)
    outfit = Outfit(top, pant)
    print outfit
    return outfit




