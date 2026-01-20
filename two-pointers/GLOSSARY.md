# Two Pointers

## Overview
Technique using two indices to traverse data structure, often from opposite ends or at different speeds. Reduces O(n^2) brute force to O(n).

## Common Patterns
- **Opposite Direction** - Start from both ends, move toward center
- **Same Direction** - Fast and slow pointers
- **Sliding Window** - Maintain a range with two pointers

## When to Use
- Sorted array problems
- Finding pairs with certain sum/difference
- Removing duplicates in-place
- Palindrome verification
- Linked list cycle detection

## Key Points
- Usually requires sorted input for opposite direction
- Fast/slow works on unsorted data (linked lists)
- Often achieves O(1) extra space

## Time Complexity
| Pattern | Complexity |
|---------|------------|
| Opposite ends | O(n) |
| Fast/slow | O(n) |

## Common Problems
- Two Sum II (sorted)
- 3Sum
- Container With Most Water
- Trapping Rain Water
- Remove Duplicates from Sorted Array
