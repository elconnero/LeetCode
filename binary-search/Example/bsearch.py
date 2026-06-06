#itterative 
# Lets see if I can do it.

def binary_search(sequence: List[int], target: int) -> int:
    
    if not sequence: return 0

    left, right = 0, len(sequence) - 1

    while left < right:

        midpoint = (left + right) // 2
        midpoint_value = sequence[midpoint]

        if midpoint_value == target: return target
        elif midpoint_value < target: left = midpoint_value - 1
        elif midpoint_value > target: right = midpoint_value + 1

seq = [1,2,3,4,5,6,7,8,9,10]
target = 4

print(binary_search(seq, target))