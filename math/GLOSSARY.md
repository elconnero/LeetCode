# Math

## Overview
Problems requiring mathematical concepts, number theory, or arithmetic manipulation rather than complex data structures.

## Common Topics
- **Modular Arithmetic** - Operations under modulo (often 10^9 + 7)
- **Prime Numbers** - Sieve of Eratosthenes, primality tests
- **GCD/LCM** - Euclidean algorithm
- **Bit Manipulation** - AND, OR, XOR, shifts
- **Combinatorics** - Permutations, combinations, Pascal's triangle

## Useful Formulas
| Concept | Formula |
|---------|---------|
| GCD | gcd(a, b) = gcd(b, a % b) |
| LCM | lcm(a, b) = (a * b) / gcd(a, b) |
| Sum 1 to n | n * (n + 1) / 2 |
| Power of 2 check | n & (n - 1) == 0 |

## Bit Manipulation Tricks
- `x & 1` - Check if odd
- `x >> 1` - Divide by 2
- `x << 1` - Multiply by 2
- `x ^ x = 0` - XOR with self is 0
- `x ^ 0 = x` - XOR with 0 is x

## Common Problems
- Reverse Integer
- Palindrome Number
- Power of Three
- Count Primes
- Single Number (XOR)
