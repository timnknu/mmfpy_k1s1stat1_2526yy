w1 = "abrakadabra"
w2 = "dakarX"

def get_chars_count(s):
    chars_cnts = {}
    for c in set(s):
        chars_cnts[c] = s.count(c)
    return chars_cnts
D_from = get_chars_count(w1)
D_to = get_chars_count(w2)
print(D_from)
print(D_to)
is_enough = True
for k_we_want, v_we_want in D_to.items():
    # if k_we_want not in D_from:
    #     is_enough = False
    #     break
    #if D_from[k_we_want] < v_we_want:
    if D_from.get(k_we_want, -100500) < v_we_want:
        is_enough = False
        break
print(is_enough)
