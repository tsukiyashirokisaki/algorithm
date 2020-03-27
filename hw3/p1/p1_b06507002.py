import sys
from sys import exit
readpath=sys.argv[1]
writepath=sys.argv[2]
def readdata(path):
    a=open(path)
    st=a.read()
    st=st.split("\n")
    for i in range(len(st)):
        st[i]=st[i].split(" ")
        while '' in st[i]:
            st[i].remove('')
    lis1=[]
    lis2=[]
    num1=1+int(st[0][0]);num2=num1+int(st[0][1])
    for i in range(1,num1):
        lis1.append(int(st[i][1]))
    for i in range(num1,num2):
        app=[]
        for j in range(2):
            app.append(int(st[i][j]))
        lis2.append(app)

    return lis1,lis2,int(st[0][0]),int(st[0][1])
data1,data2,n,r=readdata(readpath)
stop=0
def buildtree(data2,r,n):
    np=[]
    if r==0:
        for i in range(n):
            np.append(i)
        return np
            
    pre={}
    app=[]
    app.append(data2[0][1])
    if r==1:
    	pre.update({data2[0][0]:app})
    else:
    	for i in range(r-1):
        	if data2[i][0]!=data2[i+1][0]:
        		pre.update({data2[i][0]:app})
        		app=[]
        		app.append(data2[i+1][1])
        	elif data2[i][0]==data2[i+1][0]:
        		app.append(data2[i][1])
        	if i==r-2:
        		pre.update({data2[i+1][0]:app})
    for i in range(n):
        if i not in pre:
            np.append(i)
            
    return np
ite=0
now=0
std=[]
np=buildtree(data2,r,n)
bigcan=[]
while ite!=n:
    
    can=[]
    for i in range(len(np)):
        #print(np)
        if data1[np[i]]!=(now+1)%2:
            can.append(np[i])
            ite+=1
            #newnp.remove(np[i])
         
    #print(data2,can)
    std.append(can)

    lencan=len(can)
    if lencan!=0:
        #print("hi")
        for k in range(lencan):
            j=0
            while j < len(data2):
                #print(data2[j][1]==can[k])
                if data2[j][1]==can[k]:
                #print(data2[j],can[k])
                   # print(data2)
                    data2.remove(data2[j])
                    #print(data2)
                    r-=1
                    j-=1
                j+=1
    #print(data2,r,n)
    np=buildtree(data2,r,n)
    #print("n",n)
    for ele in can:
        bigcan.append(ele)
    for ele in bigcan:
        np.remove(ele)
    if len(can)==0:
        can.append(-1)
        stop+=1
    else:
    	stop=0
    if stop==2:
    	w=open(writepath,"w")
    	w.write("-1")
    	w.close()
    	exit()
    now=(now+1)%2

w=open(writepath,"w")
lw=len(std)
w.write(str(lw)+"\n")
for i in range(lw-1):
	for j in range(len(std[i])-1):
		w.write(str(std[i][j])+" ")
	w.write(str(std[i][-1]))
	w.write("\n")
for i in range(len(std[-1])-1):
	w.write(str(std[-1][i])+" ")
w.write(str(std[-1][-1]))
	