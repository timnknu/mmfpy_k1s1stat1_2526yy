s = "WWWellcccooomee ttoo PPyythooonn!!!W"

res = ""
for i in range(len(s)):
    if (i==0) or (s[i] != s[i-1]):
        res = res + s[i]
print(res)