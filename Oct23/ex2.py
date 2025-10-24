import time

s = 'abcdef\tghi\n1234\thhhhhhhhhhh'
for ch in s:
    print(ch, end='')
    time.sleep(0.5)
        