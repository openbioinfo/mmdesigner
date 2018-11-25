import sys
sys.path.insert(0,"../")
from methyprimer.primer3_design.primer3_design import primer3_design
target_fa = "data/test.target.fa" 
config = "data/test.config"
prefix = "test"

def test_primer3_design():

	primer3_design(target_fa,config,prefix)
	
if __name__ == "__main__":
	test_primer3_design()
