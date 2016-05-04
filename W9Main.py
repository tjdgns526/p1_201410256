def charCount(word):
    d=dict()
    for c in word:
        if c not in d:
            d[c]=1    
        else:
            d[c]=d[c]+1
    return d

def countDigitsLetters(word):
    d=dict()
    d.update({'digit':0,'alpha':0})
    for i in word:
        if i.isdigit():
            d['digit']=d['digit']+1
        elif i.isalpha():
            d['alpha']=d['alpha']+1
    return d
def graph(d):  
    import matplotlib
    import matplotlib.pyplot as pit
    pit.bar(range(len(d)),d.values(),align='center')
    pit.xticks(range(len(d)),list(d.keys()))
    pit.show()

def lab8():
    word=raw_input("Enter the word.")
    data1=charCount(word)
    print data1
    data2=countDigitsLetters(word)
    print data2
    graph(data1)
    graph(data2)
    
def main():
    lab8()

if __name__=="__main__":
    main()
