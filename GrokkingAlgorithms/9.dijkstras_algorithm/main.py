import math

## Dijkstra's algorithm
# cant run on negative weight edges 
graph = {}
graph["you"] = ["alice", "bob", "claire"]

graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["fin"]

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"]

infinity = math.inf
costs = {}
costs["a"] = 6
costs["b"] = 2  
costs["fin"] = infinity

parents = {}
parents["a"] = "start"
parents["b"] = "start" 
parents["fin"] = None

processed = set()

def find_lowest_cost_node(costs):
    lowest_cost = math.inf
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
        return lowest_cost_node


node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbours = graph[node]
    for n in neighbours.keys():
        new_cost = cost+neighbours[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node 
    processed.add(node)
    node = find_lowest_cost_node(costs)
    





print(list(graph["start"].keys()))



## Bellman-Ford algorithm
