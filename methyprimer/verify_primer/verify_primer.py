

def verify_primer(final_pre_primer,formatOut,prefix):
	
	primer_dict = dict()
	file = open(final_pre_primer)
	for line in file:
		if line.startswith(">") and 'F' in line:
			key = line.split(">")[1].split("_F")[0]
			value = line
			primer_dict[key] = ''
			continue
		value += line
		primer_dict[key] = value
	
	verify_file = ''
	fout = open(formatOut)
	for line in fout:
		flist = line.split()
		del(flist[-1])
		for i in flist:
			verify_file += primer_dict[i]
	
	verify_out = prefix + ".verify.fa" 
	f = open(verify_out,'w')
	f.write(verify_file)
	f.close

	return verify_out

if __name__ == "__main__":
	verify_primer(final_pre_primer,formatOut,prefix)
