infile = open('inp_13_1.txt', 'rt')

# s = infile.readlines()
# print(s)
nEmptyLines = 0

for line in infile:
    line = line.rstrip()
    #print(len(line), line)
    if len(line)==0:
        nEmptyLines += 1

infile.close()

print(nEmptyLines)
