
def bisuffle_fasta(target_fasta):

	file = open(target_fasta)
	for line in file:
		line = line.strip()
		if line.startswith('>'):
			locs = line[1:]
			file_name = locs + '.fa'
			continue
		sequence = line.upper()
		CG_count = sequence.count('CG')
	if 
		
