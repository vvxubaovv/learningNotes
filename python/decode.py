#encoding=utf-8
import re
import sys

def to_str(bs,encoding='utf8'):
    return bs.decode(encoding)

def parse8(s):
    sa=s.split('\\')
    if sa[0]=='':
        sa=sa[1:]
    b=bytearray()
    for i in sa:
        b.append(int(i,base=8))
    return b

def parse16(s):
    sa=s.split('\\')
    if sa[0]=='':
        sa=sa[1:]
    b=bytearray()
    for i in sa:
        s='0'+i
        b.append(int(s,base=16))
    return b

if __name__=='__main__':
    b=parse8(r'\344\270\255\345\233\275')
    s=to_str(b)
    #print(u'中国')
    #print(s)
    b=parse16(r'\xe4\xb8\xad\xe5\x9b\xbd')
    s=to_str(b)
    #print(s)
    print('参数:'+str(sys.argv))
    if(len(sys.argv)<2):
        print('未输入参数')
        exit()
    s=sys.argv[1]
    encoding='utf8'
    if(len(sys.argv)>2):
        encoding=sys.argv[2]
    if s.index('x') != -1:
        ss=to_str(parse16(s),encoding)
    else:
        ss=to_str(parse8(),encoding)
    print(ss)




















