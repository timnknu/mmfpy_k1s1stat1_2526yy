infile = open('inp_13_1.txt', 'rt')

# s = infile.readlines()
# print(s)

for line in infile:
    #print(line[:-1])
    if line.find(") ") == -1:
        print(line.rstrip())

infile.close()