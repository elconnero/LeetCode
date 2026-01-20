# Dynamic Programming

## Overview
Optimization technique that solves complex problems by breaking them into overlapping subproblems. Store solutions to avoid redundant computation.

## Approaches
- **Top-Down (Memoization)** - Recursive with caching
- **Bottom-Up (Tabulation)** - Iterative, building up solutions

## Common Patterns
- **1D DP** - Single array/variable tracking state
- **2D DP** - Grid-based or two-sequence problems
- **State Machine** - Problems with distinct states (buy/sell stock)
- **Interval DP** - Subproblems defined by ranges

## How to Identify DP Problems
1. Optimal substructure - Optimal solution uses optimal sub-solutions
2. Overlapping subproblems - Same subproblems solved multiple times
3. Keywords: "minimum", "maximum", "count ways", "is it possible"

## Common Problems
- Climbing Stairs
- Coin Change
- Longest Increasing Subsequence
- Edit Distance
- House Robber
