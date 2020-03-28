from numpy import *
from component import *
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
        zaxis = (self.at - self.camera)/linalg.norm(self.at - self.camera)
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