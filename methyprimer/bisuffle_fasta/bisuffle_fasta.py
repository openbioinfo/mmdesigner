
 

def bisuffle_fasta(filter_primer,prefix):
	
	new_line = ''
	file = open(filter_primer)
	for line in file:
		if line.startswith('>'):
			new_line += line
			flag = line.split("_")[-1]
			flag = flag.strip()
			continue
		if flag == 'forward':
			primer = line.replace('CG','XX')
			primer = primer.replace('C','T')
			primer = primer.replace('XX','CG')
			primer = primer.replace('A','t').replace('C','g').replace('G','c').replace('T','a')
			primer = primer.upper()
			new_line += primer
			continue
		if flag == 'reverse':
			primer = line.replace('CG','XX')
			primer = primer.replace('G','A')
			primer = primer.replace('XX','CG')
			new_line += primer
			continue
	
	final_pre_primer = prefix + ".final_pre.primer.txt"
	f = open(final_pre_primer,'w')
	f.write(new_line)
	f.close

	return final_pre_primer

if __name__ == "__main__":
	bisuffle_fasta(filter_primer,prefix)
