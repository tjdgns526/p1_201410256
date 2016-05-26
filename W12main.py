def editTime(editor,text):
    fin=open('output.txt','r')
    fout=open('outputUpper.txt','w')
    timeEdited=time.strftime('%Y-%m-%d  %H:%M:%S')
    for line in fin:
        words=line.split()
        for word in words:
            if word==text:
                word=word.upper()
            print "[{0} edited {1}]{2}".format(editor, timeEdited, word)
        print '\n'
    fin.close()
    fout.close()

def arrayTwoLines(array):
    fout=open('homework.txt','w')

    for i in array:
        if i%2==1:
            toPrint="{0}\t".format(i)
            fout.write(toPrint)
        else:
            toPrint="{0}\t\n".format(i)
            fout.write(toPrint)
    fout.close()

def lab12():
    editTime('KSH','line')
    data=list()
    data=[1,2,3,4,5,6,7,8,9,10]  
    arrayTwoLines(data)

def main():
    lab12()


if__name__=="__main__":
    main()