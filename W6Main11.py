def FindingYoonNyeon(year):

    if(year%4 == 0) and (year%100 !=0 or year%400==0):
        res="YoonNyeon"
    else:
        res="PyeongNyeon"
    return res

FindingYoonNyeon(2016)