import sys
sys.path.insert(0,"../")
from methyprimer.combine_primer.combine_primer import combine_primer
final_pre_primer = "data/test.final_pre.primer.txt" 
prefix = "test"

def test_combine_primer():

	combine_primer(final_pre_primer,prefix)
	
if __name__ == "__main__":
	test_combine_primer()
