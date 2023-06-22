"""
Hometask4.

we have four values w,x,y,z.
write if-elif-else statement that will search
minimum value and print smth aka "'y' is minimum value'
advice use python debugger and different values to check your algorithm
"""
TEMPLATE = '{} is minimum value'
wl, xl, yl, zl = 100, 200, 40, 300
if wl <= xl and wl <= yl and wl <= zl:
    print(TEMPLATE.format('w'))
elif xl <= wl and xl < yl and xl <= zl:
    print(TEMPLATE.format('x'))
elif yl <= wl and yl <= xl and yl <= zl:
    print(TEMPLATE.format('y'))
elif zl <= wl and zl <= xl and zl <= yl:
    print(TEMPLATE.format('z'))
