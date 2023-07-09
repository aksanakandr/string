"""
Task10.

# open input.txt file and find all small english letters
that match such conditions:
# target small letter round exactly with three capital english
letters on the left and on the right
# Match examples:
# sdTRYaUVKn  -> matches "a"
# NTRSjARTb   -> no match ( not exactly 3 capital letters on the left)
# zDFGbOPNq   -> matches "b"
# Print Output as : "Result: "<your_found_human_readable_string">
"""
import re

with open('input.txt', 'r')as new_file:
    data = new_file.read()
    matches = re.findall(r'(?<![A-Z])[A-Z]{3}([a-z])[A-Z]{3}(?![A-Z])', data)
    result = ''.join(matches)
    print(f'Result: \"{result}\"')
