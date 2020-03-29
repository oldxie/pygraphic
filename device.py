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
        self.pixelsh=pixelshader()
        self.vb=None
        self.ib=None
        self.cb=array([[72,117,135]]*self.size[0]*self.size[1]) #default backend
        self.backcolor=[72,117,135]
        self.imag = image(self.size[0],self.size[1],self.cb)
        self.drawnum=0
        self.lightlist=None
    def setvertex(self,vertexbuffer):
        self.vb=vertexbuffer
    def setindex(self,instancebuffer):
        self.ib=instancebuffer
    def creatwindow(self,rgb):
        self.cb = [rgb]*self.size[0]*self.size[1]
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
            pixelin=self.rasterzior.run(scence,self.backcolor,self.far)
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
