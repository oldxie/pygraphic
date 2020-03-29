from numpy import *
from component import *
class geometryshader():
    def __init__(self):
        self.lightlist=None
        self.posbuf=[]
        self.colorbuf=[]
        self.normalbuf=[]
        self.lightlist=[]
        pass
    def setlootat(self,position):
        self.at=array(position)
    def setCamera(self,position):
        self.camera=array(position)

    def setnear(self,distance):
        self.near=distance
        #fix me

    def maketranview(self):
        zaxis = (self.at - self.camera)/linalg.norm(self.at - self.camera)
        xaxis = cross(array([0.0,1.0,0.0]), zaxis)
        yaxis = cross(zaxis, xaxis)
        self.viewmatrix=array([xaxis,yaxis,zaxis]).T
    def lightfunction(self):
        for light in self.lightlist:
            args=array(self.normalbuf).dot(light.direct)
            args=(args-args.min())/(args.max()-args.min())
            args.shape=(self.size,1)
            self.colorbuf+= args.dot([light.color])
        self.colorbuf =self.colorbuf*255/self.colorbuf.max()
    def distribute(self,vb):
        self.size=len(vb)
        self.index=range(self.size)
        for v in vb:
            self.posbuf.append(v.pos)
            self.colorbuf.append(array([255,255,255]))
            self.normalbuf.append(v.normal)
    def output(self):
        vsoutbuf=[]
        self.lightfunction()
        for i in self.index:
            vsoutbuf.append(vertex(self.posbuf[i],self.colorbuf[i]))
        return vsoutbuf
    def run(self,vertexbuffer):
        self.maketranview()
        self.distribute(vertexbuffer)
        #posbuf=
        #for i in self.index:
        self.posbuf=array(self.posbuf).dot(self.viewmatrix)
        
        #norm=vsvertex.normal
        #vsoutbuf.append(vertex(pos,color))
        return self.output()