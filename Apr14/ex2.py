a = [1,2,3]
b = set()
s = 'jyvkuy'

s1 = set(dir(a))
s2 = set(dir(b))
s3 = set(dir(s))

print(s1.intersection(s2).intersection(s3))