graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["c"] = 4
graph["a"]["d"] = 2

graph["b"] = {}
graph["b"]["a"] = 8
graph["b"]["d"] = 7

graph["c"] = {}
graph["c"]["fin"] = 3
graph["c"]["d"] = 6

graph["d"] = {}
graph["d"]["fin"] = 1

graph["fin"]={}

infinity = float("inf")

#make cost table

costs = {}
costs["a"] = 5
costs["b"] = 2
costs["c"] = infinity
costs["d"] = infinity
costs["fin"] = infinity

parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["c"] = None
parents["d"] = None
parents["fin"] = None
parents["start"] = None

processed = []

def find_lowest_cost_node(costs):
  lowest_cost = float("inf")
  lowest_cost_node = None
  for node in costs:
    cost = costs[node]
    if cost < lowest_cost and node not in processed:
      lowest_cost = cost
      lowest_cost_node = node
  return lowest_cost_node

node = find_lowest_cost_node(costs)
while node is not None:
  cost=costs[node]
  neightbors = graph[node]
  for n in neightbors.keys():
    new_cost = cost + neightbors[n]
    if costs[n] > new_cost:
      costs[n] = new_cost
      parents[n] = node
  processed.append(node)
  node = find_lowest_cost_node(costs)
print(costs["fin"])

def find_path_of_lowest(end):
  path = [end]
  nextNode = parents[end]
  while nextNode is not None:
    path.append(nextNode)
    currNode = nextNode
    nextNode = parents[currNode]
  return path[::-1]
print(find_path_of_lowest("fin"))
