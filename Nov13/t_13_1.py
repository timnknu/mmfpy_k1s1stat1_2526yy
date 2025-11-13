infile = open('inp_13_1.txt', 'rt')

# s = infile.readlines()
# print(s)

for line in infile:
    line = line.rstrip()
    if len(line) > 20:
        print(line)

infile.close()
