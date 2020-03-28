
from component import *
from numpy import *
from random import randint
import time

        


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
        xlist=[triangle.vertexlist[0].pos[0],triangle.vertexlist[1].pos[0],triangle.vertexlist[2].pos[0]]
        ylist=[triangle.vertexlist[0].pos[1],triangle.vertexlist[1].pos[1],triangle.vertexlist[2].pos[1]]

        linelist=[[triangle.vertexlist[0],triangle.vertexlist[1]],[triangle.vertexlist[1],triangle.vertexlist[2]],[triangle.vertexlist[2],triangle.vertexlist[0]]]      
        randomcolor=[randint(0,255),randint(0,255),randint(0,255)]
        for index in range(0,self.w*self.h): #loop all pixels
            x0=self.sol[index][0]
            y0=self.sol[index][1]
            if min(xlist)-self.pixelsize > x0 or max(xlist)+self.pixelsize < x0 or min(ylist)-self.pixelsize > y0 or max(ylist)+self.pixelsize < y0:
                continue
            mask=[False,False,False]
            is_hit=False
            for i,line in enumerate(linelist): #loop 3 times
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

        

