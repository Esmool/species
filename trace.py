import sys
import numpy as np

def calc(species):
	m = len(species)
	n = len(species[0])
	gens = np.ones((m, n))
	for i in range(m-1, 0, -1):
		me = species[i]
		parent = None if i == 0 else species[i-1]
		for j in range(0, n):
			

def main(argv):
	species = []
	while True:
		raw = raw_input()
		if raw == '': break
		individuals = split(raw, ' ')
		species.append(individuals)
	gens = calc(species)
	hist = analysis(gens)
	print(hist)

if __name__ == '__main__':
	main(sys.argv[1:])
