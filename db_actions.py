from py2neo import Graph, Node, Relationship
import classes

graph = Graph("http://localhost:7474/db/data/", user="neo4j", password="1234")
graph.delete_all()


def create_node(item):
    type_n = find_type(item)
    item = Node(type_n, name=item.id, is_formal=item.formal, color=item.color, has_painting=item.plain)
    print item
    graph.create(item)


def create_relationship(item_src, item_dst, score):
    src = get_node(item_src)
    dst = get_node(item_dst)
    rlp = "GOES WELL" if score > 6 else "BAD MATCH"
    a = Relationship(src, rlp, dst, score=score)
    print a
    graph.create(a)


def get_connected_good(item):
    node = get_node(item)
    good_nodes = []
    for rel in graph.match(node, rel_type="GOES WELL"):
        good_nodes.append(rel.end_node())
    return good_nodes


def get_all_nodes(type_n):
    all_nodes = []
    for n in graph.find(type_n):
        all_nodes.append(n)
    return all_nodes


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
