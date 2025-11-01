import networkx as nx
import matplotlib.pyplot as plt
import gzip

file_path = "sp_data_school_day_1_g.gexf_.gz"


#with gzip.open("sp_data_school_day_1_g.gexf_.gz", "rb") as f:
    #G = nx.read_gexf(f)
#G = nx.read_gml(file_path)
G=nx.karate_club_graph()

plt.figure(figsize=(8, 6))
nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray', node_size=800, font_size=10)
plt.title("Graph Visualization")
plt.show()


if nx.is_connected(G):
    # Calculate diameter and radius
    diameter = nx.diameter(G)
    radius = nx.radius(G)
    
    print(f"Graph Diameter: {diameter}")
    print(f"Graph Radius: {radius}")
    
    
    source = list(G.nodes())[0]
    target = list(G.nodes())[-1]
    
    shortest_path = nx.shortest_path(G, source=source, target=target)
    shortest_path_length = nx.shortest_path_length(G, source=source, target=target)
    
    print(f"Shortest path from {source} to {target}: {shortest_path}")
    print(f"Shortest path length: {shortest_path_length}")
else:
    print("The graph is not connected — diameter and radius are undefined.")
