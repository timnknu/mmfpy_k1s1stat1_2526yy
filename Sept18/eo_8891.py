n = int(input("Input:"))
cond1 = n%2 == 0
cond2 = (n < 0) and (n%3 == 0)
print(cond1, cond2)
# cond1 cond2
# True  True  -> NO
# True  False -> YES
# False True  -> YES
# False False -> NO
# варіант перевірки №1
if cond1 != cond2: # або можна використати "виключне або": cond1 ^ cond2
    print("YES")
else:
    print("NO")
# варіант перевірки №2
if (cond1 and (not cond2)) or ((not cond1) and cond2):
    print("YES")
else:
    print("NO")

