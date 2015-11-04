readpost = open('../used/test/post_inside.txt','r');
readcmnt = open('../used/test/cmnt_inside.txt','r');
readtran = open('../used/test/encdec_trans_inside.txt','r');

def preprocess(line):
    lline = list(line.decode("utf-8"));
    lline = [x for x in lline if x != u' '];
    return lline
def compareSen(line1,line2):
    lline1 = preprocess(line1);
    lline2 = preprocess(line2);
    senLen = min(len(lline1),len(lline2));
    mark = True;
    for i in xrange(senLen):
        if lline1[i] != lline2[i]:
            mark = False;
            break 
    return mark
def main(count):
    i = 0;
    amount = 0;
    while i < count:
        line2 = readcmnt.readline();
        line3 = readtran.readline();
        if not line2 or not line3:
            break
        if compareSen(line2,line3):
            amount += 1
        i += 1
    print "touch the end, the amount of lines is : ",i
    print "the total amount of the same or part same sentences is :",amount

if __name__ == '__main__':
    main(1000000);
