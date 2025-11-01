import networkx as nx
import matplotlib.pyplot as plt
from collections import Counter
import gzip
with gzip.open("sp_data_school_day_1_g.gexf_.gz", "rb") as f:
    G = nx.read_gexf(f)
#G=nx.read_gml("football.gml")



#G = nx.karate_club_graph()   


deg_centrality = nx.degree_centrality(G)
closeness_centrality = nx.closeness_centrality(G)
betweenness_centrality = nx.betweenness_centrality(G)
eigenvector_centrality = nx.eigenvector_centrality(G, max_iter=1000)
pagerank_centrality = nx.pagerank(G)


def top_nodes(centrality_dict, n=30):
    return [node for node, _ in sorted(centrality_dict.items(), key=lambda x: x[1], reverse=True)[:n]]

top_degree = top_nodes(deg_centrality)
top_closeness = top_nodes(closeness_centrality)
top_betweenness = top_nodes(betweenness_centrality)
top_eigenvector = top_nodes(eigenvector_centrality)
top_pagerank = top_nodes(pagerank_centrality)


all_top_nodes = top_degree + top_closeness + top_betweenness + top_eigenvector + top_pagerank


node_counts = Counter(all_top_nodes)



plt.figure(figsize=(14,6))


nodes = list(node_counts.keys())
counts = list(node_counts.values())


plt.bar(range(len(nodes)), counts, color='cornflowerblue')


plt.xticks(range(len(nodes)), [str(n) for n in nodes], rotation=45, ha='right', fontsize=10)


plt.xlabel("Nodes", fontsize=12)
plt.ylabel("Frequency in 5 centrality lists", fontsize=12)
plt.title("Node frequency across five centrality measures", fontsize=14)

plt.tight_layout()
plt.show()

