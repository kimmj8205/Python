def max_sort(s):
    ss=[]
    for i in range(len(s)):
        maxi=max(s)
        s.remove(maxi)
        ss.append(maxi)
    return ss
