from connections.models import Connections
from django_pandas.io import read_frame
import networkx as nx
import matplotlib.pyplot as plt

def recommend(user):
    all_connections = Connections.objects.all()
    df = read_frame(all_connections)

    Graphtype = nx.Graph()
    G = nx.from_pandas_edgelist(df, 'user1', 'user2',  create_using=Graphtype)

    m = []
    fr = list(G.neighbors(user))
    for i, ibrdict in G.adjacency():
        if(user in G.neighbors(i)):
            for k in ibrdict.keys():
                if(k != user and k not in fr and k not in m):
                    m.append(k)
    return m
