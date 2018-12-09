import os
import glob

def formatOut(prefix):
    outfile = prefix + ".best.out"
    outs = glob.glob("%s*.com.out" % prefix)
    
    outdict = {}
    for out in outs:
        fp = open(out)
        for line in fp.readlines():
            if line:
                items  = line.strip().split("\t")
                com = items[:-1]
                cfl = int(items[-1])
                if cfl in outdict:
                    outdict[cfl].append(com)
                else:
                    outdict[cfl] = [com]

    ks = outdict.keys()
    ks.sort()
    coms = outdict[ks[0]]
    outset = set()
    for com in coms:
        com = list(set(com))
        com = "\t".join(com)
        outset.add(com)
    
    fp = open(outfile,"w")
    for s in outset:
        line = s + "\t" + str(ks[0]) + "\n"
        fp.write(line)
    fp.close()
    rmstr = " ".join(outs)
    os.system("rm %s" % rmstr)
    return outfile


if __name__ == "__main__":
    import sys
    formatOut(sys.argv[1])




   
