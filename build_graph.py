from graph.embed_node import node_embed
from graph.analysis_node import node_analyze
from graph.compare_node import node_compare

# Pipeline of nodes
graph_nodes = [node_embed, node_analyze, node_compare]

def run_graph(initial_state):
    """
    Sequentially execute nodes on the state.
    """
    state = initial_state
    for node in graph_nodes:
        state = node(state)
    return state
