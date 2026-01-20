# Binary Search

## Overview
Efficient search algorithm for sorted arrays. Repeatedly divides search space in half. O(log n) time complexity.

## Templates
- **Standard** - Find exact target
- **Left Bound** - Find first occurrence / insertion point
- **Right Bound** - Find last occurrence

## Common Patterns
- **Search in Rotated Array** - Modified binary search
- **Search on Answer** - Binary search on solution space
- **Peak Finding** - Find local maximum/minimum

## Key Points
- Always check for infinite loops (left <= right vs left < right)
- Careful with mid calculation: `mid = left + (right - left) // 2`
- Understand when to use `left = mid + 1` vs `left = mid`

## Time Complexity
| Operation | Complexity |
|-----------|------------|
| Standard binary search | O(log n) |
| Search on answer space | O(log(range) * verification) |

## Common Problems
- Binary Search
- Search in Rotated Sorted Array
- Find First and Last Position
- Search a 2D Matrix
- Koko Eating Bananas
