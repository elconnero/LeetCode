# Backtracking

## Overview
Algorithmic technique for finding all (or some) solutions by incrementally building candidates and abandoning ("backtracking") those that fail constraints.

## Template
```
def backtrack(candidate, state):
    if is_solution(candidate):
        output(candidate)
        return

    for choice in choices:
        if is_valid(choice):
            make_choice(choice)
            backtrack(candidate, state)
            undo_choice(choice)  # backtrack
```

## Common Patterns
- **Permutations** - All orderings of elements
- **Combinations** - All subsets of size k
- **Subsets** - All possible subsets (power set)
- **Constraint Satisfaction** - Sudoku, N-Queens

## Key Points
- Prune early - Skip invalid branches as soon as possible
- State restoration - Always undo changes after recursive call
- Avoid duplicates - Sort input and skip same elements

## Time Complexity
Often exponential: O(n!), O(2^n), or O(k^n)

## Common Problems
- Permutations
- Combinations
- Subsets
- N-Queens
- Word Search
- Sudoku Solver
