import sys
from sys import exit
readpath=sys.argv[1]
writepath=sys.argv[2]
class vertice(object):
	def __init__(self,position):
		self.position=position
		self.color=0#white=0;grey=1;black=2
		self.d=10000
		self.pi=-1
		self.neighbor=[]
def readdata(path):
    a=open(path)
    st=a.read()
    st=st.split("\n")
    m=len(st)
    for i in range(m):
        st[i]=st[i].split(" ")
        while '' in st[i]:
            st[i].remove('')
    return st
def fp(pos1,pos2):
    deltax=[]
    for i in range(2):
        deltax.append(pos2[i]-pos1[i])
    if deltax==[-1,0]:
        return 1
    if deltax==[0,1]:
        return 2
    if deltax==[1,0]:
        return 3
    if deltax==[0,-1]:
        return 4
def err(writepath):
    w=open(writepath,"w")
    w.write("-1")
    w.close()
    exit()

data=readdata(readpath)
m=len(data)
n=len(data[0])
lis=[]
for i in range(m):
    app=[]
    
    for j in range(n):
        if data[i][j]=="1":
            app.append(vertice([i,j]))
        elif data[i][j]=="3":
            app.append(vertice([i,j]))
            end=[i,j]
            
        elif data[i][j]=="2":
            a=vertice([i,j])
            a.color=1
            a.d=0
            app.append(a)
            start=[i,j]
        else:
            app.append(-1)
    lis.append(app)
valid=["1","2","3"]
for i in range(m):
    for j in range(n):
        if lis[i][j]==-1:
            continue
        if i<m-1 and data[i+1][j] in valid:
            lis[i][j].neighbor.append([i+1,j])
            lis[i+1][j].neighbor.append([i,j])
        if j<n-1 and data[i][j+1] in valid:
            lis[i][j].neighbor.append([i,j+1])
            lis[i][j+1].neighbor.append([i,j])
runque=[]
runque.append(lis[start[0]][start[1]].position)
while len(runque)!=0:
    u=runque[0]
    if u==end:
        break
    runque.remove(u)
    for ele in lis[u[0]][u[1]].neighbor:
        if lis[ele[0]][ele[1]].color==0:
            lis[ele[0]][ele[1]].color=1
            lis[ele[0]][ele[1]].d=lis[u[0]][u[1]].d+1
            lis[ele[0]][ele[1]].pi=fp(lis[u[0]][u[1]].position,lis[ele[0]][ele[1]].position)
            runque.append(lis[ele[0]][ele[1]].position)
    lis[u[0]][u[1]].color=2
now=lis[end[0]][end[1]].position
diction={1:[-1,0],2:[0,1],3:[1,0],4:[0,-1]}
wf=[]

pre=lis[now[0]][now[1]].pi
if pre==-1:
    err(writepath)
wf.append(pre)
dx=diction[pre]
for i in range(2):
    now[i]=now[i]-dx[i]

while now!=start:
    pre=lis[now[0]][now[1]].pi
    wf.append(pre)
    dx=diction[pre]
    for i in range(2):
        now[i]=now[i]-dx[i]
wf=wf[::-1]
w=open(writepath,"w")
for ele in wf:
    w.write(str(ele)+" ")
w.write("\n"+str(lis[end[0]][end[1]].d))
w.close()
    
    

