import sys
sys.path.insert(0,"../")
from methyprimer.filter_primer.CpG_filter import CpG_filter
p3outfile = "data/test.raw.primer.txt"
prefix = 'test'
def test_CpG_filter():

	CpG_filter(p3outfile,prefix)
	
if __name__ == "__main__":
	test_CpG_filter()
