import sys
sys.path.insert(0,"../")
from methyprimer.proper_primer.properPrimers import properPrimers
final_pre_primer = "data/test.final_pre.primer.txt" 
prefix = "test"

def test_proper_primer():

	properPrimers(final_pre_primer,prefix)
	
if __name__ == "__main__":
	test_proper_primer()
