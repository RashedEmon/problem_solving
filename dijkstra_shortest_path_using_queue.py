from queue import Queue
import math

def shortest_path(source, graph, cost):
    q = Queue()
    distance = {key: 100000 for key in graph}
    q.put(source)
    distance[source] = 0
    
    while not q.empty():
        u = q.get()
        for v in graph[u]:
            if int(distance[u]) + int(cost[u][v]) < int(distance[v]):
                distance[v] = int(distance[u]) + int(cost[u][v])
                q.put(v)
    
    return distance
    


if __name__ == '__main__':
    graph = {
        "1":["2", "3"],
        "2": ["3"],
        "3": ["4"],
        "4": []
    }
    cost = {
        "1": {"2": "2", "3": "5"},
        "2": {"3": "1"},
        "3": {"4": "3"}
    }
    print(shortest_path("1", graph, cost)["4"])
    
