
def flatter(lst):
    res=[]
    for item in lst:
        if isinstance(item,list):
            res.extend(flatter(item))
        else:
            res.append(item)
    
    return res

lst=[1, [2, [3, 4], 5], 6]
print(flatter(lst))