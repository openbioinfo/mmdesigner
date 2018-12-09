import os
import json
import tempfile
makedb = "makeblastdb"
blastn = "blastn"
def runBlast(fa):
    db = fa.split(".")[0] + ".blastdb"
    cmd = "%s -in %s -dbtype nucl -parse_seqids -out  %s " % (makedb,fa,db)
    os.system(cmd)
    out = fa.split(".")[0] + ".blt"
    cmd = '%s -query %s -db %s -strand minus -word_size 6 -max_hsps 1 -num_threads 4  -max_target_seqs 10000  -perc_identity 100 -evalue 100000 -outfmt "6 qseqid sseqid sstrand pident length  qlen slen qstart qend sstart send" > %s ' % ( blastn,fa,db,out)
    os.system(cmd)
    return out
def parseBlast(blt):
    fp = open(blt)

    pri2pri = {}
    for line in fp.readlines():
        items = line.strip().split("\t")
        fprimer = items[0]
        fid = fprimer.rsplit("_")[0]
        rprimer = items[1]
        rid = rprimer.rsplit("_")[0]
        strand = items[2]
        mlen = int(items[4])
        qlen = int(items[5])
        slen = int(items[6])
        qstart = int(items[7])
        qend = int(items[8])
        sstart = int(items[9])
        send = int(items[10])

        if strand == "plus":
            continue
        if fid == rid :
            continue
        if qlen - qend <= 0 or slen - sstart <= 0:
            if fprimer in pri2pri:
                pri2pri[fprimer].append(rprimer)   
            else:
                pri2pri[fprimer] = [rprimer] 
    return pri2pri

def properPair(fa,pri2pri,prefix):
    fp = open(fa)
    pids = set()
    for line in fp.readlines():
        if line.startswith(">"):
            pid = line.strip().strip(">").rsplit("_",1)[0]
            pids.add(pid)

    pid2pid = {}
    for pid in pids:
        pf = pid + "_F"
        pr = pid + "_R"
        pids2 = set()
        if pf in pri2pri:
            pris = pri2pri[pf]
            for pri in pris:
                pid2 = pri.rsplit("_",1)[0]
                pids2.add(pid2)
        if pr in pri2pri:
            pris = pri2pri[pr]
            for pri in pris:
                pid2 = pri.rsplit("_",1)[0]
                pids2.add(pid2)
        pid2pid[pid] = list(pids2)
     
    sid2pids = {}
    for pid,pids2 in pid2pid.items():
        sid = pid.split("_")[0]
        pids2len = len(pids2)
        if sid in sid2pids:
            sid2pids[sid].append([pid,pids2len])
        else:
            sid2pids[sid] = [[pid,pids2len]]
    for sid,items in sid2pids.items():
        items = sorted(items,key=lambda x:x[1])
        sid2pids[sid] = items
    pid2pid_str = json.dumps(pid2pid)
    sid2pids_str = json.dumps(sid2pids)
    temp_name = prefix
    pid2pidsfile = temp_name + ".pid2pids.json"
    sid2pidsfile = temp_name + ".sid2pids.json"
    fp = open(pid2pidsfile,"w")
    fp.write(pid2pid_str)
    fp.close()
    fp = open(sid2pidsfile,"w")
    fp.write(sid2pids_str)
    return pid2pidsfile,sid2pidsfile

def properPrimers(fa,prefix):
    blt = runBlast(fa) 
    primat = parseBlast(blt)
    pid2pid,sid2pids = properPair(fa,primat,prefix)
    
    return pid2pid,sid2pids
    

if __name__ == "__main__":
    import sys
    fa = sys.argv[1]
    prex = sys.argv[2]
    properPrimers(fa,prex) 
    
