try:
    fout=open('python.txt','a')
    fin=open('outputNumber','r')
    for line in fin:
        fout.write(line)
    fout.close()
    fin.close()
except Exception as e:
    print e