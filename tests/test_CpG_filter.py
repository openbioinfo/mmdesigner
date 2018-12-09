import sys
sys.path.insert(0,"../")
from methyprimer.filter_primer.CpG_filter import CpG_filter
p3outfile = "data/test.raw.primer.txt"
candidate_primer_num = 5
prefix = 'test'
def test_CpG_filter():

	CpG_filter(p3outfile,candidate_primer_num,prefix)
	
if __name__ == "__main__":
	test_CpG_filter()
