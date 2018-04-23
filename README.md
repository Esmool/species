Single Species Pedigree Simulation & Analysis
===

This is a set of programs to simulate & to analysis the pedigree of an agamogenesis species with population restriction and birth control.

The primary goal of these programs is to investigate the pedigree of single individuals and their descendant, to reform the diagraph of evolution in micro view port.

All program are standalone, need to run under Python 2/3.

# Usage

First, open the DOS prompt of windows, or loggin to the terminal of linux. Change current path to this project root. Support it is __SPECIES_DIR__, run command
```
	cd SPECIES_DIR
```

## simluate.py

To create simulate result, run command
```
	python simulate.py GENERATIONS POPULATION BIRTH_CONTROL OUTPUT_PATH
```

The parameters above are
* __GENERATION__	the total generations to simulate
* __POPULATION__	population of each generation, better not larger then 26, as each individual of the species is denoted by one latin character.
* __BIRTH_CONTROL__ max children of each individual could have
* __OUTPUT_PATH__	output file path relative to current path

The pedigree output reads like this (simluated using parameters 3 5 3)
```
	 A  B  C  D  E
	BA CB DC DD EE
	BA BB CC DD EE
```

Each line of the pedigree indicates each generation, combined with individuals using white space to seperate. Every individual is denoted with no more then two upper case latin characters. The first one points to its parent in last generation, and the second one denote the individual itself in this generation. Individuals of the first generation have no parent, so they are only presented by one character.

As to the above example, the first generation individuals are named 'A', 'B', ..., 'E'. The second generation individuals are 'BA', 'CB', ..., 'EE'. Where 'BA' means parent of 'A' of this generation is the individual 'B' of the last generation, the ' A' in the first line. And the third line's 'BB' means the parent of the individual 'B' of the third generation 'B' of the second generation, which 'CB' in the second line.

The diagram of the pedigree illustrated above can be displayed by Graphviz using script
```
digraph G {
	A1
	BA2 -> B1
	BA3, BB3 -> CB2 -> C1
	CC3 -> DC2 -> D1
	DD3 -> DD2 -> D1
	EE3 -> EE2 -> E1
}
```
Here the number append to each individual indicates its generation. The arrow indicates the individual's parent.

## trace.py

To analysis the pedigree of simulated results, use trace.py by command
```
	python trace INPUT_DATA_FILE HIST_OUTPUT_FILEPATH GENERATION_COUNT_OUTPUT_FILEPATH
```

The parameters above are
* __INPUT_DATA_FILE__	the file simulate.py created
* __HIST_OUTPUT_FILE__	output file path relative to current path, which will store the histogram of generation counts of each individual that last
* __GENERATION_COUNT_OUTPUT_FILE__	output file path relative to current path, which will store the genartion counts of ech individual that last

The output of histogram has several lines of data, each line has two numbers. The first number is the generations of descendant that lives, and the second number is how many individuals have such descendant lives.

The output of generation counts has the same matrix structure as output of simulate.py. Each line is one generation, and each number in line indicate on individual, the number itself is the max generation of descendant lives of curresponding individual of the INPUT_DATA_FILE.

## build.bat

Use build.bat you can batchly simulate a series of different parameters, see detail in it, you will know how to use it. It can only run in windows.

## clean.bat

Use clean.bat you can delete all the output data files that build.bat created. Also used only in windows.

# Model Hypothesis

This evolution model uses hypothesis list below:
* Popluation of each generation is fixed;
* Children of each individual is no more than the the birth control value speciefied;
* Each of the individuals has the same oppunity to birth a child under the restrictions of the above two hypothesis.

# Simluate Alogrithm
The generate of next generation is simluated using alogrithm below:
1. for each individuals of current generation, assign a random number sampled from uniform distribution in (0, 1);
1. find the individual with assigned number larger than given threshold CUT (0.5 used), to simluate the fact '__not all individuals in one generation may have children__';
1. sort the individuals by the assigned numbers, to simluate the competition fact using form '__births of the children are proceed in turn, the former will occupy the living resoures the first, the latter only have to occupy the rest__'.
1. give birth of the next generation individuals by the order of their parents sorted above. Unless one parent reaches its max children limit, who will be skipped from birthing new child. And if the population of next generation is full filled, the birth process will immediately terminated.
1. if the population of next generation is not full filled after the above steps, repeat the alogrithm from beginning to continue give birth of next generation.

