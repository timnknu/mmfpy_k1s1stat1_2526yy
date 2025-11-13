infile = open('inp_13_1.txt', 'rt')

max_line_length = -10
the_longest_line = ''

for line in infile:
    line = line.rstrip()
    #print(len(line), line)
    if len(line) > max_line_length:
        max_line_length = len(line)
        the_longest_line = line

infile.close()

print(the_longest_line)
