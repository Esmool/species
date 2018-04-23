import sys
import os
import string
import json

class RTemplate(string.Template):
    delimiter = '@'

def input(fname):
	species = []
	fpath = os.path.abspath(fname)
	with open(fpath, 'r') as f:
		for line in f.readlines():
			individuals = filter(lambda x: x != '', string.split(line.strip(), ' '))
			species.append(individuals)
	return species

def buildData(species, gens, m, n):
    data = []
    for i in range(0, m):
        row = []
        spe = species[i]
        gen = gens[i]
        for j in range(0, n):
            row.append({
                'name': spe[j],
                'lives': gen[j]
            })
        data.append(row)
    return json.dumps(data)

def readTemplate(fname):
    fpath = os.path.abspath(fname)
    text = None
    with open(fpath, 'r') as f:
        text = f.read()
    return RTemplate(text)

def output(fname, html):
    fpath = os.path.abspath(fname)
    with open(fpath, 'w') as f:
        f.write(html)

def main(argc, argv):
    fspecies = argv[0] if len(argv) > 0 else 'species.data'
    fgens = argv[1] if len(argv) > 2 else 'gens.data'
    fout = argv[2] if len(argv) > 3 else 'index.html'
    ftemplate = argv[3] if len(argv) > 4 else 'index.rtl'
    species = input(fspecies)
    gens = input(fgens)
    template = readTemplate(ftemplate)

    m = len(species)
    n = len(species[0])
    data = buildData(species, gens, m, n)
    params = fspecies
    html = template.substitute(DATA=data, PARAMS=params)
    output(fout, html)

if __name__ == '__main__':
    av = sys.argv[1:]
    ac = len(av)
    main(ac, av)
