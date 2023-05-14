import re
fozjeslua ={'ahisgfpw': 'def', 'tfutike': 'a(x):', 'nwpiafqlpb': 'for', 'ieltpc': 'i', 'ptzsnhnhb': 'in', 'sxeyrmcoef': 'range(1,x+1):', 'xmwirm': 'print(i)', 'jvhptiy': 'a(10)'}
code=  """ahisgfpw tfutike
    nwpiafqlpb ieltpc ptzsnhnhb sxeyrmcoef
        xmwirm

jvhptiy
"""
(lambda: exec(re.compile('|'.join(map(re.escape, fozjeslua.keys()))).sub(lambda match: fozjeslua[match.group(0)], code)))()
