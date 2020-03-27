import sys
readpath=sys.argv[1]
writepath=sys.argv[2]
def readdata(path):
    a=open(path)
    st=a.read()
    st=st.split("\n")
    for i in range(3):
        st[i]=st[i].split(" ")
        while '' in st[i]:
            st[i].remove('')
    lis=[]
    for j in range(len(st[0])):
        lis.append([int(st[0][j]),int(st[1][j]),float(st[2][j])])
    return lis
lis=readdata(readpath)
#print(lis)

def penalty(ele):
    return ele[2]
lis.sort(key=penalty,reverse=True)
#print(lis)
out=[]
for i in range(len(lis)):
    out.append(0)
def lp(lis,out,index,r,red):#r= the length of the list
    
    if index==r:
        j=0;pen=0
        for i in range(r):
            if out[i]==0 and j<len(red):
                out[i]=red[j]
                j+=1
        for i in range(r):
            if lis[i][0] in red:
                pen+=lis[i][2]
            #print(out,pen)
        
        return out,pen
    day=lis[index][1]-1
    while day>=0:
        if out[day]==0:
            out[day]=lis[index][0]
            return lp(lis,out,index+1,r,red)
        day-=1
    red.append(lis[index][0])
    return lp(lis,out,index+1,r,red)
#print(out)
#print(lis)
r=len(lis);red=[]
wt=lp(lis,out,0,r,red)
w=open(writepath,"w")
for i in range(len(wt[0])):
    w.write(str(wt[0][i])+" ")
w.write("\n")
w.write(str(wt[1]))
w.close()



