from Image import *
from vertex import *
from numpy import *
from random import randint
import time
# programable stage
class geometryshader():
    def __init__(self):
        pass
    def setlootat(self,position):
        self.at=array(position)
    def setCamera(self,position):
        self.camera=array(position)

    def setnear(self,distance):
        self.near=distance
        #fix me

    def maketranview(self):
        zaxis = (self.at - self.camera)/np.linalg.norm(self.at - self.camera)
        xaxis = cross(array([0,1,0]), zaxis)
        yaxis = cross(zaxis, xaxis)
        self.viewmatrix=array([xaxis,yaxis,zaxis]).T
    def run(self,vertexbuffer):
        self.maketranview()
        vsoutbuf=[]
        
        for vsvertex in vertexbuffer:
            pos=self.viewmatrix.dot(vsvertex.pos)
            color=vsvertex.color
            vsoutbuf.append(vertex(pos,color))
        return vsoutbuf
        
class pixelshader():
    def __init__(self):
        pass
    def run(self,pixelin):
        colorbuf=[]
        depthbuf=[]
        for pix in pixelin:
            colorbuf.append(pix[1])
            depthbuf.append(pix[0][2])
        return colorbuf,depthbuf

# fixed stage
class rasterizor():
    def __init__(self,w,h,x,y,center):
        self.w = w
        self.h = h
        self.x = x
        self.y = y
        self.orix=center[0]-x/2
        self.oriy=center[1]-y/2
        self.createsolution(self.w,self.h,self.x,self.y,self.orix,self.oriy)
        pass
    def createsolution(self,w,h,x,y,orix,oriy):  
        self.pixelsize=x/w
        sol=[]
        for index in range(0,w*h):
            a=int(index/w)
            b=index%w
            px=(b+0.5)*self.pixelsize+self.orix
            py=self.y - (a+0.5)*self.pixelsize+self.oriy
            sol.append([px,py])
        self.sol = sol

    def Barycentric(self,index,linelist):
        ijk=[]
        v0=linelist[0][0]
        v1=linelist[0][1]
        v2=linelist[1][1]
        x0=v0.pos[0]
        y0=v0.pos[1]
        x1=v1.pos[0]
        y1=v1.pos[1]
        x2=v2.pos[0]
        y2=v2.pos[1]
        s = (x0*y1+x1*y2+x2*y0-x0*y2-x1*y0-x2*y1)
        
        for line in linelist[0:2]:
            x0=self.sol[index][0]
            y0=self.sol[index][1]
            x1=line[0].pos[0]
            x2=line[1].pos[0]
            y1=line[0].pos[1]
            y2=line[1].pos[1]
            ijk.append((x0*y1+x1*y2+x2*y0-x0*y2-x1*y0-x2*y1)/s)

        color=v1.color +  (v2.color-v1.color)*ijk[0] + (v0.color-v1.color)*ijk[1]
        return array(color)
    def Depthin(self,index,linelist):
        p0=linelist[0][0].pos-linelist[0][1].pos
        p1=linelist[1][0].pos-linelist[1][1].pos
        n=cross(p0,p1)
        x0=self.sol[index][0]
        y0=self.sol[index][1]
        x1=linelist[0][0].pos[0]
        y1=linelist[0][0].pos[1]
        z1=linelist[0][0].pos[1]
        z0=(array([x1,y1,z1])-array([x0,y0,0])).dot(n/n[2])
        return z0
    def scan_conversion(self,triangle,pixbuf,mode,test_color=None):
        linelist=[[triangle.vertexlist[0],triangle.vertexlist[1]],[triangle.vertexlist[1],triangle.vertexlist[2]],[triangle.vertexlist[2],triangle.vertexlist[0]]]      
        randomcolor=[randint(0,255),randint(0,255),randint(0,255)]
        
        for index in range(0,self.w*self.h): #loop all pixels
            x0=self.sol[index][0]
            y0=self.sol[index][1]
            mask=[False,False,False]
            is_hit=False
            for i,line in enumerate(linelist): #loop 3 times
                #edage function
                x1=line[0].pos[0]
                x2=line[1].pos[0]
                y1=line[0].pos[1]
                y2=line[1].pos[1]
                z1=line[0].pos[2]
                z2=line[1].pos[2]
                exp = ( x0-x1)*(y2-y1)-(y0-y1)*(x2-x1)
                mask[i]=(exp<0)
                if sum(mask)==3:
                    is_hit = True
                if mode == "default":
                    if exp<0:
                        break
                    if i==2:
                        z0=self.Depthin(index,linelist)
                        if z0 < pixbuf[index][0][2]:
                            pixbuf[index][0][2]=z0 # refresh z-buffer
                            pixbuf[index][1]=self.Barycentric(index,linelist)
                            #pixbuf[index][1]=array(test_color)
                elif mode == "line":       
                    if exp < self.pixelsize and exp > -self.pixelsize: 
                        if min(x1,x2)-self.pixelsize <= x0 and max(x1,x2)+self.pixelsize>=x0 and min(y1,y2)-self.pixelsize<=y0 and max(y1,y2)+self.pixelsize>=y0 :
                            pixbuf[index][1] = array([255,255,255])
                            break
                    if is_hit:
                        pixbuf[index][1]=array([0,0,0])
            
        return pixbuf

    def run(self,scene,backcolor,depth,mode="default"):
        #pixbuf=[[[0,0,depth],backcolor]]*self.w*self.h
        pixbuf=[]
        for i in range(self.w*self.h):
            pix=[array(self.sol[i]+[depth]),array(backcolor)]
            pixbuf.append(pix)
        #colortest=[[0,0,0],[255,0,0]]
        for i,triangle in enumerate(scene):
                pixbuf = self.scan_conversion(triangle,pixbuf,mode)
        return pixbuf

        
class context():
    def __init__(self,size,viewport,center=[0,0]):
        self.size=size
        self.vp=viewport
        self.mode="default"
        self.blendmode="Default"
        self.geometrysh=geometryshader()
        self.rasterzior=rasterizor(size[0],size[1],viewport[0],viewport[1],center)
        self.pixelsh=pixelshader()
        self.vb=None
        self.ib=None
        self.cb=array([[72,117,135]]*self.size[0]*self.size[1]) #default backend
        self.backcolor=[72,117,135]
        self.imag = image(self.size[0],self.size[1],self.cb)
        self.drawnum=0
    def setvertex(self,vertexbuffer):
        self.vb=vertexbuffer
    def setindex(self,instancebuffer):
        self.ib=instancebuffer
    def creatwindow(self,rgb):
        self.cb = [rgb]*self.size[0]*self.size[1]
    def set_farest_plane(self,far):
        self.far = far
        self.db = array([far]*self.size[0]*self.size[1])
    def setblendmode(self,mode):
        self.blendmode=mode
    def makescence(self,vsout):
        scene=[]
        if self.ib:
            for i in range(0,len(self.ib),3): 
                v0=vsout[self.ib[i]]
                v1=vsout[self.ib[i+1]]
                v2=vsout[self.ib[i+2]]
                tri=triangle([v0,v1,v2])
                scene.append(tri) 
        else:
            for i in range(0,len(vsout),3): 
                tri=triangle(vsout[i:i+3])
                scene.append(tri) 
        return scene
    def render(self,cb,db):
        if self.blendmode=="Default":
            db_mask=db<self.db #depth test
            self.db = (1-db_mask)*self.db+db_mask*db 
            cb_mask = expand_dims(db_mask,1).repeat(3,axis=1)
            self.cb = ((1-cb_mask)*self.cb+cb_mask*cb).astype(int)
        elif self.blendmode=="Additive":
            self.cb = ((cb+self.cb)/2).astype(int) 
            return self.cb
    def run(self):
 
        if self.mode == "default":
        # default pipeline
            TIME={}    
            start = time.clock()
            outvs=self.geometrysh.run(self.vb)
            TIME['geometry_stage'] = time.clock()-start
            scence=self.makescence(outvs)
            start = time.clock()
            pixelin=self.rasterzior.run(scence,self.backcolor,self.far,self.mode)
            TIME['raster_stage'] = time.clock()-start
            start = time.clock()
            cb,db= self.pixelsh.run(pixelin) 
            TIME['pixel_stage'] = time.clock()-start
            start = time.clock()
            self.render(cb,db)
            TIME['render_stage'] = time.clock()-start
            self.imag.loaddata(self.cb)
            self.drawnum +=1
            self.imag.anylyze(TIME)

        elif self.mode == "line":
            outvs=self.geometrysh.run(self.vb)
            scence=self.makescence(outvs)
            pixelin=self.rasterzior.run(scence,self.backcolor,self.far,self.mode)
            self.cb= self.pixelsh.run(pixelin) 
            self.imag = image(self.size[0],self.size[1],self.cb)
            self.imag.anylyze(TIME)

    def show(self):
        self.imag.print(self.drawnum)
