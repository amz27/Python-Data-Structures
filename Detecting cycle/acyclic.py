from Graph import Graph
import sys

def has_cycles(g):
    """Return True if g contains at least 1 cycle and False otherwise"""
    
    ###########################################################################
    #
    # Replace your code here
    #
    # A note on the graph library shown here:
    #    g.get_outedges(name) will accept the name of node N
    #     and will return a list of the names of the nodes to which N has a directed edge
    #
    # You may create a helper function if that is useful to you
    #
    ###########################################################################

    def helper():
        for i in list(g.nodes):
            if bool(g.get_inedges(i)) is False:
                g.remove_node(i)
        return g.nodes

    n = helper()

    for j in list(n):
        if bool(g.get_inedges(j)) is False:
            g.remove_node(j)

    if not bool(g.nodes):
        return False
    else:
        return True


    

###############################################################################
#
# Starter Code below this line - you need not modify it if you do not want to
#
###############################################################################

def solve():
    v, e = [int(x) for x in sys.stdin.readline().strip().split()]

    graph = Graph(False)

    for i in range(v):
        graph.add_node(i+1)

    for i in range(e):
        start, end = [int(x) for x in sys.stdin.readline().strip().split()]
        graph.add_edge(start, end)

    return -1 if has_cycles(graph) else 1

ans = []
numcases = int(sys.stdin.readline().strip())
for _ in range(numcases):
    sys.stdin.readline().strip() # Blank line
    ans.append(str(solve()))

print("\n".join(ans))
