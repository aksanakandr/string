"""
Task7.

# Convert a non-negative integer num to its English words representation.
# Example 1:
# Input: num = 123
# Output: "One Hundred Twenty Three"

# let's take that number always > 100 and only three digits
# 100 <= num <= 999
"""
num = 123
ones = [
  '', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine',
  'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen',
  'Seventeen', 'Eighteen', 'Nineteen',
]

tens = [
  '', '', 'Twenty', 'Thirty', 'Forty', 'Fifty',
  'Sixty', 'Seventy', 'Eighty', 'Ninety',
]
teens = [
   'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen',
   'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen',
]
if num == 0:
    print('Zero')
number_string = ''
if num >= 100:
    number_string += ones[num // 100] + ' Hundred '
    num %= 100
if num >= 20:
    number_string += tens[num // 10] + ''
    num %= 10
elif num >= 10:
    number_string += teens[num - 10]
    print(number_string)
if num > 0:
    number_string += ones[num]
print(number_string)
