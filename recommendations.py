from connections.models import Connections
from requests.models import Requests
from django_pandas.io import read_frame
import networkx as nx
import matplotlib.pyplot as plt

def recommend(user):
    all_connections = Connections.objects.all()
    all_requests = Requests.objects.all()

    connections_df = read_frame(all_connections)
    connections_G = nx.from_pandas_edgelist(connections_df, 'user1', 'user2')

    requests_df = read_frame(all_requests)
    requests_G = nx.from_pandas_edgelist(requests_df, 'sender', 'receiver')

    # plt.clf()
    # nx.draw(connections_G, with_labels = True)
    # plt.savefig("graph.png")

    recommendations = []
    requested = []

    if user in requests_G:
        requested = list(requests_G.neighbors(user))

    if user in connections_G:
        friends = list(connections_G.neighbors(user))
        for friend in friends:
            friend_relations = list(connections_G.neighbors(friend))
            for f_relation in friend_relations:
                if(
                f_relation != user and
                f_relation not in friends and
                f_relation not in requested and
                f_relation not in recommendations):
                    recommendations.append(f_relation)

    return recommendations

print(recommend('techyon'))
