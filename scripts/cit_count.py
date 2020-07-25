#!/bin/python3

import re
from sys import argv
from collections import Counter


citations = re.findall('citep\{[\w\d]*\}',open(argv[1]).read().lower())
Counter(citations).most)_common(argv[2])
