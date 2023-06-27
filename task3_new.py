"""You have list of tuples.

Each tuple represents: name, age,
some sum, last name, sex.
# Please do such things:
# 1 - sort list by age and sex fields
# 2 - somehow you need to get new list as old list without first
# two elements and last two elements. Print this new list
# 3 - in new list calculate total numbers of "female"  and
# "male" and print it as small table.
# Example:
# -----------------
# | sex    | count |
# -----------------
# |  female |  11  |
# |   male  |  23  |
# -----------------

#  advice: female and male calculation can be done vs flat
list, or you can find your own approach ;)
"""
import itertools
from operator import itemgetter

SEP_NUM = 18
people = [
    ('Alice', 32, 100, 'Johnson', 'female'),
    ('Bob', 41, 200, 'Smith', 'male'),
    ('Charlie', 27, 150, 'Jones', 'male'),
    ('David', 52, 75, 'Williams', 'male'),
    ('Eve', 18, 300, 'Davis', 'female'),
    ('Frank', 33, 50, 'Taylor', 'male'),
    ('Grace', 42, 125, 'Clark', 'female'),
    ('Henry', 26, 225, 'Lewis', 'male'),
    ('Ivy', 38, 175, 'Moore', 'female'),
    ('Jack', 20, 140, 'Harris', 'male'),
    ('Kate', 37, 110, 'Miller', 'female'),
    ('Leo', 44, 90, 'Wilson', 'male'),
    ('Mae', 29, 180, 'Brown', 'female'),
    ('Nick', 51, 70, 'Davies', 'male'),
    ('Oliver', 18, 250, 'Collins', 'male'),
    ('Pete', 36, 160, 'Green', 'male'),
    ('Quinn', 20, 230, 'Bell', 'female'),
    ('Remy', 30, 120, 'Foster', 'male'),
    ('Sara', 28, 140, 'Baker', 'female'),
    ('Tom', 47, 80, 'Scott', 'male'),
    ('Ursula', 39, 135, 'Adams', 'female'),
    ('Vivian', 25, 190, 'Ross', 'female'),
    ('Wendy', 46, 90, 'Wright', 'female'),
    ('Xavier', 31, 105, 'Reed', 'male'),
    ('Yuliana', 22, 200, 'Lopez', 'female'),
    ('Zack', 48, 60, 'Mitchell', 'male'),
    ('Adam', 35, 75, 'Davis', 'male'),
    ('Bella', 27, 125, 'Smith', 'female'),
    ('Charlie', 44, 115, 'Johnson', 'male'),
    ('Daisy', 20, 215, 'Miller', 'female'),
    ('Ethan', 33, 100, 'Taylor', 'male'),
    ('Fiona', 40, 150, 'Jones', 'female'),
    ('George', 24, 180, 'Lewis', 'male'),
    ('Hannah', 22, 200, 'Williams', 'female'),
    ('Ivan', 29, 160, 'Brown', 'male'),
    ('Julie', 55, 90, 'Clark', 'female'),
    ('Kenny', 38, 140, 'Harris', 'male'),
    ('Luna', 55, 170, 'Smith', 'female'),
    ('Mike', 55, 55, 'Johnson', 'male'),
]
people.sort(key=itemgetter(1, 4))
people_new = people[2:-2]
print(people_new)
l2 = (list(itertools.chain.from_iterable(people_new)))
female_count = l2.count('female')
male_count = l2.count('male')
print('-' * SEP_NUM)
print(f"| {'sex':^5} | {'count':^7} |")
print('-' * SEP_NUM)
new_dict = {'female': female_count, 'male': male_count}
for female, male in new_dict.items():
    print(f'| {female:<6} |{male:^8}|')
print('-' * SEP_NUM)
