#String Matching Algorithm
def KMP_Algorithm(String,Pattern):
    LString=len(String)
    LPattern=len(Pattern)
    KMPArray=KMPArrayCreator(Pattern)
    List_Pattern=list(Pattern)
    List_String=list(String)
    i=0
    j=0
    while i<len(List_String):
        if j==0:
            start=i
        if List_Pattern[j]==List_String[i]:
            i=i+1
            j=j+1
        else:
            j=KMPArray[j]
        i=i+1
    
    print(start-1)
    
    
    
    
def KMPArrayCreator(PatternN):
    s=[]
    val=[]
    patternList=list(PatternN)
    for i in range(len(patternList)):
        if patternList[i] not in s:
            val.append(0)
            s.append(patternList[i])
        else:
            val.append(s.index(patternList[i]))
    return val
