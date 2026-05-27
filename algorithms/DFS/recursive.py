from algorithms.DFS.globals import tree

def dfs_recursive(tree, node, visited=None):

    if visited is None: visited = set() #Initialize the visited set
    visited.add(node) #Marking each node as visited
    print(node) #Printing the current node
    for child in tree[node]:
        if child not in visited:
            dfs_recursive(tree, child, visited)

dfs_recursive(tree, 'A')