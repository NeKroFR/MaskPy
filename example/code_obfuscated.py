import re
lvqlqu=(lambda jydfivpkn, jbtfkwfur: {k: ''.join([chr((ord(v[i]) - ord(jbtfkwfur[i % len(jbtfkwfur)])) % 256) for i in range(len(v))]) for k, v in jydfivpkn.items()})({'djrkoqhpx': 'ÜÛÒ', 'oratannnek': 'Ù\x9eä¢´', 'zzuwfu': 'ÞåÞ', 'yanalokq': 'á', 'uswonbrvvs': 'áä', 'qwyntpd': 'ê×Úàß\x9b\xa0¥ê¤\x9e¢®', 'zmtopmo': 'èèÕçî\x9bØ¢', 'qitpaotw': 'Ù\x9e\x9d©£'},'xvlyzsoyrymytzvt')
higmqcsg=  """djrkoqhpx oratannnek\n    zzuwfu yanalokq uswonbrvvs qwyntpd\n        zmtopmo\nqitpaotw\n"""
(lambda: exec(re.compile('|'.join(map(re.escape, lvqlqu.keys()))).sub(lambda match: lvqlqu[match.group(0)], higmqcsg)))()
