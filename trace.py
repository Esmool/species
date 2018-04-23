import sys
import os
import string

def calc(species, m, n):
	gens = [ [0 for x in range(0, n)] for y in range(0, m) ]
	for i in range(1, m):
		gen = gens[m - i - 1]
		genSub = gens[m -i ]
		subs = species[m - i]
		for j in range(0, n):
			s = subs[j]
			sIndex = ord(s[1]) - 65
			parentIndex = ord(s[0]) - 65
			if gen[parentIndex] < genSub[sIndex] + 1:
				gen[parentIndex] = genSub[sIndex] + 1
	return gens

def analysis(gens, m, n):
	hist = []
	map = {}
	for i in range(0, m):
		gen = gens[i]
		for j in range(0, n):
			age = gen[j]
			record = None
			if not map.has_key(age):
				t = { 'age': age, 'count': 0 }
				map[age] = t
				hist.append(t)
			record = map[age]
			record['count'] = record['count'] + 1
			map[age] = record
	hist.sort(lambda x, y: x['age'] - y['age'])
	return hist

def outputHist(hist, m, n, fname):
	g = lambda x: '{:2>d} {:d}'.format(x['age'], x['count'])
	ss = '\r\n'.join(map(g, hist))
	fpath = os.path.abspath(fname)
	with open(fpath, 'w') as f:
		f.write(ss)

def outputGens(gens, m, n, fname):
	g = lambda x: '{:>3d}'.format(x)
	h = lambda x: ' '.join(map(g, x))
	ss = '\r\n'.join(map(h, gens))
	fpath = os.path.abspath(fname)
	with open(fpath, 'w') as f:
		f.write(ss)

def input(fname):
	species = []
	fpath = os.path.abspath(fname)
	with open(fpath, 'r') as f:
		for line in f.readlines():
			individuals = filter(lambda x: x != '', string.split(line.strip(), ' '))
			species.append(individuals)
	return species

def main(argv):
	fin = argv[0] if len(argv) > 0 else 'species.data'
	fhist = argv[1] if len(argv) > 1 else 'hist.data'
	fgens = argv[2] if len(argv) > 2 else 'gens.data'
	species = input(fin)
	m = len(species)
	n = len(species[0])
	gens = calc(species, m, n)
	hist = analysis(gens, m, n)
	outputHist(hist, m, n, fhist)
	outputGens(gens, m, n, fgens)

if __name__ == '__main__':
	main(sys.argv[1:])
