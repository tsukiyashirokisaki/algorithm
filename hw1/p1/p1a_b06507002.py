import sys
from tools import Parser
readpath=sys.argv[1]
writepath=sys.argv[2]
myParser=Parser(readpath)
lis=myParser.queryList()
def cl(string):#cl=creatlist
    lis=[]
    for i in range(len(string)):
        lis.append(string[i])
    return lis
def compare(a,b):#type(a,b) is string
    alist=cl(a);blist=cl(b)
    lena=len(alist);lenb=len(blist)
    minindex=min(lena,lenb)
    for i in range(minindex):
        if ord(blist[i])<ord(alist[i]):
            return 1
        elif ord(alist[i])<ord(blist[i]):
            return 0
    if lena<lenb:
        return 0
    elif lenb<lena:
        return 1
    return 0
# 1=change,0=not change
def ins(lis):#ins=insertion sort
    for i in range(1,len(lis)):
        t=lis[i]
        j=i-1
        while j>=0 and compare(lis[j],t):
            lis[j+1]=lis[j]
            j=j-1
        lis[j+1]=t
    return lis
wr=ins(lis)
w=open(writepath,"w")
for i in range(len(wr)-1):
    w.write(wr[i]+"\n")
w.write(wr[-1])
w.close()
#reference:
#https://goo.gl/uQKe5T
#https://goo.gl/BLW9bB    