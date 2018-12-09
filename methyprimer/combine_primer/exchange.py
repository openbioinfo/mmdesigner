
def exchange(alist,i):

    head = alist[0]
    take = alist[i]
    alist.pop(i)
    alist[0] = take
    alist.insert(1,head)
    return alist




