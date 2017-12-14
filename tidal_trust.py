import networkx as nx
import matplotlib.pyplot as plt

graph = [(1, 2),(1, 3),(1, 4),(2, 5),(2, 6),(3, 5),(3, 6),(4, 6),(5, 7),(6, 7)]
node_max = [0,9,8,10,9,9,0]
ratings = [9,8,10,9,8,10,10,9,8,6]
q = []
color = [0]*len(graph)

def get_graph(graph):

    # extract nodes from graph
    nodes = set([n1 for n1, n2 in graph] + [n2 for n1, n2 in graph])

    # create networkx graph
    # G=nx.Graph()
    G = nx.DiGraph()

    # add nodes
    for node in nodes:
    	G.add_node(node)

    # add edges
    for edge in graph:
        G.add_edge(edge[0], edge[1])

    # draw graph
    # pos = nx.shell_layout(G)
    # nx.draw(G, pos)

    # show graph
    # plt.show()
    return G

def draw_graph(G, graph, labels=None, graph_layout='shell',
               node_size=1600, node_color='blue', node_alpha=0.3,
               node_text_size=12,
               edge_color='blue', edge_alpha=0.3, edge_tickness=1,
               edge_text_pos=0.3,
               text_font='sans-serif'):

    # create networkx graph
    # G=nx.Graph()

    # add edges
    # for edge in graph:
    #     G.add_edge(edge[0], edge[1])

    # these are different layouts for the network you may try
    # shell seems to work best
    if graph_layout == 'spring':
        graph_pos=nx.spring_layout(G)
    elif graph_layout == 'spectral':
        graph_pos=nx.spectral_layout(G)
    elif graph_layout == 'random':
        graph_pos=nx.random_layout(G)
    else:
        graph_pos=nx.shell_layout(G)

    # draw graph
    nx.draw_networkx_nodes(G,graph_pos,node_size=node_size, 
                           alpha=node_alpha, node_color=node_color)
    nx.draw_networkx_edges(G,graph_pos,width=edge_tickness,
                           alpha=edge_alpha,edge_color=edge_color)
    nx.draw_networkx_labels(G, graph_pos,font_size=node_text_size,
                            font_family=text_font)

    if labels is None:
        labels = range(len(graph))

    edge_labels = dict(zip(graph, labels))
    nx.draw_networkx_edge_labels(G, graph_pos, edge_labels=edge_labels, 
                                 label_pos=edge_text_pos)

    # show graph
    plt.show()

def tidal_trust(source, sink):
	global q
	q.append(source)
	depth = 1
	max_depth = 10
	found = False
	temp_q = []

	while (len(q) != 0 & depth <= max_depth):
		nl = q.pop()
		print(nl)
		print("loop")
		depth = depth + 1

		for n in g.neighbors(nl):
			if n == sink:
				found = True
				print("found")
				max_depth = depth
				
			else:
				if color[n] == 0:
					color[n] = 1
					temp_q.append(n)
					# for t in temp_q:
					# 	if n != t:
					# 		temp_q.append(n)

		if not q:
			print(temp_q)
			q = temp_q
			depth = depth + 1
			temp_q = []


		

g = get_graph(graph)
#draw_graph(g, graph)
tidal_trust(1,7)