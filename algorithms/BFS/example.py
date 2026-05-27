from collections import deque
from algorithms.BFS.globals import tree

def bfs(tree, start):
    visited = [] #An array to keep track of nodes.
    queue = deque([start]) #Initialize the queue with the starting node.

    while queue: # While there are still nodes to process

        node = queue.popleft() #Dequeue a node from the front of the queue, FIFO

        if node not in visited: #Check if the node has been visited 
            visited.append(node) #Mark it as visited now
            print(node, end=" ")

            #Enqueue all the unvisited neighbors now
            for neighbor in tree[node]: queue.append(neighbor) #Add unvisited neighbors to the queue.