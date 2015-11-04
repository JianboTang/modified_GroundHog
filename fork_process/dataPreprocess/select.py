readpost = open('intermediate_data/post.txt','r');
readcmnt = open('intermediate_data/cmnt.txt','r');

writepost = open('used/train/post.txt','w');
writecmnt = open('used/train/cmnt.txt','w');
outpost  = open('used/test/post_outside.txt','w');
outcmnt  = open('used/test/cmnt_outside.txt','w');
inpost   = open('used/test/post_inside.txt','w');
incmnt   = open('used/test/cmnt_inside.txt','w');
def main(count,test_count):
    i = 0;
    while i < count:
        line1 = readpost.readline();
        line2 = readcmnt.readline();
        if not line1 or not line2:
            print "touch the end of file"
            break
	writepost.write(line1);
	writecmnt.write(line2);
        inpost.write(line1);
        incmnt.write(line2);
	i += 1
    while i < count + test_count:
        line1 = readpost.readline();
        line2 = readcmnt.readline();
        if not line1 or not line2:
            print "touch the end of file"
            break
	outpost.write(line1);
	outcmnt.write(line2);
	i += 1
    writepost.close();
    writecmnt.close();
    readpost.close();
    readcmnt.close();
    outpost.close();
    outcmnt.close();
    inpost.close();
    incmnt.close();
if __name__ == '__main__':
    main(100000,15000);
