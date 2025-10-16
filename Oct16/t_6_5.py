s = "WWWellcccooomee ttoo PPyythooonn!!!W"

res = ""
prev_char = ""
for ch in s:
    #
    if ch != prev_char:
        res = res + ch
    #
    prev_char = ch
#
print(res)