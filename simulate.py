import random
import sys

CUT = 0.5

def simulate(n, limit, maxChildren):
	species = []
	firstGeneration = [' ' + chr(65 + i) for i in range(0, limit)]
	species.append(firstGeneration)
	for i in range(0, n-1):
		species.append(evolute(species[i], limit, maxChildren))
	return species

def evolute(generation, limit, maxChildren):
	children = {}
	allChild = 0

	outerLoop = True
	while outerLoop:
		list = [ { 'index': i, 'value': random.random() } for i in range(0, len(generation))]
		toBirth = filter(lambda x: x['value'] > CUT, list)
		toBirth.sort(lambda x, y: int(x['value'] - y['value']))
		for tb in toBirth:
			idx = tb['index']
			if not children.has_key(idx):
				children[idx] = 0
			if children[idx] == maxChildren:
				continue
			children[idx] += 1
			allChild += 1
			if allChild == limit:
				outerLoop = False
				break

	nextGeneration = []
	j = 0
	for i in range(0, limit):
		individual = generation[i]
		if not children.has_key(i):
			continue
		parent = individual[-1]
		j0 = j
		while j - j0 < children[i]:
			nextGeneration.append(parent + chr(65 + j))
			j += 1

	return nextGeneration

def main(argv):
	n = int(argv[0] if len(argv) > 1 else 100)
	limit = int(argv[1] if len(argv) > 2 else 20)
	maxChildren = int(argv[2] if len(argv) > 3 else 3)
	species = simulate(n, limit, maxChildren)
	text = '\r\n'.join(map(lambda x: ' '.join(x), species))
	print(text)

if __name__ == '__main__':
	main(sys.argv[1:])
