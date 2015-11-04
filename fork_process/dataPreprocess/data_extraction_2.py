import numpy
import pickle

readfile1 = open('intermediate_data/post_1.txt','r');
readfile2 = open('intermediate_data/cmnt_1.txt','r');
writefile = open('intermediate_data/dictionary.pkl','w');
#writefile1 = open('intermediate_data/post_2.txt','w');
#writefile2 = open('intermediate_data/cmnt_2.txt','w');

def staticDict(dictionary,lline):
    for i in xrange(len(lline)):
	if lline[i] in dictionary:
	    dictionary[lline[i]] += 1;
	else:
	    dictionary[lline[i]] = 1;
    return dictionary

def preprocess(line):
    line = line.decode("utf-8");
    lline = [x for x in list(line) if x != u' '];
    del lline[-1]
    return lline
    
def dictPrint(dictionary):
    for x in dictionary:
	print x," : ",dictionary[x];

def main(count):
    dict1 = {};
    dict2 = {};
    i = 0;
    while i < count:
	line1 = readfile1.readline();
	line2 = readfile2.readline();
	if not line1 or not line2:
	    print "touch the end of file"
	    break;
	lline1 = preprocess(line1);
	lline2 = preprocess(line2);
	dict1 = staticDict(dict1,lline1);
	dict2 = staticDict(dict2,lline2);
	i += 1;
    print "print the first dictionary"
    dictPrint(dict1);
    print "print the second dictionary"
    dictPrint(dict2); 
    pickle.dump(dict1,writefile);
    pickle.dump(dict2,writefile);
if __name__ == '__main__':
    main(1000000);
