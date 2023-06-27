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

vowel_counts = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
poem_text_lower = poem_text.lower()

for char in poem_text_lower:
    if char in vowel_counts:
        vowel_counts[char] += 1

sep_num = 20
print('-' * sep_num)
print(f"| {'vowel':^5} | {'count':^8} |")
print('-' * sep_num)

for vowel, count in vowel_counts.items():
    print(f'| {vowel:<5} | {count:^8} |')

print('-' * sep_num)

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
for vow, replacement in replacements.items():
    poem_text = poem_text.replace(vow, replacement)

print(poem_text)

