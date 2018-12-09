import sys
sys.path.insert(0,"../")
from methyprimer.verify_primer.verify_primer import verify_primer 
final_pre_primer = "test/test.final_pre.primer.txt"
formatOut = 'test/test.best.out'
prefix = 'test'
def test_verify_primer():

	verify_primer(final_pre_primer,formatOut,prefix)
	
if __name__ == "__main__":
	test_verify_primer()
