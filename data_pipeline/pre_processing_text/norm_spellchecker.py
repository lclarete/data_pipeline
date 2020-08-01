"""
SPELL CHECKING is a quite helpful procedure to normalize the text.
The normalization process is made before cleaning stopwords,
and vectorization. 

For now, I'll use this file as a sandbox, but not implement it
in the pipeline. The results were not encoraging so far.


# pyspellchecker: https://pypi.org/project/pyspellchecker/

I've tested pyspellchecker using the following code. 
However, the results I got were useful. I tried "you're", 
and the checker returned "you'se" as a correction.

# spell correction for Portuguese
# https://github.com/samuelhei/spell-corrector-pt/blob/master/spell_corrector_pt/__init__.py

"""


# pyspellchecker is different from spellchecker
# the following code refers to pyspellchecker

# from spellchecker import SpellChecker

s = 'tests test'

spell = SpellChecker()
misspelled = spell.unknown(s_clean.split())

d = {}

for w in misspelled:
    print(spell.correction(w))
    corrections = spell.candidates(w)
    print(spell.candidates(w))
    d[w] = corrections

