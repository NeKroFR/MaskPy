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
print(1+1)
```
<ins>After:</ins>
```py
import re
swap ={'osuwtxq': 'print(1+1)'}
code=  """osuwtxq
"""
(lambda: exec(re.compile('|'.join(map(re.escape, swap.keys()))).sub(lambda match: swap[match.group(0)], code)))()
```
