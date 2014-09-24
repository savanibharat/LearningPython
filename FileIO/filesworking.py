'''
Created on Sep 24, 2014

@author: bsavani
'''
def main():
    infile=open("file.txt")
    outfile=open("newfile.txt","w");
    for f in infile:
        outfile.write(f)


if __name__ == '__main__':
    main()