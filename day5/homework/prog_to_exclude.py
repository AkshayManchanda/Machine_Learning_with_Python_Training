def main():
    infile  = open("list.txt",'r')
    outfile = open("new.txt",'w')
    for line in infile:
        if line not in read_another():
            print(line,file=outfile)
def read_another():
    ifile = open("not_include_list.txt",'r')
    return ifile.readlines()
main()
