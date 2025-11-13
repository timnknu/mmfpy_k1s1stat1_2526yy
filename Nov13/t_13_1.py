infile = open('inp_13_1.txt', 'rt')

the_longest_line = infile.readline()
max_line_length = len(the_longest_line)

for line in infile:
    line = line.rstrip()
    print("I'm reading line:", len(line), line)
    if len(line) > max_line_length:
        max_line_length = len(line)
        the_longest_line = line

infile.close()

print('-'*80)
print(the_longest_line)
