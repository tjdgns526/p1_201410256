def charCount(word):
    d=dict()
    for c in word:
        if c not in d:
            d[c]=1    
        else:
            d[c]=d[c]+1
    return d

def lab8():
    word=raw_input("Enter the word.")
    data=charCount(word)
    print data

def main():
    lab8()
    
if __name__=="__main__":
    main()