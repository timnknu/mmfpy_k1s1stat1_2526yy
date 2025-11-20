f = open('inp1.txt')

# while True:
#     s = f.readline()
#     print(s)
for line in f:
    line_cleaned = line.rstrip('\r\n')
    #print(line.rstrip('\r\n'))
    print(f"<{line_cleaned}>")

f.close()