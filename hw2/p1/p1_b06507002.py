import sys
readpath=sys.argv[1]
writepath=sys.argv[2]

def myList(inputPath):
    f1 = open(inputPath, "r", encoding="utf-8")
    st=f1.read()
    f1.close()
    new=st.split("\n")
    while "" in new: 
        new.remove("")
    new2=[]
    for ele in new:
        new2.append(int(ele))
    return new2
lis=myList(readpath)
modlist=[]
for i in range(8):
    modlist.append(9-i)

#fss= find smallest array
def fss(x,modlist,faclist):
    if x<10:
        faclist.append(x)
        faclist.reverse()
        return faclist
    for ele in modlist:
        if x%ele==0:
            faclist.append(ele)
            x=x//ele
            return fss(x,modlist,faclist)
def out(x,modlist,faclist):

    faclist=fss(x,modlist,faclist)
    if len(faclist)==1:
        st=str(10+x)
    else:
        st=""
        for ele in faclist:
            st+=str(ele)
    return st

outlist=[]
for ele in lis:
    faclist=[]
    outlist.append(out(ele,modlist,faclist))
def myPrint(outlist,writepath):
    w=open(writepath,"w")
    n=len(outlist)
    for i in range(n):
        w.write(str(outlist[i]))
        if i!=n-1:
            w.write("\n")
    w.close()
myPrint(outlist,writepath)







            
        
        
    