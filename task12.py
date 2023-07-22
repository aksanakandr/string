"""

Task12.

# Given list of list of list etc of integers
# write recursive function that will accept as argument target list
# and return sum of all integers inside it
# Input: [[[[1, 4, 5], [[6, 9],[[[8, 1], 7], 3], 2], 7], 5, 2], 9, [1, 2]]
# Output: Target sum = 72
"""


def sum_recursive(target_l):
    """
    Write recursive function.

    Args:
        target_l:list

    Returns:
        sum of elements

    """
    stack = [target_l]
    result = []
    while stack:
        current = stack.pop()
        if isinstance(current, list):
            stack.extend(current[::-1])
        else:
            result.append(current)
    total = 0
    for element in result:
        if (type(element) == type([])):
            total = total + sum_recursive(element)
        else:
            total = total + element
    return total


target_l = [[[[1, 4, 5], [[6, 9], [[[8, 1], 7], 3], 2], 7], 5, 2], 9, [1, 2]]
flat_list = sum_recursive(target_l)
print(flat_list)
