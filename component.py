from numpy import *


def rotationz(x):
    x1=array([cos(x),sin(x),0])
    x2=array([-sin(x),cos(x),0])
    x3=array([0,0,1])
    return array([x1,x2,x3])
def rotationy(x):
    x1=array([cos(x),0,-sin(x)])
    x2=array([0,1,0])
    x3=array([sin(x),0,cos(x)])
    return array([x1,x2,x3])
class vertex():
    def __init__(self,pos=None,color=None,normal=None,uv=None):
        if type(pos) is list:
            self.pos=array(pos)
            if len(pos) ==3:
                self.pos=append(self.pos,1)
        else:
            if len(pos) ==4:
                self.pos=pos
            elif len(pos) ==3:
                self.pos=append(pos,1)
        if type(color) is list:
            self.color=array(color)
        else:
            self.color=color
        if type(normal) is list:
            self.normal=array(normal)
        else:
            self.normal=normal
        if type(uv) is list:
            self.uv=array(uv)
        else:
            self.uv=uv

class pixel():
    def __init__(self,pos=None,color=None,uv=None):
        if type(pos) is list:
            self.pos=array(pos)
        else:
            self.pos=pos
        if type(color) is list:
            self.color=array(color)
        else:
            self.color=color
        if type(uv) is list:
            self.uv=uv
        else:
            self.uv=uv

class triangle():
    def __init__(self,vertexlist,w,h,orix,oriy,pixelsize,idxarray):
        if len(vertexlist)==3:
            self.vertexlist = vertexlist
            pos=[x.pos[0:2] for x in vertexlist]
            uv=array([x.uv for x in vertexlist])
            self.uvl=int(uv[:,0].min()*512)
            self.uvr=int(uv[:,0].max()*512)
            self.uvu=int(uv[:,1].min()*512)
            self.uvd=int(uv[:,1].max()*512)
            if self.culltest(array(pos)):
                self.makeBVH(array(pos),w,h,orix,oriy,pixelsize,idxarray)
                self.culltest=True
<<<<<<< HEAD
                x0=pos[0][0]
                y0=pos[0][1]
                
                x1=pos[1][0]
                y1=pos[1][1]
                
                x2=pos[2][0]
                y2=pos[2][1]
                
                self.s = (x0*y1+x1*y2+x2*y0-x0*y2-x1*y0-x2*y1)
=======
>>>>>>> 21f6ded06283429d1a8f036e09cd8856dfa5d69b
            else:
                self.culltest=False
    def culltest(self,pos):
        l1=pos[1]-pos[0]
        l2=pos[2]-pos[0]
        return cross(l1,l2)<0

    def makeBVH(self,pos,w,h,orix,oriy,pixelsize,idxarray):
        l=pos[:,0].min()    
        r=pos[:,0].max()  
        u=pos[:,1].max()  
        d=pos[:,1].min()
        
<<<<<<< HEAD
        idx_row_start= int((l-orix)/pixelsize)-1 if l>orix else 0
        idx_row_stop = int((r-orix)/pixelsize)+1 if r>orix else 0
        idx_col_start= int((oriy-u)/pixelsize)-1 if u<oriy else 0
        idx_col_stop= int((oriy-d)/pixelsize)+1 if d<oriy else 0
=======
        idx_row_start= int((l-orix)/pixelsize)-1
        idx_row_stop = int((r-orix)/pixelsize)+2
        idx_col_start= int((oriy-u)/pixelsize)-1
        idx_col_stop= int((oriy-d)/pixelsize)+2
>>>>>>> 21f6ded06283429d1a8f036e09cd8856dfa5d69b
        bvh=idxarray[idx_col_start:idx_col_stop,idx_row_start:idx_row_stop]
        #bvh_sol_1=sol[bvh[0]]
        #bvh_sol_2=sol[bvh[-1]]
        self.bvh=bvh.reshape(1,bvh.size)[0]
        
            

class light():
    def __init__(self,src,direct,clour,mode):
        self.src=array(src)
        self.direct=array(direct)
        self.color=array(clour)
        self.mode=mode
        

def loadfromobj(path):
    f=open(path,"r")
    cont= f.readlines()
    posbuf=[]
    normalbuf=[]
    indexbuf=[]
    uvbuf=[]
    vb=[]
    for l in cont:
        if l.split(" ")[0]=="v":
            pos=l.split(" ")[1:]
            posf = [float(x) for x in list(filter(None, pos))]
            posf.append(1.0)
            posbuf.append(posf)
        elif l.split(" ")[0]=="vn":
            norm=l.split(" ")[1:]
            normf = [float(x) for x in list(filter(None, norm))]
            #normf[1]=1.0-normf[1]
            normalbuf.append(normf)
        elif l.split(" ")[0]=="vt":
            uv=l.split(" ")[1:]
            uvf = [float(x) for x in list(filter(None, uv))]
            uvf.reverse()
            
            #uvf[1]
            uvbuf.append(uvf)

        elif l.split(" ")[0]=="f":
            for tri in l.split(" ")[1:]:
                idx=tri.split("/")
                if int(idx[0])>0:
                    offset=-1
                else:
                    offset=0
                vb.append(vertex(posbuf[int(idx[0])+offset],normal=normalbuf[int(idx[2])+offset],uv=uvbuf[int(idx[1])+offset]))
    return vb
if __name__=="__main__":
    v0=vertex([0,1,1])
    v1=vertex([0,0,1])
    v2=vertex([1,0,1])
    tri1=triangle([v0,v1,v2])
