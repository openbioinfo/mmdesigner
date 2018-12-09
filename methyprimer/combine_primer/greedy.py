from conflict import conflict 
import config

def idx2name(idxs,inls):
    outs = []
    for idx in idxs:
        out = inls[ idx[0] ][ idx[1] ]
        outs.append(out)
    return outs

def Score(idxs,inls,mat):
    outs = idx2name(idxs,inls)
    conflitNum = conflict(mat,outs)
    flag = 0
    if conflitNum < config.conflictThrehold:
        flag = 1
    return flag

def Score2(idxs,inls,mat):
    outs = idx2name(idxs,inls)
    conflitNum = conflict(mat,outs)
    if conflitNum <= config.conflictThrehold:
        config.conflictThrehold = conflitNum

def greedy(inlist,mat,limit,prefix):
    out = prefix + ".com.out"
    fp = open(out,"w") 
    inlen = len(inlist)
    stack = [(0,-1)]
    i = 0
    j = 0
    while len(stack) > 0:
        tail = stack.pop()
        tail_col = tail[1]
        tail_row = tail[0]
        tail_len = len(inlist[tail_row])
        tail_last_idx = tail_len - 1
        if tail_col < tail_last_idx :
            nextNode = [(tail_row,tail_col+1)]
            stack = stack + nextNode
            if not Score(stack,inlist,mat):
                stack.pop()
                continue  
            for n in range(tail_row+1,inlen):
                nextNode = [(n,0)]
                stack = stack + nextNode
                if not Score(stack,inlist,mat):
                    stack.pop()
                    break
            # search space
            j = j + 1
            if j > limit:
                break
            if len(stack) == inlen:
                # answser
                i = i + 1
                Score2(stack,inlist,mat)
                out = idx2name(stack,inlist)
                line = "\t".join(out)
                line = line + "\t" + str(config.conflictThrehold) + "\n"
                print line
                fp.write(line)
    fp.close()
