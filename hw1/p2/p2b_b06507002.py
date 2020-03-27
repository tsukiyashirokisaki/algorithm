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
def findvalley(lis,f,t,n):#f=from t=to (in index)
    mid= (f+t)//2
    if n==1:
        return 0
    elif mid==0 and lis[0]<=lis[1]:
        return mid
    elif mid==n-1 and lis[n-1]<=lis[n-2]:
        return mid
    elif lis[mid]<=lis[mid-1] and lis[mid]<=lis[mid+1]:
        return mid
        
    elif lis[mid]<=lis[mid+1]:
        return findvalley(lis,f,mid-1,n)
    else:
        return findvalley(lis,mid+1,t,n)

a=findvalley(lis,0,len(lis)-1,len(lis))
w=open(writepath,"w")
w.write(str(a))
w.close()
#reference:https://www.geeksforgeeks.org/find-a-peak-in-a-given-array/

