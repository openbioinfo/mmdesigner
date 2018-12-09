import json
from greedy import greedy
import random
from multiprocessing import Pool
from exchange import exchange
import copy
threads = 6
def greedySearch(sid2pids,pid2pid,prefix):
    iterationTime = 1000000
    fp = open(sid2pids)
    sid2pids = json.loads(fp.read())
    fp.close()
    fp = open(pid2pid)
    pid2pid = json.loads(fp.read())
    fp.close()

    PIDS = []
    SIDS = []

    for sid,pids in sid2pids.items():
        ps = []
        for pid in pids:
            p = pid[0]
            ps.append(p)
        PIDS.append(ps) 
    '''
    PIDSS = []
    limits = []
    PIDSS.append(PIDS[:])
    limits.append(iterationTime)
    for i in range(1,len(PIDS[0])):
        iterationTime = iterationTime/2
        limits.append(iterationTime)
        PIDS2 = copy.deepcopy(PIDS)
        head = copy.deepcopy(PIDS2[0])
        head = exchange(head,i)
        PIDS2[0] = head
        PIDSS.append(PIDS2[:]) 
    #gready search
    pools = Pool(threads)
    it = min(5,len(PIDSS))
    for i in range(it):
        prex = prefix + ".%s" % i
        PIDS = PIDSS[i]
        limit = limits[i]
        pools.apply_async(greedy,(PIDS,pid2pid,limit,prex))
    pools.close()
    pools.join()
    '''
    greedy(PIDS,pid2pid,10000000,prefix)
if __name__ == "__main__":
    import sys
    s2p = sys.argv[1]
    p2p = sys.argv[2]
    prefix = sys.argv[3]
    #greedySearch("example.sid2pids.json","example.pid2pids.json")
    greedySearch(s2p,p2p,prefix)
    
