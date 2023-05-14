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
twcszpdk=(lambda cipher_dict, key: {k: ''.join([chr((ord(v[i]) - ord(key[i % len(key)])) % 256) for i in range(len(v))]) for k, v in cipher_dict.items()})({'auzyhds': 'ÊÌÓ', 'gdcdbjvuv': 'Ç\x8få\x9e³', 'wzrsmqm': 'ÌÖß', 'ndzzmhaon': 'Ï', 'zjlsndzj': 'ÏÕ', 'lhcgaf': 'ØÈÛÜÞ\x8c\x93\x91ã\x96\x97\x97©', 'jdozjpiyp': 'ÖÙÖãí\x8cË\x8e', 'nzkrbkbqcm': 'Ç\x8f\x9e¥¢'},'fgmuydbekkfnowlp')
ptaxoyryue=  """auzyhds gdcdbjvuv
    wzrsmqm ndzzmhaon zjlsndzj lhcgaf
        jdozjpiyp
nzkrbkbqcm
"""
(lambda: exec(re.compile('|'.join(map(re.escape, twcszpdk.keys()))).sub(lambda match: twcszpdk[match.group(0)], ptaxoyryue)))()
```
