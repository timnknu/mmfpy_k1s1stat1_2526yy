infile = open('inp_13_1.txt', 'rb')

# s = infile.readlines()
# print(s)

for line in infile:
    #print(line)
    for c in line:
        print(c, bin(c))

infile.close()