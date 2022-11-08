def search2 (mylist, target, lo, hi):
    while lo <= hi:
        if mylist[lo] == target:
            return lo
        lo += 1
        hi -= 1
        
        
    return -1


a = [1,2,3,4,5,6,7,8,9,10,11]