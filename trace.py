import sys

def trace(lines):
	generations = []
	firstGeneration = [ record(0, x, None) for x in lines[0] ]
	n = len(lines)
	for i in range(0, n-1):
		generations.append(makeGeneration(i+1, generations[i], lines[i+1]))
	return generations

def makeGeneration(gId, pGeneration, sLine):
	list = []
	codes = sLine.split(' ')
	for code in sLine:
		pCode = code[1]
		# TODO:

def record(gId, individual, parent):
	return {
		'generation': gId,
		'individual': individual,
		'parent': parent,
		'descendantLives': 0,
		'children': []
	}

def main(argv):
	lines = []
	while True:
		raw = raw_input()
		if raw == '': break
		lines.append(raw)
	trace(lines)

if __name__ == '__main__':
	main(sys.argv[1:])
