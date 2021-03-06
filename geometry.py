from numpy import *
from component import *
class geometryshader():
    def __init__(self):
        self.lightlist=None 
        self.layout=[]
        self.posbuf=[]
        self.colorbuf=[]
        self.normalbuf=[]
        self.uvbuf=[]
<<<<<<< HEAD
        self.lookup=array([0.0,1.0,0.0])
=======
>>>>>>> 21f6ded06283429d1a8f036e09cd8856dfa5d69b
    def setlootat(self,position):
        self.at=array(position)
    def setCamera(self,position):
        self.camera=array(position)
        self.z=position[2]
<<<<<<< HEAD
    def setlookup(self,direction):
        self.lookup=array(direction)
=======

>>>>>>> 21f6ded06283429d1a8f036e09cd8856dfa5d69b
    def setnear(self,distance):
        self.near=distance
        #fix me
    def maketranview(self):
        zaxis = (self.at - self.camera)/linalg.norm(self.at - self.camera)
<<<<<<< HEAD
        xaxis = cross(self.lookup, zaxis)
=======
        xaxis = cross(array([0.0,0.0,1.0]), zaxis)
>>>>>>> 21f6ded06283429d1a8f036e09cd8856dfa5d69b
        yaxis = cross(zaxis, xaxis)
        bias=[-xaxis.dot(self.camera),-yaxis.dot(self.camera),-zaxis.dot(self.camera),1]
        self.viewmatrix = column_stack((array([xaxis,yaxis,zaxis,[0,0,0]]),bias)).T
        
    def BuildProjectionMatrix(self,fov,aspect,zn,zf):
        proj=zeros((4,4),dtype='float')
        proj[0][0] = 1 / (tan(fov * 0.5) *aspect) ;
        proj[1][1] = 1 / tan(fov * 0.5) ;
        proj[2][2] = zf / (zf - zn) ;
        proj[2][3] = 1.0; 
        proj[3][2] = (zn * zf) / (zn - zf);
        self.proj = proj
    def lightfunction(self):
<<<<<<< HEAD
        if self.lightlist == None:
            return
        for light in self.lightlist:
            if light.mode == "parell":
                args=-array(self.normalbuf).dot(light.direct)
=======
        if len(self.lightlist) == 0:
            return
        for light in self.lightlist:
            if light.mode == "parell":
                #r=linalg.norm(light.direct)
                #light.direct=light.direct/r
                args=-array(self.normalbuf).dot(light.direct)
                #args=(args*(args>0))
>>>>>>> 21f6ded06283429d1a8f036e09cd8856dfa5d69b
                args=(args-args.min())/(args.max()-args.min())
                args.shape=(self.size,1)
                self.colorbuf+= args.dot([light.color])
            elif light.mode=="spot":
                direct=array(self.posbuf)[:,0:3] - light.src
                r=linalg.norm(direct,axis =1)
<<<<<<< HEAD
                args=(-array(self.normalbuf)*array(direct)).sum(1)
                args=(args)/r
                args=(args-args.min())/(args.max()-args.min())
                args.shape=(len(args),1)
                self.colorbuf+= args.dot([light.color])
        #if self.colorbuf.max>255:
        #self.colorbuf =self.colorbuf*255/self.colorbuf.max()
=======
                #dmask=self.depthbuf<100
                args=(-array(self.normalbuf)*array(direct)).sum(1)
                args=(args)/r
                #r=r*(args>0)
                args=(args-args.min())/(args.max()-args.min())
                args.shape=(len(args),1)
                self.colorbuf+= args.dot([light.color])
        self.colorbuf =self.colorbuf*255/self.colorbuf.max()
>>>>>>> 21f6ded06283429d1a8f036e09cd8856dfa5d69b

    def distribute(self,vb):
        self.size=len(vb)
        self.index=range(self.size)
        for v in vb:
            if self.layout[0]== True:
                self.posbuf.append(v.pos)
            else:
                self.posbuf.append(array([0,0,0,1]))
            if self.layout[1]== True:
                self.colorbuf.append(v.color)
            else:
<<<<<<< HEAD
                self.colorbuf.append(array([0.0,0.0,0.0]))
            if self.layout[2]== True:
                self.normalbuf.append(v.normal)
            else:
                self.normalbuf.append(array([0.0,0.0,0.0]))
            if self.layout[3]== True:
                self.uvbuf.append(v.uv)
            else:
                self.uvbuf.append(array([0.0,0.0]))
=======
                self.colorbuf.append(array([0,0,0]))
            if self.layout[2]== True:
                self.normalbuf.append(v.normal)
            else:
                self.normalbuf.append(array([0,0,0]))
            if self.layout[3]== True:
                self.uvbuf.append(v.uv)
            else:
                self.uvbuf.append(array([0,0]))
            #if self.layout[3]== True:
            #    self.normalbuf.append(v.uv)
            #else:
            #    self.colorbuf.append(array([0,0]))
>>>>>>> 21f6ded06283429d1a8f036e09cd8856dfa5d69b

    def output(self):
        vsoutbuf=[]
        for i in self.index:
            z=self.posbuf[i][3]
            vsoutbuf.append(vertex(self.posbuf[i][0:-1]/z,self.colorbuf[i],self.normalbuf[i],self.uvbuf[i]))
<<<<<<< HEAD
=======
        self.layout=[]
>>>>>>> 21f6ded06283429d1a8f036e09cd8856dfa5d69b
        self.posbuf=[]
        self.colorbuf=[]
        self.normalbuf=[]
        self.uvbuf=[]
<<<<<<< HEAD
=======
        #self.lightlist=[]
>>>>>>> 21f6ded06283429d1a8f036e09cd8856dfa5d69b
        return vsoutbuf,self.lightlist

    def run(self,vertexbuffer):
        self.maketranview()
        self.BuildProjectionMatrix(3.14/4,1,1,100)
        self.distribute(vertexbuffer)
        self.lightfunction()
        self.posbuf=array(self.posbuf).dot(self.viewmatrix)
<<<<<<< HEAD
=======
        t_posbuf=self.posbuf
        #t_posbuf = column_stack((self.t_posbuf,[1]*self.t_posbuf.shape[0]))
>>>>>>> 21f6ded06283429d1a8f036e09cd8856dfa5d69b
        self.posbuf = self.posbuf.dot(self.proj)
        x_buf=self.posbuf 
        xc=x_buf[:,0].max() + x_buf[:,0].min()
        yc=x_buf[:,1].max() + x_buf[:,1].min()
        return self.output()