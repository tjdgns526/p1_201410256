def distance():
    Locations=((37.571572, 126.976475),(37.576502, 126.985526),(37.570188, 126.982941),(37.565699, 126.977103),(37.574527, 126.957706))
    import math
    ky=(37.575869, 126.976637)
    d=list()
    for i in Locations:
        d.append(math.sqrt((ky[0]-i[0])**2+(ky[1]-i[1])**2))
    print "minimum distance:",min(d)
def seoulMnW():
    data=[
    [74425, 76326],
    [61164, 61636],
    [109688, 115744],
    [144796, 146776],
    [174996, 181676],
    [177841, 177434],
    [204630, 205980],
    [223373, 232245],
    [161055, 166130],
    [171576, 176735],
    [279169, 293772],
    [239450, 251066],
    [148690, 156510],
    [182977, 196992],
    [237792, 242641],
    [283869, 296762],
    [209344, 210282],
    [118965, 114441],
    [186503, 186856],
    [195734, 203014],
    [254381, 249472],
    [212401, 229111],
    [271654, 295354],
    [319197, 335045],
    [229829, 231671]]
    mSum=0
    wSum=0
    for i in data:
        mSum= mSum+i[0]
        wSum= wSum+i[1]
    print "Seoul Male Pop=",mSum
    print "Seoul Female Pop=",wSum
    print "Seoul Male Avr=", mSum/len(data)
    print "Seoul Female Avr=", wSum/len(data)

    d=list()
    for i in data:
        d.append((i[0]+i[1])/2)
    print d

def milkFinder():
    coffee=[['Coffee','Water','Milk','Icecream'],['Espresso','No','No','No'],['Long Black','Yes','No','No'],['Flat white','No','Yes','No'],['cappuccino','No','Yes','No'],['Affogato','No','No','Yes']]
    subData= coffee[1:6]
    milktime=0
    for i in subData:
        if i[2]=='Yes':
            milktime = milktime +1
    print "Milk rates:", float(milktime)/float(len(subData))
def enmaAvr():
    enSum=0
    maSum=0
    k=0
    j=0
    Grade=[('English',100),('Math',200),('English',200),('Math',200),('English',100),('Math',300)]
    for i in Grade:
        if i[0]=='English':
            enSum = enSum + i[1]
            k = k+1
        else:
            maSum = maSum + i[1]
            j = j+1
    enAvr = enSum/k
    maAvr = maSum/j
    print "English Average=",enAvr,"Math Average=",maAvr
def Beatles():
    d=dict()
    beatles= list()
    most=set()
    beatles=("When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness She is standing right in front of me peaking words of wisdom let it be Let it be let it be let it be let it be hisper words of wisdom let it be nd when the broken-hearted people Living in the world agree There will be an answer let it be For though they may be parted There is still a chance that they will see There will be an answer let it be Let it be let it be Let it be let it be Yeah there will be an answer let it be Let it be let it be Let it be let it be Whisper words of wisdom let it be Let it be let it be Ah let it be yeah let it be Whisper words of wisdom let it be And when the night is cloudy There is still a light that shines on me Shine on until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be Let it be yeah let it be Oh there will be an answer let it be Let it be let it be Let it be yeah let it be Whisper words of wisdom let it be")

    for i in beatles.split():
        if i not in d:
            d[i]=1
        else:
            d[i]  = d[i]+1
    print "The most words are:"

    for i in d:
        if d[i]>20:
            print i

def lab10():
    distance()
    seoulMnW()
    milkFinder()
    enmaAvr()
    Beatles()
def main():
    lab10()
if __name__=="__main__":
    main()