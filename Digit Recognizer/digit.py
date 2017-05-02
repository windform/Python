def loadTrainData():  
    l=[]  
    with open('train.csv') as file:  
         lines=csv.reader(file)  
         for line in lines:  
             l.append(line) #42001*785  
    l.remove(l[0])  
    l=array(l)  
    label=l[:,0]  
    data=l[:,1:]  
    return nomalizing(toInt(data)),toInt(label);

def toInt(array):  
    array=mat(array)  
    m,n=shape(array)  
    newArray=zeros((m,n))  
    for i in xrange(m):  
        for j in xrange(n):  
                newArray[i,j]=int(array[i,j])  
    return newArray;

def nomalizing(array):  
    m,n=shape(array)  
    for i in xrange(m):  
        for j in xrange(n):  
            if array[i,j]!=0:  
                array[i,j]=1
    return array;

def loadTestResult():  
    l=[]  
    with open('sample_submission.csv') as file:  
         lines=csv.reader(file)  
         for line in lines:  
             l.append(line)  
    l.remove(l[0])  
    label=array(l)  
    return toInt(label[:,1])

def classify(inX, dataSet, labels, k):  
    inX=mat(inX)  
    dataSet=mat(dataSet)  
    labels=mat(labels)  
    dataSetSize = dataSet.shape[0]                    
    diffMat = tile(inX, (dataSetSize,1)) - dataSet     
    sqDiffMat = array(diffMat)**2  
    sqDistances = sqDiffMat.sum(axis=1)                    
    distances = sqDistances**0.5  
    sortedDistIndicies = distances.argsort()              
    classCount={}                                        
    for i in range(k):  
        voteIlabel = labels[0,sortedDistIndicies[i]]  
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1  
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)  
    return sortedClassCount[0][0] 

def saveResult(result):  
    with open('result.csv','wb') as myFile:      
        myWriter=csv.writer(myFile)  
        for i in result:  
            tmp=[]  
            tmp.append(i)  
            myWriter.writerow(tmp)  

def handwritingClassTest():  
    trainData,trainLabel=loadTrainData()  
    testData=loadTestData()  
    testLabel=loadTestResult()  
    m,n=shape(testData)  
    errorCount=0  
    resultList=[]  
    for i in range(m):  
         classifierResult = classify(testData[i], trainData, trainLabel, 5)  
         resultList.append(classifierResult)  
         print "the classifier came back with: %d, the real answer is: %d" % (classifierResult, testLabel[0,i])  
         if (classifierResult != testLabel[0,i]): errorCount += 1.0  
    print "\nthe total number of errors is: %d" % errorCount  
    print "\nthe total error rate is: %f" % (errorCount/float(m))  
    saveResult(resultList) 

classifierResult = classify(testData[i], trainData[0:20000], trainLabel[0:20000], 5)