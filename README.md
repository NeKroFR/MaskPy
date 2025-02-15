# MaskPy

MaskPy is a python code obfuscator made in python.

You can find the desobfuscator [here](https://github.com/NeKroFR/Maskpy-was-a-joke).

# ⚠️ Disclaimer ⚠️
This version of MaskPy is not secure and is easy to reverse.
For a more robust and secure obfuscator, please check out at [MaskPy2](https://github.com/NeKroFR/Maskpy2).


# Installation

```
git clone https://github.com/NeKroFR/MaskPy.git
cd MaskPy
pip3 install requirements.txt
```

## Before:
```py
def a(x):
    for i in range(1,x+1):
        print(i)
a(10)
```
## After:
```py
from re import compile as oatoejce,escape as welgsofzrw
kbekmqt=(lambda qpnmoqozwe, kggwqvk: {k: ''.join([chr((ord(v[i]) - ord(kggwqvk[i % len(kggwqvk)])) % 256) for i in range(len(v))]) for k, v in qpnmoqozwe.items()})({'tsdiok': 'ÑÉß', 'ixzocvex': 'Î\x8cñ\x9f¥', 'vkptszsmi': 'ÓÓë', 'ifsfhmwx': 'Ö', 'sfckrsk': 'ÖÒ', 'nlbakerd': 'ßÅçÝÐ¡ª\x8eæ¡\x9d\x90£', 'vuxhhl': 'ÝÖâäß¡â\x8b', 'jszzsw': 'Î\x8cª¦\x94'},'mdyvkyybnvlgiirc')
zanslxdsfd=  """tsdiok ixzocvex\n    vkptszsmi ifsfhmwx sfckrsk nlbakerd\n        vuxhhl\njszzsw\n"""
(lambda: exec(oatoejce('|'.join(map(welgsofzrw, kbekmqt.keys()))).sub(lambda match: kbekmqt[match.group(0)], zanslxdsfd)))()
```
