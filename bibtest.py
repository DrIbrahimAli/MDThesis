import sys

reffile= sys.argv[1]

with open(reffile,'r') as bib:
    i = 0
    for line in bib:
        i +=1
        if line.startswith('@'):
            with open(reffile,'r') as ref:
                x =0
                for LINE in ref:
                    x+=1
                    if line == LINE and not x==i:
                        print('duplicates entries at line' , i, 'and', x)
