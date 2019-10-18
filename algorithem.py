import DB
import random
import classes

tops = DB.get_all_nodes('Top')
pants = DB.get_all_nodes('Pants')
shoes = DB.get_all_nodes('Shoes')


def pick_random_top():
    index = random.randint(len(tops))
    return tops[index]


def match_pant_to_top():
    top = pick_random_top()
    pants_connected = DB.get_connected_good(top)
    best_score = 0
    for pant in pants_connected:
        score = pant[1]
        if score > best_score:
            best_score = score
            best_item = pant[0]
    if best_item:
        return (best_item, top)
    else:
        return None


def generate_outfit():

    pant, top = match_pant_to_top()
    outfit = classes.Outfit(top, pant)
    print outfit
    return outfit
