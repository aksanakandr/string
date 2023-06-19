"""
# The English language has five vowels: A, E, I, O, and U
# Please count each vowel occurence in text bellow ( sum of lower and capital cases)
# and write output as table smth like this
# -----------------
# | vowel | count |
# -----------------
# |   a   |  11   |
# |   e   |  23   |
#   ...
# -----------------

# then modify text where each vowel replaced with
# A->À;  a->à ; E-> É ; e->é; I->Í , i->í ; O->Ó ; o->ó; U->Ú; u->ú
# ex. "Í wàndéréd lónély...."   and print it
"""


poem_text = """I wandered lonely as a cloud
That floats on high o'er vales and hills,
When all at once I saw a crowd,
A host, of golden daffodils;
Beside the lake, beneath the trees,
Fluttering and dancing in the breeze. 

Continuous as the stars that shine
And twinkle on the Milky Way,
They stretched in never-ending line
Along the margin of a bay:
Ten thousand saw I at a glance,
Tossing their heads in sprightly dance."""

SEP_NUM = 20
replacements = {
    'A': 'À',
    'a': 'à',
    'E': 'É',
    'e': 'é',
    'I': 'Í',
    'i': 'í',
    'O': 'Ó',
    'o': 'ó',
    'U': 'Ú',
    'u': 'ú'
}
vowels = ['a', 'e', 'i', 'o', 'u']
vowel_counts = {vowel: 0 for vowel in vowels}
for il in poem_text:
    if il.lower() in vowels:
        vowel_counts[il.lower()] += 1
print('-' * SEP_NUM)
print(f"| {'vowel':^5} | {'count':^8} |")
print('-' * SEP_NUM)
for vowel, count in vowel_counts.items():
    print(f'| {vowel:<5} | {count:^8} |')
print('-' * SEP_NUM)
for vow, replacement in replacements.items():
    poem_text = poem_text.replace(vow, replacement)
print(poem_text)

