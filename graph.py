import simplejson as json
#import networkx as nx
from networkx import *

input_dict = json.load(open("graph.json"))

G=DiGraph()

for word in input_dict:
    for defining_word in input_dict[word]:
        #print "%s is defined with %s" % (word, defining_word)
        G.add_edge(defining_word, word)

#print G.nodes()
#print G.edges()
#print info(G)
#print number_of_nodes(G)
#print number_of_edges(G)
#UG=G.to_undirected()
#print number_connected_components(UG)
#print maximal_independent_set(G)
print pagerank(G)
