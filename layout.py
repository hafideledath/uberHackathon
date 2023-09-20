import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

import heapq

# Create a graph
G = nx.Graph()

# Define different locations and their types
locations = [
    'Skyscraper',
    'Mall pt',
    'Strip \nMall',
    'Grocery \nStore pt',
    'Cinema',
    'Park',
    'Stadium',
    'Apartment \nBuilding',
    'Villa',
    'Tourist \nAttraction pt',
    'School pt',
    'Restaurant',
    'Bank',
    'Library pt',
    'Cafe',
    'Office',
    'Hospital pt',
    'Alex\'s \nHotpot',
    'Gym',
    'Gas \nStation',
    'Airport pt',
    'Train \nStation',
    'Pharmacy',
    'Theater',
    'Post \nOffice pt',
    'Hotel',
    'Beach pt',
    'Zoo',
    'Art \nGallery'
]

# Define fixed positions for each location
positions = {
    'Skyscraper': (5, 15),
    'Mall pt': (2, 12),
    'Strip \nMall': (8, 12),
    'Grocery \nStore pt': (5, 10),
    'Cinema': (2, 8),
    'Park': (8, 8),
    'Stadium': (5, 6),
    'Apartment \nBuilding': (2, 4),
    'Villa': (8, 4),
    'Tourist \nAttraction pt': (5, 2),
    'School pt': (2, 15),
    'Restaurant': (8, 15),
    'Bank': (2, 10),
    'Library pt': (8, 10),
    'Cafe': (2, 6),
    'Office': (8, 6),
    'Hospital pt': (5, 12),
    'Alex\'s \nHotpot': (12, 15),
    'Gym': (12, 12),
    'Gas \nStation': (12, 9),
    'Airport pt': (12, 6),
    'Train \nStation': (12, 3),
    'Pharmacy': (16, 15),
    'Theater': (16, 12),
    'Post \nOffice pt': (16, 9),
    'Hotel': (16, 6),
    'Beach pt': (16, 3),
    'Zoo': (18, 15),
    'Art \nGallery': (18, 12),
}


Ride_options = [
    ("Uber_Green",  0),     # Model of the car: BMW Xi 2007  
    ("UberX_Share", 333),   # Model of the car: Audi RS6 2007
    ("UberXL", 383),        # Model of the car: Cadillac Escalade 2007
    ("Uber_Comfort",  250), # Model of the car: Masearti Quattroporte 2018
    ("Uber_WAV",  441)      # Model of the car: Toyota Sienna 2018 
]


# Add nodes (locations) to the graph with fixed positions
for location in locations:
    x, y = positions[location]
    G.add_node(location, pos=(x, y))

# Define fixed connections between locations (edges) with fixed weights 
# The format of the connection is (location A, Location B, weight/distance)
connections = [
    ('Skyscraper', 'Mall pt', 3),
    ('Bank', 'Mall pt', 3),
    ('Bank', 'Cinema', 3),
    ('Skyscraper', 'Strip \nMall', 2),
    ('Mall pt', 'Grocery \nStore pt', 2),
    ('Strip \nMall', 'Library pt', 3),
    ('Grocery \nStore pt', 'Park', 2),
    ('Grocery \nStore pt', 'Stadium', 1),
    ('Cinema', 'Stadium', 2),
    ('Cafe', 'Apartment \nBuilding', 1),
    ('Stadium', 'Apartment \nBuilding', 2),
    ('Stadium', 'Park', 2),
    ('Park', 'Office', 2),
    ('Airport pt', 'Office', 2),
    ('Stadium', 'Villa', 2),
    ('Stadium', 'Tourist \nAttraction pt', 4),
    ('Apartment \nBuilding', 'Tourist \nAttraction pt', 3),
    ('Villa', 'Tourist \nAttraction pt', 3),
    ('Villa', 'Office', 1),
    ('School pt', 'Mall pt', 3),
    ('Cinema', 'Cafe', 2),
    ('Library pt', 'Park', 1),
    ('Library pt', 'Gas \nStation', 1),
    ('Stadium', 'Office', 2),
    ('Cafe', 'Stadium', 2),
    ('Skyscraper', 'Restaurant', 4),
    ('Strip \nMall', 'Alex\'s \nHotpot', 1),
    ('Strip \nMall', 'Grocery \nStore pt', 3),
    ('Bank', 'Grocery \nStore pt', 3),
    ('School pt', 'Skyscraper', 3),
    ('Restaurant', 'Alex\'s \nHotpot', 2),
    ('Strip \nMall', 'Gym', 4),
    ('Alex\'s \nHotpot', 'Gym', 2),
    ('Gym', 'Gas \nStation', 1),
    ('Gas \nStation', 'Airport pt', 3),
    ('Pharmacy', 'Zoo', 1),
    ('Alex\'s \nHotpot', 'Pharmacy', 3),
    ('Zoo', 'Art \nGallery', 2),
    ('Theater', 'Art \nGallery', 1),
    ('Pharmacy', 'Theater', 2),
    ('Gas \nStation', 'Post \nOffice pt', 2),
    ('Gas \nStation', 'Park', 2),
    ('Gym', 'Theater', 2),
    ('Theater', 'Post \nOffice pt', 2),
    ('Post \nOffice pt', 'Hotel', 2),
    ('Hotel', 'Beach pt', 2),
    ('Hotel', 'Airport pt', 2),
    ('Beach pt', 'Train \nStation', 2),
    ('Train \nStation', 'Airport pt', 2),
    ('Train \nStation', 'Villa', 3),
    ('Hospital pt', 'Strip \nMall', 3),
    ('Hospital pt', 'Skyscraper', 3),
    ('Hospital pt', 'Mall pt', 3),
    ('Restaurant', 'Strip \nMall', 3)
]

for connection in connections:
    G.add_edge(connection[0], connection[1], weight=f"{connection[2]}km")

# Draw the graph
def get_layout():
    # Creates a layout for a city map.
    pos = nx.get_node_attributes(G, 'pos')
    edge_labels = nx.get_edge_attributes(G, 'weight')
    node_labels = {n: n for n, data in G.nodes(data=True)}
    plt.figure(figsize=(15, 15))
    # Draw the graph without labels.
    nx.draw(G, pos, with_labels=False, node_size=5000, node_color='black', font_size=10)
    # Draw the node labels.
    nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=10, font_color='white', verticalalignment='center')
    # Draw the edge labels.
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)
    plt.axis('off')
    plt.title("City Map of UberLand's layout")
    st.pyplot(plt)


def get_shortest_path(graph, node1, node2):
    # priority queue. |
                    # v
    Alex_good = [(0, [node1])]

    # Setting up the set we are going to ues. 
    visited = set()

    # when the priority queue != empty:
    while Alex_good:
        distance, now = heapq.heappop(Alex_good)
        last_node = now[-1]
        if last_node == node2:
            return now

        # check if the last node had been visited 
        if last_node not in visited:
            visited.add(last_node)
            for nextone, dis in graph[last_node]:

                # see if neighbur node had beenvisited
                if nextone not in visited:
                    new = distance + dis
                    path = now + [nextone]
                    heapq.heappush(Alex_good, (new, path))
    return []
graph = {}

# Add the connections to the graph dictionary.
for node1, node2, distance in connections:
    if node1 not in graph:
        graph[node1] = []
    if node2 not in graph:
        graph[node2] = []
    graph[node1].append((node2, distance))
    graph[node2].append((node1, distance))

def get_branch_impact(a, b, impact):
    for connection in connections:
        if a in connection and b in connection:
            if not b.endswith(" pt"):
                return connection[2] * impact
            return connection[2] * 35

def get_route_impact(a, b):
    path = get_shortest_path(graph, a, b)
    sumlist = []
    for model in Ride_options: 
        sum = 0   
        for i in range(len(path) - 1):
            n1, n2 = path[i:i+2]
            sum += get_branch_impact(n1, n2, model[1])
        sumlist.append(sum)
    return sumlist


def get_branch_distance(a, b):
    # Get the distance/weight between location A and location B 
    # returns the distance/weight
    for connection in connections:
        if a in connection and b in connection:
            return connection[2]

def get_route_distance(a, b):
    # Get the distance/weight between location A and location B 
    # Return the totle sum of distance/weight 
    path = get_shortest_path(graph, a, b)
    sum = 0
    for i in range(len(path) - 1):
        n1, n2 = path[i:i+2]
        sum += get_branch_distance(n1, n2)
    return sum
# general carbon emissions for a merecedez bens 2018 is 120grams/km
# for carbon emissions mutliply distance by 120
# for price mui