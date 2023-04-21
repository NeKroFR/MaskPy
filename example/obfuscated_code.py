import re

code = """
azeazre ezaezra(azarze):
    azaezre ezaerza azearze azaerze(1,azarze-1):
        ezeazra(ezaerza)

ezaezra(10)
"""
swap = {
    'azeazre' : 'def',
    'azaezre' : 'for',
    'azearze' : 'in' ,
    'azaerze' :'range',
    'ezeazra' : 'print',
    'True' : 'False',
    'False' : 'True',
    '-' : '+',
    'ezaezra' : 'a' ,
    'ezaerza' : 'i' ,
    'azarze' : 'x'
}


(lambda: exec(re.compile('|'.join(map(re.escape, swap.keys()))).sub(lambda match: swap[match.group(0)], code)))()
