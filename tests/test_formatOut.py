import sys
sys.path.insert(0,"../")
from methyprimer.combine_primer.formatOut import formatOut
prefix = "test"

def test_formatOut():

	formatOut(prefix)
	
if __name__ == "__main__":
	test_formatOut()
