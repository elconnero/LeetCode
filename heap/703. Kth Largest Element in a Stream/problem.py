import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k  # store the heap and k
        heapq.heapify(self.minHeap)     # convert nums into a min heap
        while len(self.minHeap) > k:    # trim heap down to size k
            heapq.heappop(self.minHeap) # boot out the smallest elements

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)          # push new value in
        if len(self.minHeap) > self.k:             # if heap grew too big
            heapq.heappop(self.minHeap)            # boot out the smallest
        return self.minHeap[0]                     # top is always Kth largest

        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

obj = KthLargest(3, [4, 5, 8, 2])
print(obj.add(3))   # expected 4
print(obj.add(10))  # expected 5
print(obj.add(1))   # expected 5