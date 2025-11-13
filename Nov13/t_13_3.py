myfile = open('file_13_3.txt', 'wt')

#myfile.write("abcccccccc\nhhhhhhhhhh")
#print("this is my line for the file", file=myfile)
for i in range(1, 9+1):
    c = str(i)
    print(c*i, file=myfile)

myfile.close()

