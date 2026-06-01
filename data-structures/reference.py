import heapq
from collections import deque

# ==========================================
# MAPS / DICTIONARIES
# ==========================================
# Used for counting frequency, caching, grouping
# O(1) average for get, set, delete

d = {}
d["key"] = "value"       # set
d["key"]                 # get
d.get("key", "default")  # get with default if key doesn't exist
del d["key"]             # delete
"key" in d               # check if key exists O(1)
d.keys()                 # get all keys
d.values()               # get all values
d.items()                # get all key/value pairs

# counting frequency example
nums = [1, 2, 2, 3, 3, 3]
freq = {}
for n in nums:
    freq[n] = freq.get(n, 0) + 1  # {1:1, 2:2, 3:3}

#Two Sum


# ==========================================
# SETS
# ==========================================
# Used for tracking visited, removing duplicates, O(1) membership check

s = set()
s.add(1)        # add element
s.remove(1)     # remove element
1 in s          # check membership O(1)
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s1 & s2         # intersection: {2, 3}
s1 | s2         # union: {1, 2, 3, 4}
s1 - s2         # difference: {1}

# removing duplicates example
nums = [1, 2, 2, 3, 3, 3]
unique = set(nums)  # {1, 2, 3}


# ==========================================
# LISTS / ARRAYS
# ==========================================
# Used for ordered data, index based access

arr = [1, 2, 3]
arr.append(4)       # push to end O(1)
arr.pop()           # pop from end O(1)
arr.pop(0)          # pop from front O(n)
arr.insert(0, 5)    # insert at index O(n)
arr[0]              # access by index O(1)
arr[-1]             # last element O(1)
arr[1:3]            # slicing O(n)
arr.sort()          # sort in place O(n log n)
sorted(arr)         # returns new sorted list O(n log n)
len(arr)            # length O(1)

# two pointer example
left, right = 0, len(arr) - 1
while left < right:
    left += 1
    right -= 1


# ==========================================
# LINKED LISTS
# ==========================================
# Used for dynamic data, O(1) insert/delete at known position

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)  # 1 -> 2 -> 3

# traverse
curr = head
while curr:
    print(curr.val)
    curr = curr.next

# slow/fast pointer example (cycle detection)
slow = head
fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next


# ==========================================
# TREES
# ==========================================
# Used for hierarchical data

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

# inorder traversal: left -> root -> right
def inorder(node):
    if not node: return
    inorder(node.left)
    print(node.val)
    inorder(node.right)

# preorder traversal: root -> left -> right
def preorder(node):
    if not node: return
    print(node.val)
    preorder(node.left)
    preorder(node.right)

# postorder traversal: left -> right -> root
def postorder(node):
    if not node: return
    postorder(node.left)
    postorder(node.right)
    print(node.val)


# ==========================================
# HEAPS / PRIORITY QUEUES
# ==========================================
# Used for always needing min/max of changing data

min_heap = []
heapq.heappush(min_heap, 3)   # push O(log n)
heapq.heappush(min_heap, 1)
heapq.heappush(min_heap, 2)
heapq.heappop(min_heap)        # pop smallest O(log n)
min_heap[0]                    # peek smallest O(1)
heapq.heapify([3, 1, 2])       # convert list to heap O(n)
heapq.nlargest(2, min_heap)    # get 2 largest O(n log k)
heapq.nsmallest(2, min_heap)   # get 2 smallest O(n log k)

# max heap — negate values
max_heap = []
heapq.heappush(max_heap, -5)
heapq.heappush(max_heap, -1)
print(-max_heap[0])             # peek largest: 5
print(-heapq.heappop(max_heap)) # pop largest: 5


# ==========================================
# QUEUES
# ==========================================
# Used for FIFO processing, BFS level by level traversal

queue = deque()
queue.append(1)      # enqueue to back O(1)
queue.append(2)
queue.popleft()      # dequeue from front O(1)
queue[0]             # peek front O(1)
queue[-1]            # peek back O(1)
len(queue)           # length O(1)

# BFS example
def bfs(root):
    if not root: return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.val)
        if node.left: queue.append(node.left)
        if node.right: queue.append(node.right)


# ==========================================
# GRAPHS
# ==========================================
# Used for networks, relationships between nodes

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [], 'E': [], 'F': []
}

# DFS on graph
def dfs(graph, node, visited=set()):
    if node in visited: return
    visited.add(node)
    print(node)
    for neighbor in graph[node]:
        dfs(graph, neighbor, visited)

# BFS on graph
def bfs_graph(graph, start):
    visited = set()
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            print(node)
            for neighbor in graph[node]:
                queue.append(neighbor)


# ==========================================
# STACKS
# ==========================================
# Used for LIFO processing, tracking previous state

stack = []
stack.append(1)   # push O(1)
stack.append(2)
stack.pop()       # pop from top O(1)
stack[-1]         # peek top O(1)
len(stack)        # length O(1)
not stack         # check if empty O(1)

# valid parentheses example
def isValid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in mapping:
            if not stack or stack[-1] != mapping[char]: return False
            stack.pop()
        else:
            stack.append(char)
    return not stack