import os


def primer3_design(target_fa,config,prefix):

	allconfig = ''
#	config_file = open(config)
	file = open(target_fa)
	for line in file:
		line = line.strip()
		if line.startswith('>'):
			name = line[1:]
			continue
		sequence = line
		length = len(sequence)
		hlength = length/2
		target = "%s,1" % hlength

		config_file = open(config)
		for config_line in config_file:
			config_line = config_line.strip()
			if config_line.startswith("SEQUENCE_ID"):
				config_line = "SEQUENCE_ID=" + name
			elif config_line.startswith("SEQUENCE_TEMPLATE"):
				config_line = "SEQUENCE_TEMPLATE=" + sequence
			elif config_line.startswith("SEQUENCE_TARGET"):
				config_line = "SEQUENCE_TARGET=" + target
			allconfig += config_line
			allconfig += "\n"
	
	p3infile = prefix + ".all.config"
	f = open(p3infile,'w')
	f.write(allconfig)
	f.close()
	
	outfile = prefix + ".raw.primer.txt"
	cmd = "primer3 %s -output=%s" % (p3infile,outfile)
	os.system(cmd)

if __name__ == "__main__":
	primer3_design(target_fa,config,prefix)
