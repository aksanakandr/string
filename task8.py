"""
Task8.

# Given the list of integers ( positive , negative, zeros)
# Find max multiplication of three values in list
#l1 = [-7, 1, 2, 0, 3, 12, -24, 5, -1, 6]

# Input: [-1, 1, 2, 0, 3, 12, 4, 5, -1, 6]
# Output: Max value = "360". Nums are: (12, 5, 6)

# Input: [-7, 1, 2, 0, 3, 12, -24, 5, -1, 6]
# Output: Max value = "2016". Nums are: (-7, 12, -24)
"""
l1 = [-7, 1, 2, 0, 3, 12, -24, 5, -1, 6]
l1.sort()
nl = len(l1)
nl2 = l1[0]*l1[1]*l1[nl-1]
nl3 = l1[nl-1]*l1[nl-2]*l1[nl-3]
l2 = (max(nl2, nl3))
if l2 == nl2:
    al = (l1[0], l1[1], l1[nl-1])
else:
    al = (l1[nl-1], l1[nl-2], l1[nl-3])
print(f'Max value = {str(l2)} . Nums are: {al}')
