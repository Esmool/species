function reform(data) {
	let getParentIndex = name => name.length == 1 ? null : name[0].charCodeAt() - 65;

	for (let i=0; i<data.length - 1; i++) {
		let parents = data[i];
		let subs = data[i + 1];
		for (let j=0; j<parents.length; j++) {
			let p = parents[j];
			let q = subs[j];

			let qParentIdx = getParentIndex(q.name);
			let qParent = parents[qParentIdx];

			if (typeof qParent.children === 'undefined')
				qParent.children = [];
			qParent.children.push(q);
			q.parent = qParent;

			if (typeof p.children === 'undefined')
				p.children = [];
		}
	}

	let first = data[0];
	let last = data[data.length - 1];
	for (let i=0; i<data[0].length; i++) {
		first[i].parent = null;
		last[i].children = [];
	}
}

function refresh(data) {
	let makeGeneration = generation => {
		let div = $('<div class="generation"></div>');
		for (var individual of generation) {
			let sDiv = makeIndividual(individual);
			div.append(sDiv);
		}
		return div;
	};

	let makeIndividual = individual => {
		let html = [];
		html.push(`<div class="individual cls${individual.clz==null?'':individual.clz}">`);
		html.push(`		<span class="name">${individual.name}</span>`);
		html.push(`		<br />`);
		html.push(`		${individual.lives}`);
		html.push(`</div>`);

		var div = $(html.join('\r\n'));
		div.data('individual', individual);

		div.on({
			mousedown: evt => alter(data, evt.currentTarget, evt.button, evt.ctrlKey, evt.shiftKey)
		});

		return div;
	};

	let container = $('.container');
	container.empty();
	for (let gen of data) {
		let div = makeGeneration(gen);
		container.append(div);
	}
}

function alter(data, div, mouseButton, ctrl, shift) {
	let digUp = (individual, clz) => {
		if (individual.parent == null)
			return;

		individual.parent.clz = clz;
		digUp(individual.parent, clz);
	};

	let digDown = (individual, clz) => {
		individual.clz = clz;
		let subs = individual.children || [];
		for (let s of subs)
			digDown(s, clz);
	};

	var individual = $(div).data('individual');

	let clz = individual.clz == null ? -1 : individual.clz;
	let dc = shift ? -1 : 1;
	switch (mouseButton) {
		case 2: clz = null; break;
		case 0: clz = (clz + dc + 10) % 10; break;
		default: break;
	}

	if (ctrl)
		digUp(individual, clz);
	digDown(individual, clz);
	refresh(data);
}