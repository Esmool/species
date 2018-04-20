
if (require.main == module) {
	var argv = process.argv.splice(2);
	main(argv);
}

const CUT = 0.5;

function main(argv) {
	var n = parseInt(argv[0] || 100);
	var limit = parseInt(argv[1] || 20);
	var maxChildren = parseInt(argv[2] || 3);
	var species = simulate(n, limit, maxChildren);
	var text = species.map(x => x.join(' ')).join('\r\n');
	console.log(text);
}

function simulate(n, limit, maxChildren) {
	var species = [];
	species.push(initCreate(limit));
	for (var i=0; i<n-1; i++)
		species.push(evolute(species[i], limit, maxChildren));
	return species;
}

function initCreate(limit) {
	var generation = [];
	for (var i=0; i<limit; i++)
		generation[i] = ' ' + String.fromCharCode(65 + i);
	return generation;
}

function evolute(generation, limit, maxChildren) {
	var children = {};
	var allChild = 0;

outter:
	while (true) {
		var list = [];
		for (var i=0; i<generation.length; i++) {
			list.push({
				index: i,
				value: Math.random()
			});
		}
		var toBirth = list.filter(x => x.value > CUT).sort((x, y) => y.value - x.value);
		for (var i=0; i<toBirth.length; i++) {
			var tb = toBirth[i];
			if (typeof children[tb.index] === 'undefined')
				children[tb.index] = 0;
			if (children[tb.index] == maxChildren) continue;
			children[tb.index]++;
			allChild++;
			if (allChild == limit) break outter;
		}
	}

	var nextGeneration = [];
	var j = 0;
	for (var i=0; i<generation.length; i++) {
		if (typeof children[i] === 'undefined') continue;
		var parent = generation[i].substr(generation[i].length - 1);
		var j0 = j;
		while (j - j0 < children[i])
			nextGeneration[j] = parent + String.fromCharCode(65 + j++);
	}

	return nextGeneration;
}
