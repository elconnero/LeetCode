import heapq

# ---- MIN HEAP (default in Python) ----
min_heap = []
heapq.heappush(min_heap, 5)
heapq.heappush(min_heap, 1)
heapq.heappush(min_heap, 3)
heapq.heappush(min_heap, 2)

print(min_heap[0])           # peek at smallest: 1 (O(1))
print(heapq.heappop(min_heap))  # pop smallest: 1 (O(log n))
print(heapq.heappop(min_heap))  # pop smallest: 2 (O(log n))

# ---- HEAPIFY (convert existing list into a heap) ----
nums = [5, 3, 8, 1, 2]
heapq.heapify(nums)          # converts in place, O(n)
print(nums[0])               # 1, smallest is now at the top

# ---- MAX HEAP (negate values to simulate) ----
# Python only has min heap, so to get max heap negate all values
max_heap = []
heapq.heappush(max_heap, -5)
heapq.heappush(max_heap, -1)
heapq.heappush(max_heap, -3)

print(-max_heap[0])             # peek at largest: 5 (negate back)
print(-heapq.heappop(max_heap)) # pop largest: 5 (negate back)
print(-heapq.heappop(max_heap)) # pop largest: 3 (negate back)

# ---- GET N LARGEST / N SMALLEST ----
nums = [5, 3, 8, 1, 2, 9, 4]
print(heapq.nlargest(3, nums))   # [9, 8, 5] top 3 largest
print(heapq.nsmallest(3, nums))  # [1, 2, 3] top 3 smallest

# ---- HEAP WITH TUPLES (useful for priority queues) ----
# heapq sorts by first element of tuple
task_heap = []
heapq.heappush(task_heap, (3, "low priority task"))
heapq.heappush(task_heap, (1, "high priority task"))
heapq.heappush(task_heap, (2, "medium priority task"))

print(heapq.heappop(task_heap))  # (1, 'high priority task')
print(heapq.heappop(task_heap))  # (2, 'medium priority task')
print(heapq.heappop(task_heap))  # (3, 'low priority task')

# ---- SIZE OF HEAP ----
heap = [1, 2, 3]
heapq.heapify(heap)
print(len(heap))  # 3

# ---- CHECK IF EMPTY ----
print(len(heap) == 0)  # False
heap = []
print(len(heap) == 0)  # True

# Heaps are important because they give you instant access to the
# smallest or largest element in O(1) time. This is useful for problems
# where you repeatedly need the min or max of a changing dataset,
# like finding the top K elements, scheduling tasks by priority,
# or running median calculations. Without a heap you would have to
# sort the data every time which is O(n log n), but a heap lets you
# push and pop in O(log n) making it much more efficient.

# Heaps are mainly used with:
# - Top K Elements (find K largest/smallest elements in a dataset)
# - Sliding Window (find max/min element in every window)
# - Topological Sort (ordering tasks by priority)
# - Greedy Algorithms (always picking the min/max at each step)
# - Graph Algorithms like Dijkstra's shortest path (picking the lowest cost node)
