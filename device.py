from Image import *
from geometry import *
from rasterizaton import *
from pixel import *

class context():
    def __init__(self,size,viewport,center=[0,0]):
        self.size=size
        self.vp=viewport
        self.mode="default"
        self.blendmode="Default"
        self.geometrysh=geometryshader()
        self.rasterzior=rasterizor(size[0],size[1],viewport[0],viewport[1],center)
        self.w=size[0]
        self.h=size[1]
        self.pixelsh=pixelshader()
        self.vb=None
        self.ib=None
        self.cb=array([[72,117,135]]*self.size[0]*self.size[1]) #default backend
        self.backcolor=[72,117,135]
        self.imag = image(self.size[0],self.size[1],self.cb)
        self.drawnum=0
        self.lightlist=None
        self.layout=None
    def setvertex(self,vertexbuffer):
        self.vb=vertexbuffer
    def setindex(self,instancebuffer):
        self.ib=instancebuffer
    def cleanwindow(self):
        self.cb =array([self.backcolor]*self.size[0]*self.size[1])
        self.db = array([self.far]*self.size[0]*self.size[1])
    def set_farest_plane(self,far):
        self.far = far
        self.db = array([far]*self.size[0]*self.size[1])
    def set_mode(self,mode):
        self.mode=mode
        self.rasterzior.rastmode=mode
    def setblendmode(self,mode):
        self.blendmode=mode
    def setlight(self,lightlist):
        self.lightlist=lightlist
        self.geometrysh.lightlist=lightlist
        
    def inputlayout(self,vert=False,color=False,normal=False,uv=False):
        self.layout=[vert,color,normal,uv]
        self.geometrysh.layout=[vert,color,normal,uv]

    def makescence(self,vsout):
        scene=[]
        pixelsize=self.rasterzior.pixelsize
        orix=self.rasterzior.orix
        oriy=self.rasterzior.y+self.rasterzior.oriy
        idxarray=array(range(self.w*self.h))
        idxarray.shape=(self.w,self.h)
        #sol=self.rasterzior.sol
        if self.ib:
            total=int(len(self.ib)/3)
            d=0
            for i in range(0,len(self.ib),3): 
                d=d+1
                v0=vsout[self.ib[i]]
                v1=vsout[self.ib[i+1]]
                v2=vsout[self.ib[i+2]]
                tri=triangle([v0,v1,v2],self.w,self.h,orix,oriy,pixelsize,idxarray)
                if tri.culltest:
                    scene.append(tri) 
<<<<<<< HEAD
                    print("\r build {i}rd triangle ,total :{total}  ".format(i=d,total=total),end='')
                else:
                    print("\r cull {i}rd triangle ,total :{total}   ".format(i=d,total=total),end='')
=======
                    print("build {i}rd triangle ,total :{total}".format(i=d,total=total))
                else:
                    print("cull {i}rd triangle ,total :{total}".format(i=d,total=total))
>>>>>>> 21f6ded06283429d1a8f036e09cd8856dfa5d69b
        else:
            total=int(len(vsout)/3)
            d=0
            for i in range(0,len(vsout),3): 
                d=d+1
                tri=triangle(vsout[i:i+3],self.w,self.h,orix,oriy,pixelsize,idxarray)
                if tri.culltest:
                    scene.append(tri) 
<<<<<<< HEAD
                    print("\r build {i}rd triangle ,total :{total}  ".format(i=d,total=total),end='')
                else:
                    print("\r cull {i}rd triangle ,total :{total}   ".format(i=d,total=total),end='')      
        print('')
=======
                    print("build {i}rd triangle ,total :{total}".format(i=d,total=total))
                else:
                    print("cull {i}rd triangle ,total :{total}".format(i=d,total=total))        
>>>>>>> 21f6ded06283429d1a8f036e09cd8856dfa5d69b
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
 
        #if self.mode == "default":
        # default pipeline
            print ("begin draw{num}".format(num=self.drawnum))
            TIME={}    
            start = time.clock()
            outvs,lightlist=self.geometrysh.run(self.vb)
            #self.pixelsh.lightlist=lightlist
            TIME['geometry_stage'] = time.clock()-start
            start = time.clock()
            scence=self.makescence(outvs)
<<<<<<< HEAD
            TIME['build_scene'] = time.clock()-start
=======
            TIME['make_sence'] = time.clock()-start
>>>>>>> 21f6ded06283429d1a8f036e09cd8856dfa5d69b
            start = time.clock()
            pixelin=self.rasterzior.run(scence,self.backcolor,self.far)
            TIME['raster_stage'] = time.clock()-start
            start = time.clock()
            cb,db= self.pixelsh.run(pixelin) 
            TIME['pixel_stage'] = time.clock()-start
            start = time.clock()
            self.render(cb,db)
            TIME['render_stage'] = time.clock()-start
            self.imag.anylyze(TIME)
            self.imag.loaddata(self.cb)
            self.drawnum +=1
            return self.cb
    def show(self):
        self.imag.print(self.drawnum)              
    def runani(self):
        i=0
        while i<11:
            self.cleanwindow()
            self.geometrysh.lightlist[0].direct=self.geometrysh.lightlist[0].direct+array([1,0,0])
            self.run()
            self.imag.loaddata(self.cb)
            i+=1
    def showani(self):
        self.imag.printaction(self.drawnum)
    def showtk(self):
        self.imag.printtk(self.drawnum)

<<<<<<< HEAD
=======
        
>>>>>>> 21f6ded06283429d1a8f036e09cd8856dfa5d69b

