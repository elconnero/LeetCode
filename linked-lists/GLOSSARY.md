# Linked Lists

## Overview
Linear data structure where elements are stored in nodes, each pointing to the next. Allows efficient insertion/deletion but no random access.

## Types
- **Singly Linked** - Each node points to next
- **Doubly Linked** - Nodes point to both next and previous
- **Circular** - Last node points back to first

## Common Patterns
- **Two Pointers (Fast/Slow)** - Cycle detection, finding middle
- **Dummy Head** - Simplifies edge cases for insertion/deletion
- **Reversal** - Iterative or recursive list reversal

## Key Operations
| Operation | Time Complexity |
|-----------|-----------------|
| Access by index | O(n) |
| Insert at head | O(1) |
| Insert at tail | O(n) or O(1) with tail pointer |
| Delete node | O(1) if node given, O(n) to find |

## Common Problems
- Reverse Linked List
- Merge Two Sorted Lists
- Linked List Cycle
- Remove Nth Node From End
- Add Two Numbers
