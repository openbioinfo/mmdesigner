
def CpG_filter(p3outfile,prefix):
	
	candidate_primer_num = 10
	primer_dict = dict()
	file = open(p3outfile)
	for line in file:
		line = line.strip()
		if line.startswith("SEQUENCE_ID"):
			nothing,name = line.split("=")
			primer_dict[name] = ''
		if 'PRIMER_LEFT' in line and '_SEQUENCE' in line:
			nothing,sequence_f = line.split("=")
			primer_dict[name] += sequence_f
			primer_dict[name] += "\t"
		if 'PRIMER_RIGHT' in line and '_SEQUENCE' in line:
			nothing,sequence_r = line.split("=")
			primer_dict[name] += sequence_r
			primer_dict[name] += "|"
	
	new_line = ''
	final_primer_dict = dict()
	for k,v in primer_dict.items():
		primers = v.split("|")
		CG_num_dict = dict()
		CG_num_count_dict = dict()
		for primer in primers:
			CG_num = primer.count('CG')
			if CG_num not in CG_num_dict:
				CG_num_dict[CG_num] = primer
			else:
				CG_num_dict[CG_num] += "|"
				CG_num_dict[CG_num] += primer
			if CG_num not in CG_num_count_dict:
				CG_num_count_dict[CG_num] = 1
			else:
				CG_num_count_dict[CG_num] += 1
		
		if CG_num_count_dict[0] >= candidate_primer_num:
			final_primer_dict[k] = CG_num_dict[0].split("|")[0:5]
		elif CG_num_count_dict[0] + CG_num_count_dict[1] >= candidate_primer_num:
			final_primer_dict[k] = CG_num_dict[0].split("|")[0:CG_num_count_dict[0]]
			final_primer_dict[k] += CG_num_dict[1].split("|")[0:candidate_primer_num - CG_num_count_dict[0]]
		elif CG_num_count_dict[0] + CG_num_count_dict[1] + CG_num_count_dict[2] >= candidate_primer_num:
			final_primer_dict[k] = CG_num_dict[0].split("|")[0:CG_num_count_dict[0]]
			final_primer_dict[k] = CG_num_dict[1].split("|")[0:CG_num_count_dict[1]]
			final_primer_dict[k] += CG_num_dict[2].split("|")[0:candidate_primer_num - CG_num_count_dict[0] - CG_num_count_dict[1]]
		else:
			pass
		
	for key,value in final_primer_dict.items():
		chrom = str(key.split(":")[0])
		start = int(key.split(":")[1].split("-")[0])
		end = int(key.split("-")[1])
		pos = str((start+end)/2)
		primer_id = '>' + chrom + "|" + pos
		count = '1'
		for each_primer in value:
			primer_f,primer_r = each_primer.split()
			new_line += primer_id + "_" + count + "_F"
			new_line += "\n"
			new_line += primer_f
			new_line += "\n"
			new_line += primer_id + "_" + count + "_R"
			new_line += "\n"
			new_line += primer_r
			new_line += "\n"
			count = str(int(count) + 1)

	filter_CpG_primer = prefix + ".filter_CpG.primer.txt"
	f = open(filter_CpG_primer,'w')
	f.write(new_line)
	f.close

	return filter_CpG_primer

if __name__ == "__main__":
	CpG_filter(p3outfile,prefix)
