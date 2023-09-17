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
from re import compile as oatoejce,escape as welgsofzrw
kbekmqt=(lambda qpnmoqozwe, kggwqvk: {k: ''.join([chr((ord(v[i]) - ord(kggwqvk[i % len(kggwqvk)])) % 256) for i in range(len(v))]) for k, v in qpnmoqozwe.items()})({'tsdiok': 'ÑÉß', 'ixzocvex': 'Î\x8cñ\x9f¥', 'vkptszsmi': 'ÓÓë', 'ifsfhmwx': 'Ö', 'sfckrsk': 'ÖÒ', 'nlbakerd': 'ßÅçÝÐ¡ª\x8eæ¡\x9d\x90£', 'vuxhhl': 'ÝÖâäß¡â\x8b', 'jszzsw': 'Î\x8cª¦\x94'},'mdyvkyybnvlgiirc')
zanslxdsfd=  """tsdiok ixzocvex\n    vkptszsmi ifsfhmwx sfckrsk nlbakerd\n        vuxhhl\njszzsw\n"""
(lambda: exec(oatoejce('|'.join(map(welgsofzrw, kbekmqt.keys()))).sub(lambda match: kbekmqt[match.group(0)], zanslxdsfd)))()
```
# Performances

```
>>> python3 peformance_test.py 
Code executed in 8.406094551086426 seconds.
>> python3 peformance_test_obfuscated.py 
Code executed in 8.20453691482544 seconds.
```
The benchmarks says the obfuscated version run faster maybe it's because I run it after I don't know however it means that their is no big performances issues due to the fact it don't take much times to decode the code before executing it aproximativaly 0.0002951463063557943secs per keyword in the dict
