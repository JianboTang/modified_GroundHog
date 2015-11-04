#-*- coding:utf-8 -*-
"""
Created on Wed Aug 12 18:57:31 2015

@author: tangjianbo
"""

import re
cmnt = '../../originalData/repos-id-cmnt-cn-seg.txt'
post = '../../originalData/repos-id-post-cn-seg.txt'
new_cmnt = 'intermediate_data/cmnt_1.txt'
new_post = 'intermediate_data/post_1.txt'
dict_name = 'intermediate_data/dictionary_1.pkl'

def preprocess(line1):
    line1 = line1.decode("utf-8")
    xx = u"([\u4e00-\u9fa5]+)"
    pattern = re.compile(xx)
    line1 = pattern.findall(line1)
    line1 = ''.join(line1)
    lline1 = list(line1)
    lline1 = [x for x in lline1 if x != u' ']
    return lline1

def dictTree(dictName,lline):
    pass_mark = True
    temp_dict = dictName
    for i in xrange(len(lline)):
        if lline[i] in temp_dict:
            temp_dict = temp_dict[lline[i]]
        else:
            temp_dict[lline[i]] = {}
            temp_dict = temp_dict[lline[i]]
            pass_mark = False

    return pass_mark,dictName


def file_process(train_count):
    read_cmnt = open(cmnt,'r')
    read_post = open(post,'r')
    write_cmnt = open(new_cmnt,'w')
    write_post = open(new_post,'w')
    i = 0;
    dict1 = {}
    dict2 = {}
    while i < train_count:
        line1 = read_post.readline()
        line2 = read_cmnt.readline()
        if not line1 or not line2:
            print "the number of lines is : ",i
            break
        lline1 = preprocess(line1)
        lline2 = preprocess(line2)
        if  0 < len(lline1) <= 30 and 0 < len(lline2) <= 30:
            pass_mark1,dict1 = dictTree(dict1,lline1)
            pass_mark2,dict2 = dictTree(dict2,lline2)
            if not pass_mark1 and not pass_mark2:
		lline1.append(u'\n');
		lline2.append(u'\n');
                write_post.write(' '.join(lline1).encode('utf-8'))
                write_cmnt.write(' '.join(lline2).encode('utf-8'))
                i += 1
            if i % 10000 == 0:
                print i
		lline1.append(u'\n');
		lline2.append(u'\n');
                print "post : ",' '.join(lline1).encode('utf-8')
                print "resp : ",' '.join(lline2).encode('utf-8')
    read_cmnt.close()
    read_post.close()
    write_cmnt.close()
    write_post.close()
    return dict1,dict2

def main():
    dict_post,dict_cmnt = file_process(10000000)

if __name__ == '__main__':
    main()
