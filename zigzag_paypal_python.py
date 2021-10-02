def zigzag(s,rows):
    if rows ==1:
        return s
    res = ""
    for r in range(rows):
        inc  = 2*(rows - 1)
        for i in range(r,len(s),inc):
            res+=s[i]
            if (r>0 and r<rows-1 and (i+inc - 2*r<len(s))):
                res+=s[i+inc-2*r]
    return res
        
s = "PAYPALISHIRING"
s = zigzag(s,3)
print(s)