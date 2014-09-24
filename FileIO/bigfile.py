'''
Created on Sep 24, 2014

@author: bsavani
'''
def main():
    buffersize=5;
    infile=open("file.txt")
    outfile=open("newfile.txt","w");
    buffer=infile.read(buffersize)
    while len(buffer):
        outfile.write(buffer)
        print(".")
        buffer=infile.read(buffersize)

print("Done")

if __name__ == '__main__':
    main()