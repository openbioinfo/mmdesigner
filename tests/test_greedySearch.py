import sys
sys.path.insert(0,"../")
from methyprimer.combine_primer.greedySearch import greedySearch
sid2 = "data/test.sid2pids.json"
pid2 = "data/test.pid2pids.json"
prefix = "test"

def test_greedySearch():

	greedySearch(sid2,pid2,prefix)
	
if __name__ == "__main__":
	test_greedySearch()
