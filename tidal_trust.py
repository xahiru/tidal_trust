import networkx as nx
import matplotlib.pyplot as plt

graph = [(1, 2),(1, 3),(1, 4),(2, 5),(2, 6),(3, 5),(3, 6),(4, 6),(5, 7),(6, 7)]#,(6, 8)]
#node_max should have an element for each unique node in the graph
node_max = [0,9,8,10,9,9,0]#,0]
#ratings should be of length len(graph)
ratings = [9,8,10,9,8,10,10,9,8,6]#,0]
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
    	G.add_node(node, max=node_max[node-1])

    # add edges
    for edge in graph:
        G.add_edge(edge[0], edge[1], rating=ratings[graph.index(edge)])
        # print("index ed", graph.index(edge))

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

def path_flow(souce,node):
	pass

def tidal_trust(source, sink):
	global q
	d = [];
	q.append(source)
	depth = 1
	max_depth = 1000
	found = False
	temp_q = []
	scores = nx.get_edge_attributes(g, 'rating')

	children = []
	cache_rating = []

	while (len(q) != 0 & depth <= max_depth):
		nl = q.pop()
		# print(nl)
		# print("loop")
		print("current node", nl)
		

		for n in g.neighbors(nl):
			if n == sink:
				cache_rating.append(scores[(nl,n)])
				found = True
				print("found")
				# print("cache_rating", cache_rating)
				max_depth = depth
				flow = min(cache_rating)
				# print("min=",flow)
				d.append([n])
				# children.append(sink)
				
			else:
				if color[n] == 0:
					color[n] = 1
					temp_q.append(n)
					
				# for n2 in g.neighbors(nl):
					# if color[n2] == 0:
					# 	color[n2] = 1
					# 	temp_q.append(n2)
					# 	# for t in temp_q:
						# 	if n2 != t:
						# 		# d.append(t)
						# 		children.append(n2)

		print("cache_rating", cache_rating)
		if not q:
			# print("temp_p",temp_q)
			# print("depth",depth)
			if(not found):
				q = temp_q
				d.append(temp_q[:])
				# print(d)
				depth = depth + 1
				temp_q = []

	print(d)
	print(depth)
	
	while not d:
		print(d.pop())

g = get_graph(graph)
#draw_graph(g, graph,ratings)
tidal_trust(1,7)

