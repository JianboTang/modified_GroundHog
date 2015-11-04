
readfile1 = open('intermediate_data/post_1.txt','r');
readfile2 = open('intermediate_data/cmnt_1.txt','r');

writefile1 = open('used/train/post.txt','w');
writefile2 = open('used/train/cmnt.txt','w');

def preprocess(line):
    lline = [x for x in list(line) if x != u' '];
    return lline

def prune(lline):
    temp = [u' '];
    for i in xrange(len(lline) - 1):
	if temp[-1] != lline[i]:
	    temp.append(lline[i]);
    temp.append(lline[-1]);
    return temp

def main(count):
    i = 0;
    while i < count:
	line1 = readfile1.readline();
	line2 = readfile2.readline();
	if not line1 or not line2:
	    print "touch the end of files"
	    break
	lline1 = preprocess(line1.decode('utf-8'));
	lline2 = preprocess(line2.decode('utf-8'));
	lline1 = prune(lline1);
	lline2 = prune(lline2);
	writefile1.write(' '.join(lline1).encode('utf-8'));
	writefile2.write(' '.join(lline2).encode('utf-8'));
	i += 1;

if __name__ == '__main__':
    main(1000000);
