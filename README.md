# MaskPy

MaskPy is a python code obfuscator made in python.

# Installation

```
git clone https://github.com/NeKroFR/MaskPy.git
cd MaskPy
pip3 install requirements.txt
```

# Layers

An obfuscator uses different layers to obfuscate the code and make it harder to understand.
For the moment, i only have one layer wich swap the keywords of the code and i'm working on making new layers.

**Keyword layer example:**

<ins>Before:</ins>
```py
def a(x):
    for i in range(1,x+1):
        print(i)
a(10)
```
<ins>After:</ins>
```py
import re
hgmwtabcm=(lambda cipher_dict, key: {k: ''.join([chr((ord(v[i]) - ord(key[i % len(key)])) % 256) for i in range(len(v))]) for k, v in cipher_dict.items()})({'pwznltyyrk': '×ÍÚ', 'abmjad': 'Ô\x90ì\x9a¬', 'bzqexcy': 'Ù×æ', 'rzfqfe': 'Ü', 'sohgdlrdwh': 'ÜÖ', 'kjmdyibnoz': 'åÉâØ×\x9d\x98\x98ì\x91ª¡\x9d', 'viiizbama': 'ãÚÝßæ\x9dÐ\x95', 'jgucggz': 'Ô\x90¥¡\x9b'},'shtqrugltfyxcbmv')
cfihjj=  """pwznltyyrk abmjad\n    bzqexcy rzfqfe sohgdlrdwh kjmdyibnoz\n        viiizbama\njgucggz\n"""
(lambda: exec(re.compile('|'.join(map(re.escape, hgmwtabcm.keys()))).sub(lambda match: hgmwtabcm[match.group(0)], cfihjj)))()
```
