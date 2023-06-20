"""The English language has five vowels: A, E, I, O, and U.

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

poem_text_lower=poem_text.lower()
for vowel in poem_text_lower:
    count_a=poem_text_lower.count('a')
    count_e=poem_text_lower.count('e')
    count_i=poem_text_lower.count('i')
    count_o=poem_text_lower.count('o')
    count_u=poem_text_lower.count('u')
dict1={'a': count_a, 'e': count_e, 'i': count_i, 'o': count_o, 'u': count_u}
print('-' * SEP_NUM)
print(f"| {'vowel':^5} | {'count':^8} |")
print('-' * SEP_NUM)
for vowel, count in dict1.items():
    print(f'| {vowel:<5} | {count:^8} |')
print('-' * SEP_NUM)
for vow, replacement in replacements.items():
    poem_text = poem_text.replace(vow, replacement)
print(poem_text)
