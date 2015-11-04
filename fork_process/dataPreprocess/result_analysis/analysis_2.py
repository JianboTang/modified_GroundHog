import numpy
import pickle
readcmnt = open('../used/test/cmnt_inside.txt','r')
readtran = open('../used/test/cmnt_outside.txt','r');

def preprocess(line):
    lline = list(line.decode("utf-8"));
    lline = [x for x in lline if x != u' ']
    del lline[-1]
    return lline
def static(dictionary,lline):
    for i in xrange(len(lline) - 1):
        if lline[i] in dictionary:
            if lline[i + 1] in dictionary[lline[i]]:
                dictionary[lline[i]][lline[i + 1]] += 1
            else:
                dictionary[lline[i]][lline[i + 1]] = 1;
        else:
            dictionary[lline[i]] = {}
            dictionary[lline[i]][lline[i + 1]] = 1;
    return dictionary,len(lline)

def fileStatic(fileHandle,count):
    statDict = {}
    number = 0;
    i = 0;
    while i < count:
        line = fileHandle.readline();
        if not line:
            print "touch the end of file"
            break 
        statDict,temp = static(statDict,preprocess(line))
        number += temp
        i += 1
    print "total number is : ",number
    return statDict
    
def extractDict(dict1,dict2):
    common = [];
    dict_x = []
    dict_y = []
    for x in dict1:
        for y in dict1[x]:
            if x in dict2 and y in dict2[x]:
                if x not in dict_x:
                    dict_x.append(x)
                if y not in dict_y:
                    dict_y.append(y)
                common.append([x,y])
    matrix1 = numpy.zeros((len(dict_x),len(dict_y)));
    matrix2 = numpy.zeros((len(dict_x),len(dict_y)));
    for i,x in enumerate(dict_x):
        for j,y in enumerate(dict_y):
            if x in dict1 and y in dict1[x]:
                matrix1[i,j] = dict1[x][y];
            if x in dict1 and y in dict2[x]:
                matrix2[i,j] = dict2[x][y];
    return matrix1,matrix2
            
def similarityMatrix(matrix1,matrix2):
    similar = numpy.zeros(matrix1.shape[0])
    for i in xrange(matrix1.shape[0]):
        temp = numpy.zeros(1);
        temp1 = numpy.zeros(1);
        temp2 = numpy.zeros(1);
        for j in xrange(matrix1.shape[1]):
            temp += matrix1[i,j] * matrix2[i,j];
            temp1 += matrix1[i,j] ** 2;
            temp2 += matrix2[i,j] ** 2;
        similar[i] = temp / (numpy.sqrt(temp1) * numpy.sqrt(temp2));
    return similar

def main(count):
    cmnt_dict = fileStatic(readcmnt,count);
    tran_dict = fileStatic(readtran,count);
    matrix1,matrix2 = extractDict(cmnt_dict,tran_dict);
#    writeMatrix = open('matrix.pkl','w');
#    pickle.dump(matrix1,writeMatrix);
#    pickle.dump(matrix2,writeMatrix);
#    writeMatrix.close();
#    readMatrix = open('matrix.pkl','r');
#    matrix1 = pickle.load(readMatrix)
#    matrix2 = pickle.load(readMatrix);
    similar = similarityMatrix(matrix1,matrix2);
    print sum(matrix1)
    print sum(matrix2)
    print float(sum(similar >= 0.8)) / float(len(similar))
    print float(sum(similar >= 0.5)) / float(len(similar))
    
if __name__ == '__main__':
    main(1000000);
