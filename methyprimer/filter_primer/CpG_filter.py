
def CpG_filter(p3outfile,filter_primer_num,prefix):
	
	left_dict = dict()
	right_dict = dict()
	file = open(p3outfile)
	for line in file:
		line = line.strip()
		if line.startswith("SEQUENCE_ID"):
			nothing,name = line.split("=")
			left_dict[name] = ''
			right_dict[name] = ''
		if 'PRIMER_LEFT' and '_SEQUENCE' in line:
			nothing,sequence = line.split("=")
			left_dict[name] += sequence
			left_dict[name] += "\t"
		if 'PRIMER_RIGHT' and '_SEQUENCE' in line:
			nothing,sequence = line.split("=")
			right_dict[name] += sequence
			right_dict[name] += "\t"
	
	left_new_line = ''
	for k,v in left_dict.items():
		primers = v.split()
		CG_num_dict = dict()
		CG_num_count_dict = dict()
		for primer in primers:
			CG_num = primer.count('CG')
			if CG_num not in CG_num_dict:
				CG_num_dict[CG_num] = primer
			else:
				CG_num_dict[CG_num] += "\t"
				CG_num_dict[CG_num] += primer
			if CG_num not in CG_num_count_dict:
				CG_num_count_dict[CG_num] = 1
			else:
				CG_num_count_dict[CG_num] += 1
		
		final_primer_dict = dict()
		if CG_num_count_dict[0] >= filter_primer_num:
			final_primer_dict[k] = CG_num_dict[0].split()[0:5]
		elif CG_num_count_dict[0] + CG_num_count_dict[1] >= filter_primer_num:
			final_primer_dict[k] = CG_num_dict[0].split()[0:CG_num_count_dict[0]]
			final_primer_dict[k] += CG_num_dict[1].split()[0:filter_primer_num-CG_num_count_dict[0]]
		else:
			pass
		
		for key,value in final_primer_dict.items():
			print key,value
			new_key = '>' + key + '_forward'
			for each_primer in value:
				left_new_line += new_key
				left_new_line += "\n"
				left_new_line += each_primer
				left_new_line += "\n"

	right_new_line = ''
	for k,v in right_dict.items():
		primers = v.split()
		CG_num_dict = dict()
		CG_num_count_dict = dict()
		for primer in primers:
			CG_num = primer.count('CG')
			if CG_num not in CG_num_dict:
				CG_num_dict[CG_num] = primer
			else:
				CG_num_dict[CG_num] += "\t"
				CG_num_dict[CG_num] += primer
			if CG_num not in CG_num_count_dict:
				CG_num_count_dict[CG_num] = 1
			else:
				CG_num_count_dict[CG_num] += 1

		final_primer_dict = dict()
		if CG_num_count_dict[0] >= filter_primer_num:
			final_primer_dict[k] = CG_num_dict[0].split()[0:5]
		elif CG_num_count_dict[0] + CG_num_count_dict[1] >= filter_primer_num:
			final_primer_dict[k] = CG_num_dict[0].split()[0:CG_num_count_dict[0]]
			final_primer_dict[k] += CG_num_dict[1].split()[0:filter_primer_num-CG_num_count_dict[0]]
		else:
			pass

		for key,value in final_primer_dict.items():
			new_key = '>' + key + '_reverse'
			for each_primer in value:
				right_new_line += new_key
				right_new_line += "\n"
				right_new_line += each_primer
				right_new_line += "\n"
	
	filter_CpG_primer = prefix + ".filter_CpG.primer.txt"
	f = open(filter_CpG_primer,'w')
	f.write(left_new_line)
	f.write(right_new_line)
	f.close

	return filter_CpG_primer

if __name__ == "__main__":
	CpG_filter(p3outfile,filter_primer_num,prefix)
