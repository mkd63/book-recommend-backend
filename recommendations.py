from connections.models import Connections
from django_pandas.io import read_frame
import networkx as nx
import matplotlib.pyplot as plt

all_connections = Connections.objects.all()
df = read_frame(all_connections)

Graphtype = nx.Graph()
G = nx.from_pandas_edgelist(df, 'user1', 'user2',  create_using=Graphtype)
# nx.draw(G, with_labels = True)
# plt.savefig("graph.png")

def nodes_connected(u, v):
    return u in G.neighbors(v)

def recommend(user):
    m = []
    fr = list(G.neighbors(user))
    for i, ibrdict in G.adjacency():
        if(nodes_connected(user,i)):
            for k in ibrdict.keys():
                if(k != user and k not in fr and k not in m):
                    m.append(k)
    return m

print(recommend('test4'))
