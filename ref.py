import sys

fh = open(sys.argv[1], 'r')

for line in fh:

    info=line.split('.')
    # print(info)
    authors=info[0]
    # print(authors)
    # print(authors.split(', '))
    author=authors.split(',')[0]
    abbrev = author.split(' ')[0]
    title= info[1]
    journal=info[2]
    data=info[3]
    # print(data)
    reauthor= ''
    for author in authors.split(', '):
        *a, b = author.split(' ')
        reauthor = reauthor + b + ' ' + ' '.join(a) + ' and '
    authors = reauthor[:-5]
    year, data = data.split(',')
    volume, pages = data.split(':')
    abbrev = (abbrev + year).replace(' ','')
    print('@article{'+abbrev+',')
    print('\tauthor = {'+authors+'},')
    print('\ttitle = {'+title+'},')
    print('\tjournal = {'+journal+'},')
    print('\tyear = '+year+',')
    print('\tvolume = '+volume+',')
    print('\tpages = {'+pages+'},')
    print('}\n\n')
