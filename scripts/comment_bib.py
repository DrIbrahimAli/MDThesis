import re

citations = set()


with open('lit.tex','r') as texfile:
    for line in texfile:
        for cite in re.findall('citep\{.*?\}',line):
            citations.add(cite)

with open('lit.bib.bak','r') as ref:
    with open('lit.bib','w') as newref:
        content = ref.readlines()
        for line in content:
            if '@' in line:
                line = re.sub('@','%',line)
                for item in citations:
                    cit = item.split('{')[1].split('}')[0]
                    cit = 'article{'+cit+','
                    if cit in line:
                        line = re.sub('%','@',line)
                        break

            newref.write(line)

