#!/usr/bin/env python3

"""
splitFunctionalAndNonfunctional.py

This script parses the status of each read in a lineage to separate
   out those that are functional and those that are from passenger alleles.

Usage: splitFunctionalAndNonfunctional.py [ -a lineageNotations.fa -f functionalLineages.fa -n nonfunctional.fa]

Options:
    -a --all lineageNotations.fa          All sequences with lineage notations.
                                             [default: output/sequences/nucleotide/<project>_allJ_unique_lineageNotations.fa]
    -f --func functionalLineages.fa       Where to save the representatives of functional lineages.
                                             [default: output/sequences/nucleotide/<project>_functionalLineages.fa]
    -n --nonf nonfunctional.fa            Where to save the representatives of nonfunctional lineages.
                                             [default: output/sequences/nucleotide/<project>_nonFunctionalLineages.fa]

Created by Larissa K. Ault 2018-07-11.
Renamed, added functionality, and documented by Chaim A. Schramm 2018-08-30.
Altered to run before 5.1 and discard bad reads from functional lineages by CAS 2018-08-31

Copyright (c) 2011-2018 Vaccine Research Center, National Institutes of Health, USA. All rights reserved.

"""

import sys, re
from docopt import docopt
from Bio import SeqIO
try:
	from sonar import *
except ImportError:
	find_SONAR = sys.argv[0].split("sonar/utilities")
	sys.path.append(find_SONAR[0])
	from sonar import *

#parse arguments	
arguments = docopt(__doc__)
for arg in arguments:
	arguments[arg] = re.sub("<project>",fullpath2last_folder(os.getcwd()),arguments[arg])

#log command line
logCmdLine(sys.argv)


#parse lineages
lineages = dict()
reads    = dict()
for sequence in SeqIO.parse( open(arguments['--all'], "rU"), "fasta" ):
	info = re.search("status=(\\S+).*lineage_rep=(\\d+) lineage_size=(\\d+)", sequence.description)
	if info:
		reads[sequence.id] = { 'status':info.group(1), 'rep':info.group(2) }
		if info.group(2) not in lineages:
			if info.group(1) == "nonproductive":
				lineages[info.group(2)] = "nonproductive"
			else:
				lineages[info.group(2)] = "functional"
		if info.group(1) == "nonproductive":
			if lineages[info.group(2)] == "functional":
				lineages[info.group(2)] = "discard"
		elif lineages[info.group(2)] == "nonproductive":
			lineages[info.group(2)] = "discard"
	else:
		#shouldn't happen, but this prevents unexplained KeyErrors from crashing the script
		print("Warning, could not find status and lineage annotations for sequence %s" % sequence.id)
		reads[sequence.id] = { 'status':None, 'rep':sequence.id }
		lineages[sequence.id] = "discard"

		
#now do output
with open(arguments['--func'], "w") as fHandle:
	SeqIO.write( [ s for s in SeqIO.parse(open(arguments['--all'], "rU"), "fasta") if reads[s.id]['status']=="good" and lineages[reads[s.id]['rep']]=="functional" ], fHandle, "fasta" )

with open(arguments['--nonf'], "w") as nHandle:
	SeqIO.write( [ s for s in SeqIO.parse(open(arguments['--all'], "rU"), "fasta") if lineages[reads[s.id]['rep']]=="nonproductive" ], nHandle, "fasta" )
