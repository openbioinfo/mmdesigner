import sys
def conflict(pid2pidsdict,outs):
    outs = set(outs)
    cf1 = []
    for pid in outs:
        if pid in pid2pidsdict:
            pid2s = pid2pidsdict[pid]
            cf1.extend(pid2s)
    
    cf2 = []
    for cf in cf1:
        if cf in outs:
            cf2.append(cf)
    return len(cf2)/2


if __name__ == "__main__":
    import json
    p2p = sys.argv[1] 
    fp = open(p2p)
    p2p = json.loads(fp.read())
    out = [u'chr19|45923653_92', u'chr16|69143577_91', u'chr5|7870973_30', u'chr17|7579472_34', u'chr13|32915244_18', u'chr8|69389217_89', u'chr1|11856378_39', u'chr7|87138645_51', u'chr17|41222975_41', u'chr21|37518706_70', u'chr16|69745145_38', u'chr17|41258495_69', u'chr3|14187449_33', u'chr11|67352689_12', u'chr17|41245852_43', u'chr13|32937507_7', u'chr17|41246381_86', u'chr3|124456742_34']

    conflict(p2p,out)
