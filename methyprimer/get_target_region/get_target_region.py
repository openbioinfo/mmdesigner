import os

def get_target_region(bed,ref,prefix):
	
	max_product_len = 120
	new_file = ''
	file = open(bed)
	for line in file:
		line_list = line.strip().split()
		chr   = str(line_list[0])
		start = str(int(line_list[1]) - max_product_len)
		end   = str(int(line_list[2]) + max_product_len)
		new_line = "\t".join([chr,start,end])
		new_file += new_line
		new_file += "\n"
	
	new_bed = prefix + ".extend.bed"
	f = open(new_bed,'w')
	f.write(new_file)
	f.close()
	target_fasta = prefix + ".target.fa"
	cmd = "bedtools getfasta -fi %s -bed %s -fo %s" % (ref,new_bed,target_fasta)
	print cmd
	os.system(cmd)

	return target_fasta

if __name__ == "__main__":
	get_target_region(bed,ref,prefix)
