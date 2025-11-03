
def nsd(a, b):
    if b==0:
        return a
    # else:
    if a==0:
        return b
    # else:
    if a>=b:
        res = nsd(a % b, b)
        return res
    # else:
    res = nsd(a, b % a)
    return res
#

#y = nsd(42, 24)
y = nsd(8675476476, 654745435)
print(y)
