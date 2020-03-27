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
def compare(a,b):#type(a,b) is string / if a>=b return True
    alist=cl(a);blist=cl(b)
    lena=len(alist);lenb=len(blist)
    minindex=min(lena,lenb)
    for i in range(minindex):
        if osc(blist[i])<osc(alist[i]):
            return 1
        elif osc(alist[i])<osc(blist[i]):
            return 0
    if lena<lenb:
        return 0
    elif lenb<lena:
        return 1
    return 1
def osc(st):
    if st=="(":#"[" has the same meaning of inf in the text book
        return 1000
    else:
        return ord(st)
def ms(lis,p,r):# ms=merge sort
    lenms=r-p+1;il=(lenms)//3
    if p<r:
        if lenms%3==0:
            a=p+il;b=p+2*il
            ms(lis,p,p+il-1)
            ms(lis,a,p+2*il-1)
            ms(lis,b,r)
            #print(0)
        elif lenms%3==1:
            a=p+il+1;b=p+2*il+1
            ms(lis,p,a-1)
            ms(lis,a,b-1)
            ms(lis,b,r)
            #print(1)
        elif lenms%3==2:
            a=p+il+1;b=p+2*il+2
            #print(p,a,b,r)
            ms(lis,p,a-1)
            ms(lis,a,b-1)
            ms(lis,b,r)
        return merge(lis,p,a,b,r)
def makelis(lis,st,num):
    #print(lis[5+0])
    newlis=[]
    for i in range(num):
        newlis.append(lis[st+i])
    return newlis
def merge(lis,p,a,b,r):
    if p==r:
        return 
    n1=a-p;n2=b-a;n3=r-b+1
    lis1=makelis(lis,p,n1);lis1.append("(")
    lis2=makelis(lis,a,n2);
    lis2.append("(")
    lis3=makelis(lis,b,n3);lis3.append("(")
    i=0;j=0;k=0
    for l in range(p,r+1):
        if compare(lis2[j],lis1[i]) and compare(lis3[k],lis1[i]):
            lis[l]=lis1[i]
            i=i+1
        elif compare(lis1[i],lis2[j]) and compare(lis3[k],lis2[j]):
            lis[l]=lis2[j]
            j=j+1
        elif compare(lis1[i],lis3[k]) and compare(lis2[j],lis3[k]):
            lis[l]=lis3[k]
            k=k+1
    return lis
mergesort=ms(lis,0,len(lis)-1)
w=open(writepath,"w")
for i in range(len(mergesort)-1):
    w.write(mergesort[i]+"\n")
w.write(mergesort[-1])
w.close()
#no collaborators

