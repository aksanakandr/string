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
l2=l1[:]
l2.sort()
list_len = len(l2)
multi_case1 = l2[0] * l2[1] * l2[list_len - 1]
multi_case2 = l2[list_len-1]*l2[list_len-2]*l2[list_len-3]
max_mul = (max(multi_case1, multi_case2))
if max_mul == multi_case2:
    nums = (l2[0], l2[1], l2[list_len-1])
else:
    nums = (l2[list_len-1], l2[list_len-2], l2[list_len-3])
print(f'Max value = {str(max_mul )} . Nums are: {nums}')
