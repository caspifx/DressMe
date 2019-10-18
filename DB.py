from py2neo import Graph, Node, Relationship
import classes

graph = None
all_nodes = []


def init():
    global graph
    global matcher
    graph = Graph("http://localhost:7474/db/data/", user="neo4j", password="1234")
    graph.delete_all()
    print 'Look at Graph at %s' % "http://localhost:7474/db/data/"


def create_node(item):
    type_n = find_type(item)
    item = Node(type_n, name=item.id, is_formal=item.formal, color=item.color, has_painting=item.plain)
    print item
    graph.create(item)
    all_nodes.append(item)


def node_to_obj(node):
    item_type = node.labels()
    if 'Top' in item_type:
        item = classes.Top(node['name'], node['color'], node['plain'], node['is_formal'], False, False)
    elif 'Pants' in item_type:
        item = classes.Pants(node['name'], node['color'], node['plain'], node['is_formal'], False, False)
    elif 'Shoes' in item_type:
        item = classes.Top(node['name'], node['color'], node['plain'], node['is_formal'], False)
    return item


def create_relationship(item_src, item_dst, score):
    src = get_node(item_src)
    dst = get_node(item_dst)
    rlp = "GOES WELL" if score > 6 else "BAD MATCH"
    a = Relationship(src, rlp, dst, score=score)
    print a
    graph.create(a)


def get_connected_good(item):
    node = get_node(item)
    matching_nodes = []
    for rel in graph.match(node, rel_type="GOES WELL"):
        node = rel.end_node()
        item = node_to_obj(node)
        matching_nodes.append((item, rel['score']))
    return matching_nodes


def get_all_nodes(type_n):
    all_nodes_type = []
    print type_n
    for n in graph.find(type_n):
        print "!!!!!"
        print n
        all_nodes_type.append(node_to_obj(n))
    return all_nodes_type


def get_node(item):
    id_n = item.id
    type_n = find_type(item)
    return graph.find_one(type_n, "name", id_n)


def find_type(item):
    if isinstance(item, classes.Top):
        return 'TOP'
    elif isinstance(item, classes.Pants):
        return 'Pants'
    else:
        return 'Shoes'


"""
    top = classes.Top('0', "(0,0,0)", "No", "No", "Short", "No")
top2 = classes.Top('1', "(0,0,0)", "No", "No", "Short", "No")
n1 = create_node(top)
n2 = create_node(top2)
t1 = get_node(top2)
print t1
0/0
create_relationship(n1, n2, 8)
nodes = get_connected_good(n1)
print nodes
print "!!!!!"
print get_all_nodes("top")
"""