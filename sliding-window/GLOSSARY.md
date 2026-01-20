# Sliding Window

## Overview
Technique for problems involving contiguous subarrays/substrings. Maintain a "window" that slides through the data, updating state incrementally.

## Types
- **Fixed Size** - Window size is given (k elements)
- **Variable Size** - Window expands/contracts based on condition

## Common Patterns
- **Expand then shrink** - Grow until invalid, shrink until valid
- **Hash map tracking** - Count characters/elements in window
- **Running sum/product** - Maintain aggregate as window moves

## Template (Variable Size)
```
left = 0
for right in range(len(arr)):
    # Add arr[right] to window
    while window_invalid:
        # Remove arr[left] from window
        left += 1
    # Update result
```

## Time Complexity
O(n) - Each element is added and removed at most once

## Common Problems
- Maximum Sum Subarray of Size K
- Longest Substring Without Repeating Characters
- Minimum Window Substring
- Permutation in String
- Fruit Into Baskets
