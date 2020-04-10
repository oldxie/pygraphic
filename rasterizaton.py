
from component import *
from numpy import *
from random import randint
import time
import matplotlib.pyplot as plt
        


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
        #self.lightmode="plane"
        self.rastmode="default"
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
    def scan_conversion(self,triangle,test_color=None):

<<<<<<< HEAD
        linelist=[[triangle.vertexlist[0],triangle.vertexlist[1]],[triangle.vertexlist[1],triangle.vertexlist[2]],[triangle.vertexlist[2],triangle.vertexlist[0]]]
        #randomcolor=[randint(0,255),randint(0,255),randint(0,255)]
        count = 0
        for index in triangle.bvh: #loop all pixels in BVH
        #for index in range(0,self.w*self.h):
            
=======
    def Barycentric(self,index,linelist):
        v0=linelist[0][0]
        v1=linelist[0][1]
        v2=linelist[1][1]
        #if list(v0.color) == list(v1.color) == list(v2.color):
        #   return v0.color
        ijk=[]
        x0=v0.pos[0]
        y0=v0.pos[1]
        z0=v0.pos[2]
        x1=v1.pos[0]
        y1=v1.pos[1]
        z1=v1.pos[2]
        x2=v2.pos[0]
        y2=v2.pos[1]
        z2=v2.pos[2]
        s = (x0*y1+x1*y2+x2*y0-x0*y2-x1*y0-x2*y1)
        for line in linelist[0:2]:
            x0=self.sol[index][0]
            y0=self.sol[index][1]
            x1=line[0].pos[0]
            x2=line[1].pos[0]
            y1=line[0].pos[1]
            y2=line[1].pos[1]
            ijk.append((x0*y1+x1*y2+x2*y0-x0*y2-x1*y0-x2*y1)/s)
            #[c]
        color=v1.color +  (v2.color-v1.color)*ijk[0] + (v0.color-v1.color)*ijk[1]
        z= 1/(1/z1 +  (1/z2-1/z1)*ijk[0] + (1/z0-1/z1)*ijk[1])
        #z= z1 +  (z2-z1)*ijk[0] + (z0-z1)*ijk[1]
        uv=(v0.uv*ijk[1]/z0+v2.uv*ijk[0]/z2+v1.uv*(1-ijk[0]-ijk[1])/z1)*z
        #uv=(v1.uv/z0+ (v2.uv-v1.uv)*ijk[0]/z1 + (v0.uv-v1.uv)*ijk[1]/z2)*z
        return array(color),z,uv
    def normal_interpolate(self,index,vertexlist):
        v0=vertexlist[0]
        v1=vertexlist[1]
        v2=vertexlist[2]
        return (v0.normal+v1.normal+v2.normal)/3
    def Depthin(self,index,linelist):
        p0=linelist[0][0].pos-linelist[0][1].pos
        p1=linelist[1][0].pos-linelist[1][1].pos
        
        n=cross(p0,p1)
        x0=self.sol[index][0]
        y0=self.sol[index][1]
        x1=linelist[0][0].pos[0]
        y1=linelist[0][0].pos[1]
        z1=linelist[0][0].pos[2]
        z0=(array([x1,y1,z1])-array([x0,y0,0])).dot(n/n[2])
        uv=(array([x1,y1,z1])-array([x0,y0,0])).dot(n/n[2])
        return z0,uv
    def scan_conversion(self,triangle,pixbuf,test_color=None):
        linelist=[[triangle.vertexlist[0],triangle.vertexlist[1]],[triangle.vertexlist[1],triangle.vertexlist[2]],[triangle.vertexlist[2],triangle.vertexlist[0]]]
        xlist=[triangle.vertexlist[0].pos[0],triangle.vertexlist[1].pos[0],triangle.vertexlist[2].pos[0]]
        ylist=[triangle.vertexlist[0].pos[1],triangle.vertexlist[1].pos[1],triangle.vertexlist[2].pos[1]]

  
        randomcolor=[randint(0,255),randint(0,255),randint(0,255)]
        for index in triangle.bvh: #loop all pixels in BVH
        #for index in range(0,self.w*self.h):
>>>>>>> 21f6ded06283429d1a8f036e09cd8856dfa5d69b
            x0=self.sol[index][0]
            y0=self.sol[index][1]
            #if min(xlist)-self.pixelsize > x0 or max(xlist)+self.pixelsize < x0 or min(ylist)-self.pixelsize > y0 or max(ylist)+self.pixelsize < y0:
            #    continue
            mask=[False,False,False]
            is_hit=False
            ijk=[]
            for i,line in enumerate(linelist): #loop 3 times             
                x1=line[0].pos[0]
                x2=line[1].pos[0]
                y1=line[0].pos[1]
                y2=line[1].pos[1]
                exp = ( x0-x1)*(y2-y1)-(y0-y1)*(x2-x1)
                #continue
                #mask[i]=(exp<0)
                #if sum(mask)==3:
                #    is_hit = True
                if self.rastmode == "default":
                    if exp<0:
                        break
                    ijk.append(-exp/triangle.s)
                    if i==2:
<<<<<<< HEAD
                        #return
                    #Barycentric
                        count +=1
                        v0=linelist[0][0]
                        v1=linelist[0][1]
                        v2=linelist[1][1]
                        z0=v0.pos[2]                 
                        z1=v1.pos[2]
                        z2=v2.pos[2]
                        z= 1/(1/z1 +  (1/z2-1/z1)*ijk[0] + (1/z0-1/z1)*ijk[1])
                        #return 
                        if z0 < self.pixbuf[index][0][2]:
                            uv=(v0.uv*ijk[1]/z0+v2.uv*ijk[0]/z2+v1.uv*(1-ijk[0]-ijk[1])/z1)*z
                            color=v1.color +  (v2.color-v1.color)*ijk[0] + (v0.color-v1.color)*ijk[1]
                     
                            self.pixbuf[index][0][2]=z0 # refresh z-buffer
                            self.pixbuf[index][1]=color
                            self.pixbuf[index][3]=append(uv,0)
=======
                        #z0=self.Depthin(index,linelist)
                        color,z0,uv=self.Barycentric(index,linelist)
                        if z0 < pixbuf[index][0][2]:# and 374<uv[1]*512<414 and 83< uv[0]*512<120 :
                            pixbuf[index][0][2]=z0 # refresh z-buffer
                            pixbuf[index][1]=color
                            pixbuf[index][3]=append(uv,0)
                            #N=self.normal_interpolate(index,triangle.vertexlist)
                            #pixbuf[index][2]=self.normal_interpolate(index,triangle.vertexlist)
                            #M=pixbuf[index][2]
                            #pixbuf[index][1]=array(test_color)
>>>>>>> 21f6ded06283429d1a8f036e09cd8856dfa5d69b
                elif self.rastmode == "line":       
                    if exp < self.pixelsize and exp > -self.pixelsize: 
                        if min(x1,x2)-self.pixelsize <= x0 and max(x1,x2)+self.pixelsize>=x0 and min(y1,y2)-self.pixelsize<=y0 and max(y1,y2)+self.pixelsize>=y0 :
                            z0=self.Depthin(index,linelist)
<<<<<<< HEAD
                            if z0 <= self.pixbuf[index][0][2]:
                                self.pixbuf[index][1] = array([255,255,255])
                                self.pixbuf[index][0][2]=z0
                            break
        #return pixbuf
=======
                            if z0 <= pixbuf[index][0][2]:
                                pixbuf[index][1] = array([255,255,255])
                                pixbuf[index][0][2]=z0
                            break
                    #if is_hit:
                    #    pixbuf[index][1]=array([0,0,0])
            
        return pixbuf
>>>>>>> 21f6ded06283429d1a8f036e09cd8856dfa5d69b

    def run(self,scene,backcolor,depth):
        #pixbuf=[[[0,0,depth],backcolor]]*self.w*self.h
        self.pixbuf=[]
        for i in range(self.w*self.h):
<<<<<<< HEAD
            pix=[array(self.sol[i]+[depth]),array(backcolor),array([0.0,0.0,-1]),array([-1.0,-1.0,-1.0])]
            self.pixbuf.append(pix)
        #colortest=[[0,0,0],[255,0,0]]
        total= len(scene)
        for i,triangle in enumerate(scene):
            print("\r process {i}rd triangle ,total :{total}  ".format(i=i,total=total),end='')  
            self.scan_conversion(triangle)
        print('')
        return array(self.pixbuf)
=======
            pix=[array(self.sol[i]+[depth]),array(backcolor),array([0,0,-1]),array([-1,-1,-1])]
            pixbuf.append(pix)
        #colortest=[[0,0,0],[255,0,0]]
        total= len(scene)
        for i,triangle in enumerate(scene):
            print("process {i}rd triangle ,total :{total}".format(i=i,total=total))  
            #img = plt.imread("rabbit_texture.png")
            
            #plt.imshow(img[triangle.uvu:triangle.uvd,triangle.uvl:triangle.uvr])
            #plt.show()
            pixbuf = self.scan_conversion(triangle,pixbuf)
        return array(pixbuf)
>>>>>>> 21f6ded06283429d1a8f036e09cd8856dfa5d69b

        

