import networkx as nx
import matplotlib.pyplot as plt
from itertools import compress
import numpy as np

graph = [(1, 2),(1, 3),(1, 4),(2, 5),(2, 6),(3, 5),(3, 6),(4, 6),(5, 7),(6, 7)]#,(6, 8)]
#node_max should have an element for each unique node in the graph
#node_max = [0,9,8,10,9,9,0]#,0]
node_max = []
#ratings should be of length len(graph)
ratings = [9,8,10,9,8,10,10,9,8,6]#,0]
q = []
color = [0]*len(graph)

def get_graph(graph):

    # extract nodes from graph
    nodes = set([n1 for n1, n2 in graph] + [n2 for n1, n2 in graph])
    # node_max = [0]* len(nodes)
    # create networkx graph
    # G=nx.Graph()
    G = nx.DiGraph()

    # add nodes
    for node in nodes:
    	# G.add_node(node, max=node_max[node-1])
    	G.add_node(node, max=0)

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

 
    nx.draw_networkx_nodes(G,graph_pos,node_size=node_size, 
                           alpha=node_alpha, node_color=node_color)
    nx.draw_networkx_edges(G,graph_pos,width=edge_tickness,
                           alpha=edge_alpha,edge_color=edge_color)
    node_labels = nx.get_node_attributes(G,'max')
    nx.draw_networkx_labels(G, graph_pos,labels = node_labels,font_size=node_text_size,
                            font_family=text_font)

    # if labels is None:
    #     labels = range(len(graph))

    edge_labels = nx.get_edge_attributes(G,'rating')
    nx.draw_networkx_edge_labels(G, graph_pos, edge_labels=edge_labels, 
                                 label_pos=edge_text_pos)

    # show graph
    plt.show()

# def path_flow(scores,node):
# 	#get edges list
# 	#from find edges ending with node
# 	#return min

# 	pass

def tidal_trust(source, sink):
	global q
	global node_max
	d = [];
	q.append(source)
	d.append(source)
	depth = 1
	max_depth = 1000
	found = False
	temp_q = []
	scores = nx.get_edge_attributes(g, 'rating')

	cache_rating = []


	while (len(q) != 0 & depth <= max_depth):
		nl = q.pop()
		print("current top node", nl)
		
		for n in g.neighbors(nl):
			# if depth > 1:
			# 	print("my[",n,"]parent(s): ", d[depth-1])
			# else:
				# print("my[",n,"]parent(s): ", nl)
			
			print("my[",n,"] fake parent(s) : ", d[depth-1])
			
			ko = [e[1]== n for e in g.edges]
			temp_l = list(compress(g.edges(), ko))
			# print("temp_l", temp_l)
			max_list = []
			pp_list = []
			[pp_list.append(l[0]) for l in temp_l]
			print("pp list",pp_list)
			atts = nx.get_node_attributes(g,'max')
			
			[max_list.append(atts[l[0]]) for l in list(compress(g.edges(), ko))]

			print("real parents maxes", max_list)
			r = scores[(nl,n)]
			if depth == 1:
				g.node[n]['max'] = r
			else:
				g.node[n]['max'] = max(max_list)
				print('max_node',pp_list[np.argmax(max_list)])
				print('max_node scored me', scores[(pp_list[np.argmax(max_list)],n)] )
				g.node[n]['max'] = min(max(max_list),scores[(pp_list[np.argmax(max_list)],n)]) 

			if n == sink:
				cache_rating.append(scores[(nl,n)])
				found = True
				print("found")
				# print("cache_rating", cache_rating)
				max_depth = depth
				# print("found depth", depth)
				# print("previous level", d[depth-2])
				# get the max node leading to n
				#the
				flow = min(cache_rating)
				# print("min=",flow)
				# d.append([n])
				# children.append(sink)
				temp_q.append(n)
				
			else:
				if color[n] == 0:
					color[n] = 1
					temp_q.append(n)
					#get the max node leading to n
					#the
				# print(">>>>>>>>>")

		# print("cache_rating", cache_rating)
		if not q:
			d.append(temp_q[:])
			if(not found):
				q = temp_q
				# d.append(temp_q[:])
				# print(d)
				depth = depth + 1
				temp_q = []

	print("d",d)
	# print("depth",depth)
	uuu = nx.get_node_attributes(g,'max')
	node_max = uuu
	# print("maxes", node_max)
	while not d:
		print(d.pop())

g = get_graph(graph)
draw_graph(g, graph)
tidal_trust(1,7)
draw_graph(g, graph)

