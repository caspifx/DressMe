import DB
import random
import classes

tops = []
pants = []
shoes = []


def init():
    DB.init()
    update_nodes()


def update_nodes():
    global tops
    tops = DB.get_all_nodes('Top')
    print "tops", repr(tops)
    global pants
    pants = DB.get_all_nodes('Pants')
    global shoes
    shoes = DB.get_all_nodes('Shoes')
    return tops, pants, shoes


def pick_random_top():
    index = random.randint(0, len(tops)-1)
    return tops[index]


def match_pant_to_top():
    top = pick_random_top()
    pants_connected = DB.get_connected_good(top)
    best_item = choose_from_list(pants_connected)
    if best_item:
        return (best_item, top)
    else:
        return None


def generate_outfit():
    match = match_pant_to_top()
    if match:
        top, pant = match
        outfit = classes.Outfit(top, pant)
        print outfit
        return outfit
    else:
        print "Failed"
        return 0


def add_top(top):
    DB.create_node(top)
    #update_nodes()
    tops.append(top)


def add_pants(pant):
    DB.create_node(pant)
    #update_nodes()
    pants.append(pant)


def add_shoes(shoes):
    DB.create_node(shoes)
    #update_nodes()
    shoes(shoes)


def create_relationship(top, pant, score):
   DB.create_relationship(top, pant, score)



def choose_from_list(items):
	best_score = 0
	best_item = None
	for obj in items:
		score = obj[1]
		item = obj[0]
		if score > best_score:
		best_score = score
		best_item = item
	return item
		

# added later, needs testing
def recommend_pant_to_top(top):
	pants_connected = DB.get_connected_good(top)
	shirts_connected = []
	for pant in pants_connected:
		good_tops = get_connected_good(pant)
		for top in good_tops:
		shirts_connected.append(top)
	recommeded_pants = []
	for top in shirts_connected:
		good_pants = get_connected_good(top)
		for pant in good_pants:
		recommeded_pants.append(pant)
	best_pants = choose_from_list(recommeded_pants)
	if best_item:
        return best_item
    else:
        return None

		
def main():

    for i in range(3):
        add_top(classes.Top('top' + str(i), '#F7CA18', False, False, False, False))
        add_pants(classes.Pants('pant' + str(i), '#DC3023', False, False, False, False))
    print len(tops)
    create_relationship(tops[1], pants[2], 8)
    create_relationship(tops[1], pants[1], 4)
    create_relationship(tops[0], pants[2], 10)
    create_relationship(tops[2], pants[2], 6)
    outfit = generate_outfit()
    if outfit != 0:
        print "Top {2}, Color:{1} \n Pant {0}, Color {3}".format(outfit.top.id, outfit.top.color, outfit.pants.id,
                                                                 outfit.pants.color)
        return "Top {2}, Color:{1} \n Pant {0}, Color {3}".format(outfit.top.id, outfit.top.color, outfit.pants.id,
                                                                 outfit.pants.color)
    else:
        print 'No Outfit'
        return "No Outfit"

