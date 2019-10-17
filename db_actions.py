from py2neo import Graph, Node, Relationship

graph = Graph("http://localhost:7474/db/data/", user="neo4j", password="1234")
graph.delete_all()


def create_node(name, is_formal, type_n, color, has_painting):
    item = Node(type_n, name=name, is_formal=is_formal, color=color, has_painting=has_painting)
    print item
    graph.create(item)

    return item


def create_relationship(src, dst, score):
    rlp = "GOES WELL" if score > 6 else "BAD MATCH"
    a = Relationship(src, rlp, dst, score=score)
    print a
    graph.create(a)


def get_connected_good(node):
    nodes = []
    for rel in graph.match(node, rel_type="GOES WELL"):
        nodes.append(rel.end_node())
    return nodes


def get_all_nodes(type_n):
    nodes = []
    pass


n1 = create_node("0", "No", "Shirt", "(0,0,0)", "No")
n2 = create_node("1", "No", "Shirt", "(0,0,0)", "No")
create_relationship(n1, n2, 8)
nodes = get_connected_good(n1)
print nodes
