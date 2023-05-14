import re, random, string

def Vigenere(message, key):
    """
    Cipher str using the Vigenere cipher with a fixed key
    ---
    In:
        message <str> to be ciphered + key <str>
    Out:
        the ciphered str
    """
    key_len = len(key)
    cipher = []
    for i in range(len(message)):
        key_c = key[i % key_len]
        cipher_c = chr((ord(message[i]) + ord(key_c)) % 256)
        cipher.append(cipher_c)
    return ''.join(cipher)


def randkey(swap):
    """
    generate a random key wich isn't already in the swap dict
    """
    key =''.join(random.choices(string.ascii_lowercase, k=random.randint(6,10)))
    while key in swap.keys():
        key =''.join(random.choices(string.ascii_lowercase, k=random.randint(6,10)))
    return key

def get_indent(line):
    """
    return code line indent
    """
    indent = ''
    for chr in line:
        if chr == " ":
            indent += chr
        else:
            break
    return indent


def ciphkeys(dict: dict):
    """
    Cipher dico values
    ---
    In:
        dict
    Out:
        cipher dict, key to  decipher
    """
    key = "".join(random.choices(string.ascii_lowercase, k=16))
    dico = {}
    for k, v in dict.items():
        dico[k] = Vigenere(v,key)
    return dico, key

def obfuscate(code):
    swap = {}
    obfuscated_code = []
    for l in code:
        obf_line = []
        for word in l.split():
            if word in swap:
                obf_line.append(swap[word])
            else:
                key = randkey(swap)
                obf_line.append(key)
                swap[word] = key
        obfuscated_code.append(get_indent(l)+' '.join(obf_line)+"\n")
    swapname = randkey(swap)
    codename = randkey(swap)
    while codename == swapname:
        codename = randkey(swap)
    # Reverse keys and values ​​in swap + obfuscate the dict values
    swap, dictkey = ciphkeys({v: k for k, v in swap.items()}) 
    return "import re\n"+swapname+"=(lambda cipher_dict, key: {k: ''.join([chr((ord(v[i]) - ord(key[i % len(key)])) % 256) for i in range(len(v))]) for k, v in cipher_dict.items()})("+str(swap)+",'"+dictkey+"')\n"+codename+'=  """'+''.join(obfuscated_code)+ '"""'+"\n(lambda: exec(re.compile('|'.join(map(re.escape, "+swapname+".keys()))).sub(lambda match: "+swapname+"[match.group(0)], "+codename+")))()"
