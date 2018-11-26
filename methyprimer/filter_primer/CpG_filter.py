import os 

def CpG_filter(p3outfile):
	
	#PRIMER_LEFT_SEQUENCE就是正常参考序列的一样的部分，PRIMER_RIGHT_0_SEQUENCE是正常参考序列的反向互补序列
	#而甲基化情况不同，先暂时只看正链的话，primer_left应该为甲基化参考序列的反向，primer_right应该为甲基化参考序列的反向互补
	#现在的 left_primer换成甲基化参考序列之后需要做互补处理
	file = open(p3outfile)
	for line in file:
		line = line.strip()
		if line.startswith("SEQUENCE_ID"):
			nothing,name = line.split("=")
			primer = dict()
		if 'PRIMER_LEFT' and '_SEQUENCE' in line:
			nothing,sequence = line.split("=")
			if 'CG' in sequence:
				count_left_CG = sequence.count("CG")
		if 'PRIMER_RIGHT' and '_SEQUENCE' in line:
			nothing,sequence = line.split("+")
			if 'CG' in sequnece:
				count_right_CG = sequence.count("CG")
