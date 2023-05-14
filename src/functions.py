import re, random, string

def randkey(swap):
    key =''.join(random.choices(string.ascii_lowercase, k=random.randint(6,10)))
    while key in swap.keys():
        key =''.join(random.choices(string.ascii_lowercase, k=random.randint(6,10)))
    return key

def get_indent(line):
    indent = ''
    for chr in line:
        if chr == " ":
            indent += chr
        else:
            break
    return indent


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
    # Reverse keys and values ​​in swap
    swap = {v: k for k, v in swap.items()}
    return "import re\n"+swapname+" ="+str(swap) + '\n'+codename+'=  """'+''.join(obfuscated_code)+ '"""'+"\n(lambda: exec(re.compile('|'.join(map(re.escape, "+swapname+".keys()))).sub(lambda match: "+swapname+"[match.group(0)], "+codename+")))()"
