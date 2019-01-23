from Graph import Graph
import sys

def get_bacon_numbers(g, actor_names):
	"""Return a dictionary mapping a each actor name to their Bacon Number"""


	###########################################################################
	#
	# Replace your code here
	#
	# A note on the graph library shown here:
	#    g.get_outedges(key) will accept the name of the node (in this case an integer)
	#     and will return a list of intgers corresponding to all nodes that share an edge
	#     with that node
    #
    # You may use a helper function if it is useful to you
	#
	###########################################################################
    #for i in actor_names:

    #print g.get_inedges('actor_names')
    #print g.get_outedges('actor_names')
	#return None
    #dict = {'Bacon': '0', 'Smith': '2', 'Smith2': '-1', 'Sutherland': '1', 'Cruise': '1'}
        start.setDistance(0)
        start.setPred(None)
        vertQueue = Queue()
        vertQueue.enqueue(start)
        while (vertQueue.size() > 0):
        currentVert = vertQueue.dequeue()
        for nbr in currentVert.getConnections():
            if (nbr.getColor() == 'white'):
                nbr.setColor('gray')
                nbr.setDistance(currentVert.getDistance() + 1)
                nbr.setPred(currentVert)
                vertQueue.enqueue(nbr)
        currentVert.setColor('black')


###############################################################################
#
# Starter Code below this line - you need not modify it if you do not want to
#
###############################################################################

def solve():
    v, e = [int(x) for x in sys.stdin.readline().strip().split()]
    nodes = []

    graph = Graph(True)

    for i in range(v):
        node = sys.stdin.readline().strip().strip()
        graph.add_node(node)
        nodes.append(node)

    for i in range(e):
        start, end = [x for x in sys.stdin.readline().strip().split()]
        assert start in graph.nodes.keys()
        assert end in graph.nodes.keys()
        graph.add_edge(start, end)

    bacon_numbers_dict = get_bacon_numbers(graph, nodes)
    bacon_numbers = [str(bacon_numbers_dict[i]) if i in bacon_numbers_dict.keys() else "-1" for i in nodes]
    return bacon_numbers


print("\n".join(solve()))


