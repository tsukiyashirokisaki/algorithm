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
        new2.append(float(ele))
    return new2
lis=myList(readpath)
def findvalley(lis,f,t,n):#f=from t=to (in index) n=num in lis
    if n==1:
        return 0
    elif lis[0]<=lis[1]:
        return 0
    elif lis[n-2]>=lis[n-1]:
        return n-1
    for i in range(1,n-1):
        if lis[i]<=lis[i-1] and lis[i]<=lis[i+1]:
            return i
a=findvalley(lis,0,len(lis)-1,len(lis))
w=open(writepath,"w")
w.write(str(a))
w.close()



a=findvalley(lis,0,len(lis)-1,len(lis))
w=open(writepath,"w")
w.write(str(a))
w.close()
#no collaborators

