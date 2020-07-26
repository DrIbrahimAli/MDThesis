#!/bin/python3

import re
from sys import argv
from collections import Counter


citations = []
with open(argv[1],'r') as fh:
    for line in fh:
        if line.startswith('%'): continue
        citations += re.findall('citep\{[\w\d]*\}',line)

for x,y in Counter(citations).most_common(int(argv[2])):
    print('{} cited {} times'.format(x,y))
