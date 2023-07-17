"""
Task11.

# #############################################################################
# write generator function that has as input some range value and chunk_size
# produces output as lists with len == chunk size
# Example:
# Call:  chunk_generator(range(11), chunk_size=3) ->
# Output:  [0, 1, 2]
#          [3, 4, 5]
#          [6, 7, 8]
#          [9, 10]
# #############################################################################
"""


def chunk_generator(input_range, chunk_size):
    """
    Write Generator function.

    Args:
        input_range:range(n)
        chunk_size:int
    Yields:
        lists
    """
    nl = len(input_range)
    matrix = [
        [jl for jl in range(il, il + 3) if jl < nl]
        for il in range(0, nl, chunk_size)
    ]
    for it in matrix:
        yield it


input_range = range(11)
list_of_lists = list(chunk_generator(input_range, 3))
for row in list_of_lists:
    print(row)
