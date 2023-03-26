import re
import sys, random, string
def gui():
    banner = """\033[92m
  __  __           _    _____       
 |  \/  |         | |  |  __ \      
 | \  / | __ _ ___| | _| |__) |   _ 
 | |\/| |/ _` / __| |/ /  ___/ | | |
 | |  | | (_| \__ \   <| |   | |_| |
 |_|  |_|\__,_|___/_|\_\_|    \__, |
                               __/ |
                              |___/ """
    print(banner)
    filename = input("""\033[1;35mDrag the file to be obfuscated here : \033[0m""")
    if filename[0] == filename[-1]:
        if filename[0] == "'" or filename[0] == '"':
            filename = filename[1:-1]

    return filename

def open_file(filename):
    if filename[-3:] != ".py":
        print("\033[91mError: \033[0myou need to choose a python file!")
        sys.exit()
    try:
        f = open(filename, "r", encoding='utf-8')
        content = f.read()
        cuted_file = content.splitlines()
        return cuted_file 
    except:
        print("\033[91mError: \033[0mfile doesn't exist!")
        sys.exit()

def save_file(code, filename):
    f = open(filename, "w",encoding="utf-8")
    f.write(code)
    print("\033[1;32mSuccess:\033[0m the file has been successfully obfuscated")

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

    # Reverse keys and values ​​in swap
    swap = {v: k for k, v in swap.items()}
    return "import re\nswap ="+str(swap) + '\ncode=  """'+''.join(obfuscated_code)+ '"""'+"\n(lambda: exec(re.compile('|'.join(map(re.escape, swap.keys()))).sub(lambda match: swap[match.group(0)], code)))()"


if __name__ == "__main__":
    a = len(sys.argv)
    if a == 1:
        filename = gui()
        obfuscated_filename = filename[:-3]+"_obfuscated.py"        
    elif a == 2:
        filename = sys.argv[1]
        obfuscated_filename = filename[:-3]+"_obfuscated.py"
    elif a == 3:
        filename = sys.argv[1]
        obfuscated_filename = sys.argv[2]
    else:
        print("Error: too many arguments")
        exit()
    obfuscated = obfuscate(open_file(filename))
    save_file(obfuscated, obfuscated_filename)
