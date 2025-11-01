import networkx as nx 
import pandas as pd 
import matplotlib.pyplot as plt
import gzip
#with gzip.open("sp_data_school_day_1_g.gexf_.gz", "rb") as f:
   # g = nx.read_gexf(f)
#g=nx.read_gml("dolphins.gml")



#g = nx.karate_club_graph()   






deg_centrality = nx.degree_centrality(g)
closeness_centrality = nx.closeness_centrality(g)
betweenness_centrality = nx.betweenness_centrality(g)
eigenvector_centrality = nx.eigenvector_centrality(g, max_iter=1000)
pagerank_centrality = nx.pagerank(g)


def print_top_nodes(title, data, top_n=30, group_size=5):
    print(f"\n{title}:")
    sorted_nodes = [node for node, _ in sorted(data.items(), key=lambda x: x[1], reverse=True)[:top_n]]
    
    
    for i in range(0, len(sorted_nodes), group_size):
        group = sorted_nodes[i:i+group_size]
        print(f"گروه {i//group_size + 1}: {group}")


print_top_nodes("1️⃣ Degree Centrality", deg_centrality)
print_top_nodes("2️⃣ Closeness Centrality", closeness_centrality)
print_top_nodes("3️⃣ Betweenness Centrality", betweenness_centrality)
print_top_nodes("4️⃣ Eigenvector Centrality", eigenvector_centrality)
print_top_nodes("5️⃣ PageRank", pagerank_centrality)

nx.draw_networkx(g)
plt.show()
