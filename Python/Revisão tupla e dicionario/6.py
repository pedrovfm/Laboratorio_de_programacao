def inva(d):
    inv_d = {}
    for k, v in d.items():
        if v not in inv_d:
            inv_d[v] = [k]
        else:
            inv_d[v].append(k)
    print(inv_d)
    print(len(inv_d))
    return inv_d

inva({1:2, 3:1, 4:2})