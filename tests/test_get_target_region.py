import sys
sys.path.insert(0,"../")
from methyprimer.get_target_region.get_target_region import get_target_region
bed = "data/test.bed"
ref = "/4_disk/genomes/hg19/hg19.fa"
prefix = "test"
product_len = 120

def test_get_target_region():
	
	get_target_region(bed,ref,prefix,product_len)

if __name__ == "__main__":
	test_get_target_region()
