import sys
sys.path.insert(0,"../")
from methyprimer.bisuffle_fasta.bisuffle_fasta import bisuffle_fasta 
filter_primer = "data/test.filter_CpG.primer.txt"
prefix = 'test'
def test_bisuffle_fasta():

	bisuffle_fasta(filter_primer,prefix)
	
if __name__ == "__main__":
	test_bisuffle_fasta()
