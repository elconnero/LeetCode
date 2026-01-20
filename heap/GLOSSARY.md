# Heap / Priority Queue

## Overview
Tree-based data structure where parent is always greater (max-heap) or smaller (min-heap) than children. Efficiently retrieves min/max element.

## Types
- **Min Heap** - Smallest element at root
- **Max Heap** - Largest element at root

## Common Patterns
- **Top K Elements** - Use heap of size K
- **Merge K Sorted** - Min heap for efficient merging
- **Two Heaps** - Find median (max heap + min heap)
- **Scheduling** - Process by priority

## Key Operations
| Operation | Complexity |
|-----------|------------|
| Insert | O(log n) |
| Extract min/max | O(log n) |
| Peek min/max | O(1) |
| Heapify array | O(n) |

## Language Notes
- Python: `heapq` (min heap by default, negate for max)
- Java: `PriorityQueue`
- C++: `priority_queue` (max heap by default)

## Common Problems
- Kth Largest Element
- Merge K Sorted Lists
- Find Median from Data Stream
- Top K Frequent Elements
- Task Scheduler
